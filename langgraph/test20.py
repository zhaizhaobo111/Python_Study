"""运行时上下文"""
from dataclasses import dataclass
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime



# 静态上下文
@dataclass
class Context:
    user_id:str
    language:str="En"

class State(TypedDict):
    user_name:str
    message:list[str]

def node(state:State,runtime:Runtime[Context]):
    # 静态运行时上下文
    if runtime.context.language=="En":
        greeting="hello"
    else:
        greeting="你好"
    # 动态运行时上下文
    user_name=state.get("user_name","Guest")
    return {
        "message":[f"{greeting},{user_name}"]
    }
builder=StateGraph(State,context_schema=Context)
builder.add_node(node)
builder.add_edge(START,"node")
builder.add_edge("node",END)
graph=builder.compile()

print(graph.invoke(
    {"user_name": "张三"},
    context={"user_id": "123","language": "英文"}))