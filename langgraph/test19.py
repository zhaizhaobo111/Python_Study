"""时间旅行"""
from typing import TypedDict

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph


class State(TypedDict):
    topic:str
    joke:str
model=init_chat_model(
    model="qwen-turbo",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
)
def get_topic(state:State):
    topic=model.invoke("说一个笑话的主题，六个字以内")
    return {
        "topic":topic.content
    }

def get_joke(state:State):
    joke=model.invoke(f"说一个关于{state["topic"]}的笑话")
    return {
        "topic":joke.content
    }
builder=StateGraph(State)
builder.add_node(get_topic)
builder.add_node(get_joke)
builder.add_edge(START,"get_topic")
builder.add_edge("get_topic","get_joke")
builder.add_edge("get_joke",END)

graph=builder.compile(checkpointer=InMemorySaver())
config={"configurable":{"thread_id":"123"}}
"""时间旅行步骤"""
# 步骤一：初始执⾏⼯作流
print(graph.invoke({}, config))
# 步骤二：查看历史检查点
states=list(graph.get_state_history(config=config))
# print(states)
update=states[1]
# update.values是当前的 state
print(update.values["topic"])
print(update.config)
# 步骤三：修改状态（可选）
# update 包含：线程id、状态快照id
new_config=graph.update_state(update.config,values={"topic":"讲一个程序员笑话"})
# 步骤四：：从检查点恢复执⾏（重放）
print(graph.invoke(None, new_config))