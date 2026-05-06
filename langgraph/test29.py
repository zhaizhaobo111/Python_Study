"""子图中添加短期记忆（checkpoint）"""
# 如果图包含⼦图 ，则只需在编译⽗图时提供 checkpoint 。LangGraph 会⾃动将 checkpoint 传播到⼦图。
from langgraph.graph import START, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict
class State(TypedDict):
    foo: str
# ⼦图
def subgraph_node_1(state: State):
    return {"foo": state["foo"] + "bar"}
subgraph_builder = StateGraph(State)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")

subgraph = subgraph_builder.compile()
# 主图
builder = StateGraph(State)
builder.add_node("node_1", subgraph)
builder.add_edge(START, "node_1")
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)