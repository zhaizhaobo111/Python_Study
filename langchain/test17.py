from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, filter_messages, merge_message_runs


model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 历史消息记录
messages = [
    SystemMessage("你是⼀个聊天助⼿", id="1"),
    HumanMessage("⽰例输⼊", id="2"),
    AIMessage("⽰例输出", id="3"),
    HumanMessage("真实输⼊", id="4"),
    AIMessage("真实输出", id="5"),
]
# 消息过滤
# print(filter_messages(messages, include_types="human"))
# print(filter_messages(messages, exclude_ids=["3"]))
# 消息合并
#第一种 调用
merge_messages= merge_message_runs(messages)
model.invoke(messages).pretty_print()


#第二种 chain调用
# merge_messages= merge_message_runs()
# chain= merge_messages | model
# chain.invoke(messages).pretty_print()