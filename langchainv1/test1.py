from langchain.agents import create_agent
from langchain.tools import tool
@tool
def get_weather(city:str)->str:
    return f"{city}总是天气晴朗"
agent=create_agent(
    model="",
    tools=[get_weather],
    system_prompt="你是一个乐于助人的助手",
)
res=agent.invoke({
    "messages":[{"role":"user",
                 "content":"北京天气怎么样？"
}]
})
print(res)
