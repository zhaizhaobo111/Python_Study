""" 工作流的提示链模式"""
# 1.定义输入模式-只包含用户的输入
from typing import TypedDict

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.constants import START
from langgraph.graph import StateGraph

model=init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0)
class InputState(TypedDict):
    #     主题
    topic:str

# 2.定义输出模式-只包含最终的结果
class OutState(TypedDict):
    # 最终内容
    final_content:str

# 3.定义完整状态模式
class OverState(InputState,OutState):
    # 1.生成大纲
    outline:str
    # 2.生成初稿
    draft:str
    # 3.润色
    polished_draft:str

PROMPT_1 = (
    "根据主题⽣成⽂章⼤纲。\n"
    "主题：{topic}\n"
    "要求："
    "1.只需两个最核⼼标题"
    "2.不⽤进⾏说明，只返回最终⼤纲"
)
def node1(state:InputState):
    """根据主题⽣成内容⼤纲"""
    print("*" * 50)
    print(f"内容⼤纲⽣成中...\n")
    topic=state["topic"]
    prompt=PROMPT_1.format(topic=topic)
    result=model.invoke([HumanMessage(content=prompt)]).content
    print(f"⼤纲已⽣成：\n{result}\n")
    return {
        "outline":result,
        "topic":state["topic"]
    }
PROMPT_2 = (
    "根据以下内容⽣成⽂章完整初稿。\n"
    "主题：{topic}\n"
    "⼤纲: "
    "{outline}\n"
    "要求："
    "1.每个标题下，最多使⽤三句话的内容即可"
    "2.不⽤进⾏说明，只返回最终结果"
)
def node2(state:OverState):
    """根据⼤纲⽣成完整初稿"""
    print("*" * 50)
    print(f"⽣成初稿中...\n")
    topic=state["topic"]
    outline=state["outline"]
    prompt=PROMPT_2.format(topic=topic,outline=outline)
    result=model.invoke([HumanMessage(content=prompt)]).content
    print(f"初稿已⽣成：\n{result}\n")
    return {
        "draft":result
    }

PROMPT_3 = (
    "根据⽂章初稿进⾏润⾊。\n"
    "主题：{topic}\n"
    "初稿: "
    "{draft}\n"
    "要求："
    "1.润⾊后，⽂章不能太⻓"
)
def node3(state: OverState):
    """对初稿进⾏润⾊优化"""
    print("*" * 50)
    print(f"⽂章润⾊中...\n")
    topic=state["topic"]
    draft=state["draft"]
    prompt=PROMPT_3.format(topic=topic,draft=draft)
    result=model.invoke([HumanMessage(content=prompt)]).content
    print(f"润⾊完成，内容如下：\n{result}\n")
    return {
        "polished_draft":result
    }
PROMPT_4 = (
    "根据润⾊版⽂章，⽣成⽂章终稿。\n"
    "主题：{topic}\n"
    "⼤纲: "
    "{outline}\n"
    "润⾊版⽂章: "
    "{polished_draft}\n"
)
def node4(state: OverState):
    """⽣成最终版本的内容"""
    print("*" * 50)
    print(f"最终文章生成中...\n")
    prompt=PROMPT_4.format(topic=state["topic"],outline=state["outline"],polished_draft=state["polished_draft"])
    result=model.invoke([HumanMessage(content=prompt)]).content
    print(f"最终文章，内容如下：\n{result}\n")
    return {
        "final_content":result,
    }
builder=StateGraph(OverState,input_schema=InputState,output_schema=OutState)
builder.add_sequence([node1,node2,node3,node4])
builder.add_edge(START,"node1")
chain=builder.compile()
result=chain.invoke({"topic":"计算机学生的未来就业？"})
print(result)


