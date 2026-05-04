"""custom思考模式"""
import time

"""流模式与基本算法"""
from dataclasses import dataclass

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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
    user_id = runtime.context.user_id
    # TypedDict 是一个字典
    user_name = runtime.state["user_name"]
    # print(f"日志记录：user_id:{user_id}, user_name:{user_name}")
    # 获取流式写入器
    writer=get_stream_writer()
    writer({
        "type":"search_node",
        "status":"start",
        "user_id": user_id,
        "user_name": user_name,
    })
    # 搜索步骤
    search_steps = [
    {
        "name": "搜索1",
        "time": 1,
        "result": "晴天"
    },
    {
        "name": "搜索2",
        "time": 1.5,
        "result": "15-20°"
    }]


    all_result="查询天气: "
    for i, step in enumerate(search_steps, 1):
        writer({
            "type": "search_node",   #搜索类型
            "status": "searing",     #搜索状态
            "cur_step":i,            #现在第几步
            "step":step["name"],     #步骤名
            "all_steps":len(search_steps),#总共多少步
            "user_id":user_id,
            "user_name":user_name,
        })
        # 模拟思考时间
        time.sleep(step["time"])
        # 模拟查询结果
        all_result+=step["result"]

    writer({
        "type": "search_node",
        "status": "end",
        "user_id":user_id,
        "user_name":user_name,
        "result": all_result,  # 最后结果
    })
    return all_result

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
print("已思考.....")
for chunk in graph.stream({
    "messages":[HumanMessage(content="今天烟台莱山区天气怎么样")],
    "user_name":"小猫"
},context={
    "user_id":"123"
# values → 输出完整状态
},stream_mode=["custom","values"]):
    # print(chunk)
    # ('custom', {'type': 'llm_call', 'status': 'start', 'messages': '开始调用大模型', 'content': '今天烟台莱山区天气怎么样'})
    if chunk[0]=="custom":
        # 把后面内容拿出来，比如：{'type': 'llm_call', 'status': 'start', 'messages': '开始调用大模型', 'content': '今天烟台莱山区天气怎么样'})
        info=chunk[-1]
        if info.get("type")=="search_node":
            status=info.get("status")
            if status=="start":
                pass
                print(f"用户id :{info["user_id"]},用户名称:{info["user_name"]}  开始调用工具.......")
            elif status=="searing":
                print(f"进度{info["cur_step"]}/{info["all_steps"]}正在处理{info["step"]}....")
            elif status=="end":
                print(f"搜索完成!{info["result"]}")
        elif info.get("type")=="llm_call":
            pass
    elif chunk[0] == "values":
        info = chunk[-1]
        # s是AIMessages且不包含tool_calls就是最后一条消息就打印
        if isinstance(info["messages"][-1],AIMessage) and not info["messages"][-1].tool_calls:
            print("最终结果：")
            print(info["messages"][-1].content)