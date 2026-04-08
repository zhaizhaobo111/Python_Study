from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
#  1.定义qianwenAi模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
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