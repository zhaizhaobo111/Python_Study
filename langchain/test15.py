from langchain_community.chat_models import ChatTongyi
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
# 定义⼤模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
store = {}
# 接受⼀个 session_id 并返回⼀个消息历史对象。
# 这个 session_id ⽤于区分不同的对话，并应作为配置的⼀部分在调⽤新链时传⼊
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
#InMemoryChatMessageHistory() 将消息存储在内存列表中。
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
# 包装model，管理聊天消息历史记录
with_message_history = RunnableWithMessageHistory(model, get_session_history)
config = {"configurable": {"session_id": "1"}}

with_message_history.invoke([HumanMessage(content="Hi! I'm Bob")],config=config,
).pretty_print()

with_message_history.invoke([HumanMessage(content="What's my name?")],config=config,
).pretty_print()