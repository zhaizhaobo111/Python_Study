from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# res=model.invoke("你是谁")
# print(res.content)
# 初始化 LLM 实例（以 OpenAI 模型为例）
model =ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
res=model.invoke("你好，讲一个简短的冷笑话")
print(res)
# ??????
# 调用模型，输出文本
parser=StrOutputParser()
chain=model|parser
print(chain.invoke("你好，讲一个简短的冷笑话"))
