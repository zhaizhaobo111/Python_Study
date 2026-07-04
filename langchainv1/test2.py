from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langchain.tools import tool,ToolRuntime



SYSTEM_PROMPT = """你是⼀位擅⻓⽤双关语表达的天⽓预报专家。
你拥有以下两种⼯具的使⽤权：
- get_weather_for_location：使⽤此功能可获取特定地点的天⽓情况
- get_user_location：使⽤此功能可获取⽤⼾的当前位置
如果⽤⼾向您询问天⽓情况，请务必先确认其所在位置。如果从问题中不能推断出他们指的是其所在的
具体地点，那么请使⽤“get_user_location”⼯具来获取他们的位置信息。"""
# 定义上下文
@dataclass
class Context:
    """自定义运行时上下文schema"""
    user_id:str

# 定义响应格式
@dataclass
class ResponseFormat:
    """agent 的响应模式。"""
    # ⼀个诙谐的回答（这是必须的）
    punny_response: str
    # 如果有关于天⽓的任何有趣的信息的话
    weather_conditions: str | None = None

# 定义工具
@tool
def get_weather(city:str)->str:
    return f"{city}总是天气晴朗"
"""
通过用户id将调用用户信息存储到store中，用户查询时通过id在store中查询
获取store、userid（运行时上下文中）
"""
@tool
def get_location(runtime:ToolRuntime[Context])->str:
    user_id=runtime.context.user_id
    memory_store=runtime.store
    memory_store.put(("users",),user_id,value={"name":f"name_{user_id}"})
    user_info=memory_store.get(("users",),user_id)
    print(user_info)
    return "北京"if user_id=="1" else "上海"
model=init_chat_model("",temperature=1)
agent=create_agent(
    model="",
    name="",
    system_prompt="",
    tools=[get_weather,get_location],        # 工具1：根据位置获取天气
                     # 工具2：工具用户id获取用户信息
    context_schema=Context,
    response_format=ResponseFormat,
    checkpointer=InMemorySaver(),
    store=InMemoryStore(),
)
config={"configurable":{"thread_id":"111"}}
res=agent.invoke({
    "messages":[{"role":"user","content":"我这里天气怎么样"}]},
    context=Context(user_id="1"),
    config=config,
)
print(res)
# 获取格式化结果
# print(res["structured_response"])
