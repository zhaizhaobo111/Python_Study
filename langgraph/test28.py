"""子图"""
from typing import TypedDict

from langgraph.constants import END, START
from langgraph.graph import StateGraph

"""2 ⽅式⼆：将⼦图作为节点（共享状态模式）"""
# 定义子图
class SubState(TypedDict):
    parent:str  #共享父类状态
    sub:str     #sub私有

def sub_node1(state:SubState):
    return {"sub":"这是sub"}

def sub_node2(state:SubState):
    return {"parent":state["parent"]+state["sub"]}

sub_builder=StateGraph(SubState)
sub_builder.add_node(sub_node1)
sub_builder.add_node(sub_node2)
sub_builder.add_edge(START,"sub_node1")
sub_builder.add_edge("sub_node1","sub_node2")
sub_builder.add_edge("sub_node2",END)

sub_graph=sub_builder.compile()
print(sub_graph.invoke({"parent":"parent"}))
# 定义主图
class ParentState(TypedDict):
    parent:str
def node1(state:ParentState):
    return {"parent":"这里是"+state["parent"]}
builder=StateGraph(ParentState)
builder.add_node(node1)
# 将⼦图作为节点,必须先编译
builder.add_node("node2",sub_graph)
builder.add_edge(START,"node1")
builder.add_edge("node1","node2")
builder.add_edge("node2",END)

graph=builder.compile()
# 子图里读到的 state 就是：主图前面所有节点执行完的最终状态
# 前面节点 return 什么，子图就拿到什么
# print(graph.invoke({"parent":"parent"}))

# {'node1': {'parent': '这里是parent'}}
# {'node2': {'parent': '这里是parent这是sub'}}
# sub_node2 执行 → {"parent": "这里是parent" + "这是sub"}  这里的parent 是 主图node1返回的parent覆盖的
for chunk in graph.stream({"parent": "parent"}):
    print(chunk)