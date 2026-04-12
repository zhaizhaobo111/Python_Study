#少样本提示词
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate,FewShotChatMessagePromptTemplate

model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 案例->参数
examples=[
    {"input":"hi,what is your name","output":"你叫什么名字？"},
    {"input":"hi,what is your age","output":"你多大了？"},
]
# 案例模板
examples_prompt_template=ChatPromptTemplate(
    [
        ("user","{input}"),
        ("ai","{output}"),
    ]
)
# 将案例转换为消息列表，插入到提示词把模板中去
# 少样本提示词
few_shot_prompt_template=FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=examples_prompt_template
)

# 最终提示词模板
chat_prompt_template=ChatPromptTemplate(
    [
        ("system","将文本从{language_from}翻译为{language_to}"),
        few_shot_prompt_template,
        ("user","{input}"),
    ]
)
chain=chat_prompt_template|model

chain.invoke({
    "language_from":"英文",
    "language_to":"中文",
    "input":"hi,what do you want to do?"
}).pretty_print()