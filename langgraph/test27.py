"""子图"""
from typing import TypedDict

from langgraph.constants import END, START
from langgraph.graph import StateGraph

"""方式1.节点内调用"""
# 定义子图
class SubState(TypedDict):
    sub1:str
    sub2:str
def sub_node1(state:SubState):
    return {"sub1":"这里是是sub1"}

def sub_node2(state:SubState):
    return {"sub2":"这里是sub1和sub2"+state["sub2"]+state["sub1"]}

sub_builder=StateGraph(SubState)
sub_builder.add_node(sub_node1)
sub_builder.add_node(sub_node2)
sub_builder.add_edge(START,"sub_node1")
sub_builder.add_edge("sub_node1","sub_node2")
sub_builder.add_edge("sub_node2",END)

sub_graph=sub_builder.compile()
# print(sub_graph.invoke({"sub2": "这里是小猫"}))

# 定义主图
class ParentState(TypedDict):
    parent:str

def parent_node1(state:ParentState):
    return {"parent":"这里是"+state["parent"]}

def parent_node2(state:ParentState):
    # 获取子节点,子图必须先编译
    # 把当前主图的 parent 值传给子图
    result=sub_graph.invoke({"sub2":state["parent"]})
    return {"parent":result["sub2"]}
builder=StateGraph(ParentState)
builder.add_node(parent_node1)
builder.add_node(parent_node2)
builder.add_edge(START,"parent_node1")
builder.add_edge("parent_node1","parent_node2")
builder.add_edge("parent_node2",END)
graph=builder.compile()
# "这里是sub1和sub2" + state["sub2"] + state["sub1"]
# print(graph.invoke({"parent":"主图"}))
# for chunk in graph.stream({"parent": "parent"}, subgraphs=True):
#     print(chunk)

print(graph.get_graph(xray=True).draw_mermaid())