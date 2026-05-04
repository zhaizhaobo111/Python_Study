"""流模式与基本算法"""
from dataclasses import dataclass

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.config import get_stream_writer
from langgraph.constants import START, END
from langgraph.graph import MessagesState, StateGraph
from langgraph.prebuilt import ToolRuntime, ToolNode, tools_condition


class State(MessagesState):
    user_name:str=""

@dataclass
class Context:
    user_id:str

def search(runtime:ToolRuntime[Context]):
    """搜索工具"""
    # 获取流式写入器
    writer=get_stream_writer()
    writer({
        "type":"search_node",
        "status":"start",
    })
    user_id=runtime.context.user_id
    # TypedDict 是一个字典
    user_name=runtime.state["user_name"]
    # print(f"日志记录：user_id:{user_id}, user_name:{user_name}")
    writer({
        "type": "search_node",
        "status": "searing",
        "user_id":user_id,
        "user_name":user_name,
    })
    writer({
        "type": "search_node",
        "status": "end",
        "user_id":user_id,
        "user_name":user_name,
    })
    return f"user_id:{user_id},user_name:{user_name} 查询天气，晴天：15-20°",

model_with_tool=init_chat_model(
    model="qwen-turbo",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
).bind_tools([search])

def llm_call(state:State):
    # 获取流式写入器
    writer = get_stream_writer()
    writer({
        "type": "llm_call",
        "status": "start",
        "messages": "开始调用大模型",
        "content":state["messages"][-1].content,
    })
    messages = [  #  [老板要求] + [用户问题]
                   SystemMessage(content="你是天气助手，必须调用工具查询天气")
               ] + state["messages"]

    result = model_with_tool.invoke(messages)
    writer({
        "type": "llm_call",
        "status": "end",
        "messages": "结束调用大模型",
    })
    return {
        "messages": [result]
    }

builder=StateGraph(State,context_schema=Context)
builder.add_node(llm_call)
# 定义成工具节点
builder.add_node("tool_node",ToolNode([search]))
builder.add_edge(START,"llm_call")
builder.add_conditional_edges(
    "llm_call",
    tools_condition,
    {
        "tools":"tool_node",
        "__end__":END
    }
)
builder.add_edge("tool_node","llm_call")
graph=builder.compile()
# 流式输出
for chunk in graph.stream({
    "messages":[HumanMessage(content="今天烟台莱山区天气怎么样")],
    "user_name":"小猫"
},context={
    "user_id":"123"
# updates 格式 = {节点名: { 更新的状态} }
},stream_mode=["custom","updates"]):
    print(chunk)
    # for node,update in chunk.items():
    #     # 流式输出：一个节点一个节点遍历
    #     print(f"节点{node}更新的消息如下")
    #     update["messages"][-1].pretty_print()
