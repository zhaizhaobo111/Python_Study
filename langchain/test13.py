from typing import Iterator, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

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
for chunk in chain.stream("请将一个故事，50字"):
    print(chunk,end="|",flush=True)