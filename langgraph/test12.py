from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START
from langgraph.graph import MessagesState, StateGraph



model=init_chat_model(
    model="qwen-turbo",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
class State(MessagesState):
    summary:str
def call_model(state:State):
    summary=state.get("summary","")
    messages=model.invoke(
        [HumanMessage(content=summary)]+state["messages"]
    )
    return {
        "messages":messages
    }
def summarize(state:State):
    summary = state.get("summary", "")
    if summary:
        summary_messages=(
            f"这是到⽬前为⽌的对话摘要：{summary}\n\n"
            "基于上⾯的新消息扩展摘要："
        )
    else:summary_messages="创建上面的对话摘要"
    # 总结 消息列表+历史总结
    messages=state["messages"]+[HumanMessage(content=summary_messages)]
    result=model.invoke(messages)
    return {
        "summary":result.content,
        "messages":[RemoveMessage(id=m.id)for m in state["messages"][:-1]]
    }


checkpointer=InMemorySaver()
builder=StateGraph(State)
builder.add_node(summarize)
builder.add_node(call_model)

builder.add_edge(START,"call_model")
builder.add_edge("call_model", "summarize")
graph=builder.compile(checkpointer=checkpointer)

config={"configurable":{"thread_id":"111"}}
graph.invoke({"messages": "hi, my name is bob"}, config)
graph.invoke({"messages": "write a short poem about cats"}, config)
graph.invoke({"messages": "now do the same but for dogs"}, config)
final_response = graph.invoke({"messages": "what's my name?"}, config)
final_response["messages"][-1].pretty_print()
print("\nSummary:", final_response["summary"])
for i in final_response["messages"]:
    i.pretty_print()