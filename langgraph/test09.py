# 定义状态
import operator
from typing import TypedDict, Annotated

from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
# 定义模型节点
model = init_chat_model("gpt-4o-mini", temperature=0)

def llm_call(state: dict):
    """LLM调⽤"""
    return {
    "messages": [
    model.invoke([SystemMessage(content="你是⼀个乐于助⼈的助⼿。")]
    + state["messages"])
]
}
# 构件图
builder = StateGraph(MessagesState)
builder.add_node("llm_call", llm_call)
builder.add_edge(START, "llm_call")
builder.add_edge("llm_call", END)
graph = builder.compile(checkpointer=InMemorySaver())