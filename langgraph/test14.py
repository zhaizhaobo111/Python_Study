from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command


class State(TypedDict):
    input:str
    output:str

def node(state:State):
    """中断操作"""
    # 中断恢复后，从调用interrupt开始
    # 因此对于从调用interrupt开始前代码进行幂等
    print("111111111111111111111111111")
    # 定义中断
    decision=interrupt("结束还是继续？yes表示继续，no表示结束")
    if decision == "yes":
        return {
            "output":"您好，我是你的贴心助手"
        }
    else:
        return {
            "output": "人工结束工作流"
        }
graph=StateGraph(State)
graph.add_node(node)
graph.add_edge(START,"node")
graph.add_edge("node",END)
# 外部
build=graph.compile(checkpointer=InMemorySaver())
config={"configurable":{"thread_id":123}}
result=build.invoke({"input": "hi"}, config=config)
print(result)
print(result["__interrupt__"][0].value)
# 恢复：将Command对象发送给图
print(build.invoke(Command(resume="yes"), config=config))
# LangGraph 的 interrupt 恢复机制，只会恢复一次
# {'input': 'hi', '__interrupt__': [Interrupt(value='结束还是继续？yes表示继续，no表示结束', id='63b3f5fc3982949a02e025ea94176150')]}
# {'input': 'hi', 'output': '您好，我是你的贴心助手'}
# {'input': 'hi', 'output': '您好，我是你的贴心助手'}
# ，必须重新开线程 / 重置状态，不能复用同一个 config
print(build.invoke(Command(resume="no"), config=config))
