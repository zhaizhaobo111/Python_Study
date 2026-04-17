from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
#  1.定义openAi模型
model=ChatOpenAI(model="gpt-4o-mini",api_key="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")
#  2.定义消息
# 用户消息 HumanMessage
# 系统提示消息 SystemMessage
messages=[
    SystemMessage(content="请帮我进行翻译，由英文翻译成中文"),
    HumanMessage(content="hi")
]
# 3.调用大模型
# result=model.invoke(messages)
# print(result)
# 4.定义输出解析器
parser=StrOutputParser()
# print(parser.invoke(result))
# 5.定义langchain
chain=model|parser
print(chain.invoke(messages))
# model.invoke()

