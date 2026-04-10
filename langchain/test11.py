# 聊天模型流式传输stream
import asyncio

from langchain_community.chat_models import ChatTongyi

model=ChatTongyi(model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")
# 同步 stream方法
# 返回一个迭代器，产生的消息块
# chunks=[]
# for chunk in model.stream("请将一个故事，30字"):
#     chunks.append(chunk)
#     print(chunk.content,end="|",flush=True)


# 异步 stream方法
async def async_stream():
    print("异步调用")
    async for chunk in model.astream("请将一个故事，30字"):
        print(chunk.content,end="|",flush=True)
asyncio.run(async_stream())