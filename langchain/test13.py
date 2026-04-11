from typing import Iterator, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
# import os
#
# os.environ["LANGSMITH_API_KEY"] = "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"
# os.environ["LANGSMITH_TRACING"] = "true"

#定义  模型
model=ChatTongyi(model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")
#定义  输出解析器
parser=StrOutputParser()

# 自定义生成器
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        while "。" in buffer:
            # 只要缓冲区中包含句号，就找到第⼀个句号的位置
            stop_index = buffer.index("。")
            # 将句号之前的内容（去除⾸尾空格）作为⼀个句⼦放⼊列表中并产出
            yield [buffer[:stop_index].strip()]
            # 更新缓冲区，保留句号之后的内容
            buffer = buffer[stop_index + 1:]
            yield [buffer.strip()]

chain=model|parser| split_into_list
for chunk in chain.stream("请写一首诗描述天气"):
    print(chunk,end="|",flush=True)