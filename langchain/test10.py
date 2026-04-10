from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
# 与⼯具结合使⽤
# 定义模型
model=ChatTongyi(model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")
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

class SearchResult(BaseModel):
    """结构化搜索对象"""
    query:str=Field(description="搜索查询")
    findings:str=Field(description="查询结果摘要")
model_with_structured=model_with_tools.with_structured_output(SearchResult)
print(model_with_structured.invoke(messages))
