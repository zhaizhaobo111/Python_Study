from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

# 定义模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 定义提示词模板 Runnable实例
# 文本提示词模板
# 方式1
# PromptTemplate(
#     template="介绍{city的历史}",
#     input_variables=["city"],
# )
# 方式2
# prompt_template=PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")
# # 调用 实例化模板
# print(prompt_template.invoke({"language_from": "中文", "language_to": "英文"}))

#————————————————————————————————————————————————————————————————————————————————————————————————————————
# 定义消息提示词模板
# 实例化
# chat_prompt_template=ChatPromptTemplate(
#     [
#         ("system","将文本从{language_from}翻译为{language_to}"),
#         ("user","{text}"),
#
#     ]
# )
# chat_prompt_template=ChatPromptTemplate(
#     [
#         ("system","将文本从{language_from}翻译为{language_to}"),
#         ("user","{text}"),
#
#     ]
# )
# messages=(chat_prompt_template.invoke({
#     "language_from": "中文",
#     "language_to": "英文",
#     "text": "你是谁？"
# }))

# message 调用
# model.invoke(messages).pretty_print()
#————————————————————————————————————————————————————————————————————————————————————————————————————————
# chain调用
# chain=chat_prompt_template | model
# chain.invoke({
#     "language_from": "中文",
#     "language_to": "英文",
#     "text": "你是谁？"
# }).pretty_print()


#————————————————————————————————————————————————————————————————————————————————————————————————————————

chat_prompt_template=ChatPromptTemplate(
    [
        ("system","将文本从{language_from}翻译为{language_to}"),
        MessagesPlaceholder("msgs"),
        ("user","{text}"),
    ]
)
#占位符
messages_placeholder=[
    HumanMessage(content="你是谁"),
    AIMessage(content="Who are you?")
]


chain=chat_prompt_template | model
chain.invoke({
    "language_from": "中文",
    "language_to": "英文",
    "text": "你在干什么？",
    "msgs":messages_placeholder
}).pretty_print()

