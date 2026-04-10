from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
# TavilySearch 搜索工具

# 定义模型
model=ChatOpenAI(model="deepseek",api_key="sk-235d98ccf7e14ab99ceef754a2e3438d",base_url="https://api.deepseek.com/v1")
# model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
#定义工具
tool=TavilySearch(max_results=4)
# 绑定工具
model_with_tools=model.bind_tools([tool])
#定义消息列表
messages=[
    HumanMessage("烟台的天气怎么样")
]
# 定义aimessage
ai_message=model_with_tools.invoke(messages)
messages.append(ai_message)
#定义toolmessage
for tool_call in ai_message.tool_calls:
    tool_message=tool.invoke(tool_call)
    messages.append(tool_message)

print(model.invoke(messages).content)
