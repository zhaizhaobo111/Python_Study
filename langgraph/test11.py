import operator

import operator
import uuid
from typing import TypedDict, Annotated, Optional, List

from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage, SystemMessage, ToolMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph, state
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore
from pydantic import BaseModel, Field

# 准备工作
# 搜索模型返回消息最大数 4
search=TavilySearch(max_results=4)
# 定义工具列表 【search】
tools=[search]
# 定义模型
model=init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
# 准备工作
class Person(BaseModel):
    name:Optional[str]=Field(None,description="用户姓名")
    height:Optional[str]=Field(None,description="用户身高")
    favorite:Optional[List[str]]=Field(None,description="用户最喜欢的美食偏好")
# 工具绑定
model_with_tool=model.bind_tools(tools)
# 定义结构化输出模型
model_with_structured=model.with_structured_output(Person)
# 1.状态
class MessagesState(TypedDict):
    # 定义消息
    # operator.add 追加消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 调用大模型次数
    llm_calls:int
    # llm_calls:Annotated[int,operator.add]
# 2.定义节点
# 节点1
def get_person_by_llm(state:MessagesState,config:RunnableConfig,*,store:BaseStore):
    """LLM决定是否调用工具"""
    people_info=model_with_structured.invoke(
       [
           SystemMessage(content="你是⼀个提取信息的专家，只从⽂本中提取我的相关信息，"
                                 "不能提取别⼈的信息。如果你不知道要提取的属性的值，属性值返回null。")
       ] + state["messages"][-3:]
   )
    user_id=config["configurable"]["user_id"]
    namespace1=(user_id,"info")
    # put之前有个查询有没有操作
    store.put(
        namespace1,
        str(uuid.uuid4()),
        {
            "name":people_info.name,
            "height":people_info.height,
        }
    )
    user_id = config["configurable"]["user_id"]
    namespace2 = (user_id, "pre")
    store.put(
        namespace2,
        str(uuid.uuid4()),
        {
            "favorite":people_info.favorite
        }
    )
    return {
        "llm_calls":state.get("llm_calls",0)+1
    }

def llm_call(state:MessagesState,config:RunnableConfig,*,store:BaseStore):
    """LLM决定是否调用工具"""
    user_id = config["configurable"]["user_id"]
    namespace1 = (user_id, "info")
    namespace2 = (user_id, "pre")
    info_result=store.search(namespace1,limit=1)
    pre_result=store.search(namespace2,limit=1)
    print(info_result)
    print(pre_result)


    # messages 接受返回的所有消息HumanMessage、AIMessage、ToolMessage
    messages=state["messages"]
    # result 可能性1：有tool_call 的AImessage
    # result 可能性2：无tool_call 的AImessage

    result=model_with_tool.invoke(
        [
            SystemMessage(
                content=f"你是⼀个乐于助⼈的助⼿，⽀持调⽤⼯具进⾏搜索。")

        ] +[HumanMessage(content= f"查询 LLM 前必须参考以下信息："
                        f"1. ⽤⼾基本情况：{info_result[0].value} "
                        f"2. ⽤⼾偏好情况：{pre_result[0].value}")]
           +messages
    )
    return {
        "messages":[result],
        "llm_calls":state.get("llm_calls",0)+1 #覆盖更新
    }

tools_by_name={
    tool.name:tool for tool in tools
}
# 节点2
# result可能性1会走到tool_node
def tool_node(state:MessagesState,config:RunnableConfig,*,store:BaseStore):
    """执行工具调用"""
    # result 是tool_message
    result=[]
    # 当前最新的消息就是 带有tool_calls的AiMessage
    # tool_calls 这条 AIMessage 里的工具调用指令
    for tool_call in state["messages"][-1].tool_calls:
        # 可以获取tool_call的name、agrs、id
        # tool_call["name"]AI告诉你：我要调用哪个工具
        tool=tools_by_name[tool_call["name"]]
        obs=tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=obs,tool_call_id=tool_call["id"]))
    return {
        "messages": result,
    }
agent_builder=StateGraph(MessagesState)
# 定义点
agent_builder.add_node(get_person_by_llm)
agent_builder.add_node(llm_call)
agent_builder.add_node(tool_node)
# 定义边
agent_builder.add_edge(START,"get_person_by_llm")
agent_builder.add_edge("get_person_by_llm","llm_call")
# 定义条件边
def should_call(state:MessagesState):
    # """根据LLM是否调⽤⼯具来决定是应该继续循环（路由到⼯具节点）还是停⽌循环（END）"""
    # 最新消息是AIMessage
   last_message=state["messages"][-1]
   if last_message.tool_calls:
        return "tool_node"
   return END

agent_builder.add_conditional_edges(
    "llm_call",
    should_call,
    ["tool_node",END]
)
agent_builder.add_edge("tool_node","get_person_by_llm")
# 4.编译图
agent_search=agent_builder.compile(checkpointer=InMemorySaver(),store=InMemoryStore())
config1={"configurable":{"thread_id":"1111","user_id":"user_123"}}
# 5.执行图
messages1 = agent_search.invoke({
    "messages": [
        HumanMessage(content="我叫小猫,183，我喜欢吃芝士汉堡")
    ]
},config1)
# print(f"调⽤ LLM 总次数：{messages1["llm_calls"]}次")
# for m in messages1["messages"]:
#     m.pretty_print()
messages1["messages"][-1].pretty_print()



config2={"configurable":{"thread_id":"2222","user_id":"user_123"}}
messages2 = agent_search.invoke({
    "messages": [
        HumanMessage(content="给我推荐个餐厅")
    ]
},config2)
# print(f"调⽤ LLM 总次数：{messages2["llm_calls"]}次")
# for m in messages2["messages"]:
#     m.pretty_print()
messages2["messages"][-1].pretty_print()