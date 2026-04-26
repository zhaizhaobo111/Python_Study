"""LangGraph 持久化（Persistence）"""

#这里沿用 案例二的代码
# """支持搜索的智能代理系统"""

import operator
from typing import TypedDict, Annotated

from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage, SystemMessage, ToolMessage, HumanMessage
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph, state

# 准备工作
# 搜索模型返回消息最大数 4
search=TavilySearch(max_results=4)
# 定义工具列表 【search】
tools=[search]
# 定义模型
model=init_chat_model(
    model="qwen-turbo",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
# 工具绑定
model_with_tool=model.bind_tools(tools)
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
def llm_call(state:MessagesState):
    """LLM决定是否调用工具"""
    # messages 接受返回的所有消息HumanMessage、AIMessage、ToolMessage
    messages=state["messages"]
    # result 可能性1：有tool_call 的AImessage
    # result 可能性2：无tool_call 的AImessage
    result=model_with_tool.invoke(
        [
            SystemMessage(content="你是一位乐于助人的助手，支持文件调用和搜索")
        ]
        + messages
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
def tool_node(state:MessagesState):
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
# 3.定义图、添加节点、边
# 定义图
agent_builder=StateGraph(MessagesState)
# 定义点
agent_builder.add_node(llm_call)
agent_builder.add_node(tool_node)
# 定义边
agent_builder.add_edge(START,"llm_call")
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
agent_builder.add_edge("tool_node","llm_call")


# 4.编译图
# 内存存储
# 最简单的⽅式，状态保存在程序内存中。适⽤于开发和测试，程序重启后状态会丢失。⽤法如下所
# ⽰
# checkpointer=InMemorySaver()
# agent_search=agent_builder.compile(checkpointer=checkpointer)
# DB_URI="postgresql://postgres:bit@localhost:5432/postgres"
# with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
#     # 第一次调用Postgres需要调用checkpointer.setup()
#     checkpointer.setup()
#     agent_search=agent_builder.compile(checkpointer=checkpointer)



    # config={"configurable":{"thread_id":"1"}}
    # 获取最新快照状态
    # #     调用前
    # # snapshot=agent_search.get_state(config)
    # # print(snapshot)
    # result = agent_search.invoke(
    #     {"messages": [HumanMessage(content="今天烟台天气怎么样")]},
    #     config
    # )
    # print(f"调用LLM的次数:{result['llm_calls']}次")
    # for m in result["messages"]:
    #     m.pretty_print()
    #     调用后
    # snapshot = agent_search.get_state(config)
    # print(snapshot)
# ----------------------------------------------------------------------------
#     config = {"configurable": {"thread_id": "1"}}
#     result1 = agent_search.invoke(
#         {"messages": [HumanMessage(content="你好")]},
#         config
#     )
#     # 查看状态历史记录
#     history = list(agent_search.get_state_history(config))
#     print(history)
# ----------------------------------------------------------------------------
    # config = {"configurable": {"thread_id": "1"}}
    # result = agent_search.invoke(
    #     {"messages": [HumanMessage(content="我刚才问的什么")]},
    #     config
    # )
    # print(f"调用LLM的次数:{result['llm_calls']}次")
    # for m in result["messages"]:
    #     m.pretty_print()
# 5.执行图
# messages = agent_search.invoke({
#     "messages": [
#         HumanMessage(content="明天烟台的天⽓怎样？")
#     ]
# })
# print(f"调⽤ LLM 总次数：{messages["llm_calls"]}次")
# for m in messages["messages"]:
#  m.pretty_print()


# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# try:
#     # ⽣成 Mermaid 图表并保存为图⽚
#     mermaid_code = agent_search.get_graph(xray=True).draw_mermaid_png()
#     # 保存⽂件
#     with open("../Docs/graph1.jpg", "wb") as f:
#         f.write(mermaid_code)
#     #使⽤ matplotlib 显⽰图像
#     img = mpimg.imread("../Docs/graph1.jpg")
#     plt.imshow(img) # 显⽰图⽚
#     plt.axis('off') # 关闭坐标轴
#     plt.show() # 弹出窗⼝显⽰图⽚
# except Exception as e:
#     print(f"An error occurred: {e}")


'''实现重放功能'''
DB_URI="postgresql://postgres:bit@localhost:5432/postgres"
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    # 第一次调用Postgres需要调用checkpointer.setup()
    checkpointer.setup()
    agent_search=agent_builder.compile(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "33"}}
    # 第⼀次执⾏
    result1 = agent_search.invoke(
        {"messages": [HumanMessage(content="今天烟台莱山区天气怎么样")]},
        config
    )
    # 打印最新消息
    result1["messages"][-1].pretty_print()

    result1 = agent_search.invoke(
        {"messages": [HumanMessage(content="我刚才问的什么")]},
        config
    )
    # 打印全部消息
    for r in  result1["messages"]:
        r.pretty_print()




    # 保存调⽤⼯具前的状态
    # print("-" * 80)
    # print(f"第⼀次执⾏历史：")
    to_replay = None
    for snapshot in agent_search.get_state_history(config):
        print("checkpoint_id: ", snapshot.config["configurable"]["checkpoint_id"])
        print( "下⼀节点: ", snapshot.next)
        print("\n")
        # 遍历所有历史 → 找到 ID  → 把它存起来，准备重新运行
        # if snapshot.config["configurable"]["checkpoint_id"]== "1f141646-00ee-67d2-8005-1be46877f28e":
        #     # print("state:",snapshot.values["messages"][-1])
        #     to_replay=snapshot

    # 重放（从指定的快照开始执行）
    # result=agent_search.invoke(None,config=to_replay.config)
    # print(result)