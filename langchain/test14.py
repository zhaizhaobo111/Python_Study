# 测试langsmith
import os

os.environ["LANGSMITH_API_KEY"] = "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"
os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

from langchain_community.chat_models import ChatTongyi

model = ChatTongyi(
    model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")

res = model.invoke("111111")
print(res)