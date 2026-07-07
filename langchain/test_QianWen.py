from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# #  1.定义qianwenAi模型
# model=ChatTongyi(model="deepseek-v4-flash",api_key="sk-3b066661f42f49c9971861631950c710")
# #  2.定义消息
# # 用户消息 HumanMessage
# # 系统提示消息 SystemMessage
# messages=[
#     SystemMessage(content="请帮我进行翻译，由英文翻译成中文"),
#     HumanMessage(content="hi")
# ]
# # 3.调用大模型
# # result=model.invoke(messages)
# # print(result)
# # 4.定义输出解析器
# parser=StrOutputParser()
# # print(parser.invoke(result))
# # 5.定义langchain
# chain=model|parser
# print(chain.invoke(messages))

# 千问代理的deepseek的api key
apikey="sk-ws-H.EMHHLIR.r4SK.MEQCICP0sxwtzIWJbpRoR_xNnxfq33v2ybH-ZMHig5HtyhB0AiAgisKoZi4NUNGsSgKALzPplY7dAEqOea89YOG1uFwadg"
model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=apikey,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1" # 百炼兼容网关
)

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