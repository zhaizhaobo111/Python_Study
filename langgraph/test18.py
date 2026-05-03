"""验证人机输入"""
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command


class FormState(TypedDict):
    age:int|None
def get_age_node(state:FormState):
    prompt="你今年多大？"
    while  True:
        answer=interrupt(prompt)
        if isinstance(answer,int) and answer>0:
            return {
                "age":answer
            }
        prompt=f"{answer} 不是一个有效的年龄"

builder=StateGraph(FormState)
builder.add_node(get_age_node)
builder.add_edge(START, "get_age_node")
builder.add_edge("get_age_node", END)
graph = builder.compile(checkpointer=InMemorySaver())
config={"configurable":{"thread_id":"123"}}
result1=graph.invoke({
    "age": None
}, config=config)
print(result1["__interrupt__"])



result2=graph.invoke(Command(resume="20"), config)
print(result2["__interrupt__"])
# result3成功没有中断
result3=graph.invoke(Command(resume=20), config)
print(result3)