"""查看和编辑状态"""
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command

"""查看和编辑状态"""
class State(TypedDict):
    text:str

def review_node(state:State):
    """通过中断，让审查者编辑生成的内容"""
    update=interrupt({
        "instruction":"查看并编辑内容",
        "content":state["text"]
    })
    return {
        "text":update
    }
builder=StateGraph(State)
builder.add_node(review_node)
builder.add_edge(START,"review_node")
builder.add_edge("review_node",END)
graph=builder.compile(checkpointer=InMemorySaver())
config={"configurable":{"thread_id":"111"}}

result=graph.invoke({"text":"待审核文张"},config)

print(result)
result2=graph.invoke(Command(resume="已审核"),config)
print(result2)

