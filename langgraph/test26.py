from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="qwen-turbo",
    # model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
class State(TypedDict):
    query: str
    summary: str
    translation: str
def generate_summary(state: State):
    """⽣成摘要"""
    response = model.invoke([
    {"role": "user", "content": f"请为以下内容⽣成摘要：{state['query']}"}
    ])
    return {"summary": response.content}
def generate_translation(state: State):
    """⽣成翻译"""
    response = model.invoke([
    {"role": "user", "content": f"请将以下内容翻译成英⽂：{state['query']}"}
    ])
    return {"translation": response.content}
# 构建并⾏处理图
builder = StateGraph(State)
builder.add_node("summarize", generate_summary)
builder.add_node("translate", generate_translation)
builder.add_edge(START, "summarize")
builder.add_edge(START, "translate")
builder.add_edge("summarize", END)
builder.add_edge("translate", END)
graph = builder.compile()
# 流式输出并只显⽰某个节点的 Tokens
target_node = "summarize" # 可以改为 "translate"
for token_chunk, metadata in graph.stream(
    {"query": "⼈⼯智能是计算机科学的⼀个分⽀，致⼒于创造能够执⾏通常需要⼈类智能的任务的机器。"},
    stream_mode="messages"
):
    # 获取节点名称
    node_name = metadata.get("langgraph_node", "")
# 只输出⽬标节点的 Tokens
    if token_chunk.content and node_name == target_node:
        # 添加节点标签
        if node_name == "translate":
            prefix = " [翻译] "
        elif node_name == "summarize":
                prefix = " [摘要] "
    else:
        prefix = ""
    print(f"{prefix}{token_chunk.content}", end="", flush=True)