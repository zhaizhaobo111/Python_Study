from langchain_community.chat_models import ChatTongyi
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage,trim_messages
# 定义⼤模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 历史消息记录
messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
    HumanMessage(content="What's my name?"),
]
# 使⽤ trim_messages 减少发送给模型的消息数量
#第一种方式：token_counter以model 基于 token 的修剪，
# trimmer = trim_messages(
#         max_tokens=65, # 修剪消息的最⼤令牌数，根据你想要的谈话⻓度来调整
#         strategy="last", # 修剪策略：
#         # “last”（默认）：保留最后的消息。
#         # “first”：保留最早的消息。
#         token_counter=model, # 传⼊⼀个函数或⼀个语⾔模型（因为语⾔模型有消息令牌计数⽅法）
#         include_system=True, # 如果想始终保留初始系统消息，可以指定include_system=True
#         allow_partial=False, # 是否允许拆分消息的内容
#         start_on="human", # 如果需要确保我们的第⼀条消息（不包括系统消息）始终是特定类型，可以指定 start_on
# )
#第二种方式 token_counter以len 基于 消息数 的修剪，
trimmer = trim_messages(
        max_tokens=11, # 修剪消息的最⼤令牌数，根据你想要的谈话⻓度来调整
        strategy="last", # 修剪策略：
        # “last”（默认）：保留最后的消息。
        # “first”：保留最早的消息。
        token_counter=len, # 传⼊⼀个函数或⼀个语⾔模型（因为语⾔模型有消息令牌计数⽅法）
        include_system=True, # 如果想始终保留初始系统消息，可以指定include_system=True
        allow_partial=False, # 是否允许拆分消息的内容
        start_on="human", # 如果需要确保我们的第⼀条消息（不包括系统消息）始终是特定类型，可以指定 start_on
)

chain = trimmer | model
print(chain.invoke(messages))