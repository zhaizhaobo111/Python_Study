"""流式输出token"""
"""按 Tags 过滤 Tokens"""
from typing import TypedDict
from langgraph.graph import StateGraph, START
from langchain_openai import ChatOpenAI
# 初始化带标签的模型
joke_model = ChatOpenAI(
    model="qwen-turbo",
    # model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0,
    model_kwargs={"tags": ["joke"]} # 给模型添加标签
)
poem_model = ChatOpenAI(
model="gpt-4o-mini",
model_kwargs={"tags": ["poem"]} # 给模型添加标签
)
class CreativeState(TypedDict):
    topic: str
    joke: str
    poem: str
def generate_creative_content(state: CreativeState):
    """同时⽣成笑话和诗歌"""
    topic = state["topic"]
    # ⽣成笑话
    print(f"\n⽣成关于 {topic} 的笑话：")
    joke_response = joke_model.invoke([
    {"role": "user", "content": f"讲⼀个关于 {topic} 的笑话"}
    ])
    # ⽣成诗歌
    print(f"\n⽣成关于 {topic} 的诗歌：")
    poem_response = poem_model.invoke([
    {"role": "user", "content": f"写⼀⾸关于 {topic} 的短诗"}
    ])
    return {
        "joke": joke_response.content,
        "poem": poem_response.content
    }
# 构建图
builder = StateGraph(CreativeState)
builder.add_node("creative", generate_creative_content)
builder.add_edge(START, "creative")
graph = builder.compile()
# 流式输出并过滤
for token_chunk, metadata in graph.stream(
    {"topic": "猫"},
    stream_mode="messages"
    ):
        # 只输出笑话相关的 Tokens
        tags = metadata.get("tags", [])