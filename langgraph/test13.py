"""持久化三大应用：1记忆"""
from langchain.chat_models import init_chat_model
from langchain_core.messages import trim_messages, RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import MessagesState, StateGraph
"""修剪消息"""
# model=init_chat_model(
#     model="qwen-turbo",
#     model_provider="openai",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     api_key="sk-3b066661f42f49c9971861631950c710",
#     temperature=0
# )
# def call_node(state:MessagesState):
#     # 修建消息
#     messages=trim_messages(
#         state["messages"],
#         strategy="last",             #策略，保留最后的部分
#         token_counter=model,        #计算token数量
#         max_tokens=128,             #最大token数
#         start_on="human",           #从用户消息开始
#         end_on=("human","tool")     #结束于用户或工具消息
#     )
#     result=model.invoke(messages)
#     return {
#         "messages":[result]
#     }
#
# builder=StateGraph(MessagesState)
# builder.add_node(call_node)
# builder.add_edge(START,"call_node")
# builder.add_edge("call_node",END )
#
# graph=builder.compile(InMemorySaver())
# config={"configurable":{"thread_id":"123"}}
# graph.invoke({"messages": "hi, my name is bob"}, config)
# graph.invoke({"messages": "write a short poem about cats"}, config)
# graph.invoke({"messages": "now do the same but for dogs"}, config)
# final_response = graph.invoke({"messages": "what's my name?"}, config)
# final_response["messages"][-1].pretty_print()


# ------------------------------------------------------------------------------------------------
"""删除消息"""
model=init_chat_model(
    model="qwen-turbo",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
def call_node(state:MessagesState):
    # 修建消息
    messages=state["messages"]
    if len(messages)>6:
       return {
           "messages":[RemoveMessage(id=m.id)for m in messages[:6]]
       }
    result=model.invoke(messages)
    return {
        "messages":[result]
    }

builder=StateGraph(MessagesState)
builder.add_node(call_node)
builder.add_edge(START,"call_node")
builder.add_edge("call_node",END )

graph=builder.compile(InMemorySaver())
config={"configurable":{"thread_id":"123"}}
graph.invoke({"messages": "hi, my name is bob"}, config)
graph.invoke({"messages": "write a short poem about cats"}, config)
graph.invoke({"messages": "now do the same but for dogs"}, config)
final_response = graph.invoke({"messages": "what's my name?"}, config)
final_response["messages"][-1].pretty_print()