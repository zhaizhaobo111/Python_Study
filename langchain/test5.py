from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

# from langchain_openai import ChatOpenAI
from typing_extensions import Annotated


@tool
def my_add(
        a:Annotated[int,...,"第一个整数"],
        b:Annotated[int,...,"第二个整数"])->int:
        # 文档字符串
        """ 两数相加 """

        return a+b

@tool
def my_multiple(
        a:Annotated[int,...,"第一个整数"],
        b:Annotated[int,...,"第二个整数"])->int:
        # 文档字符串
        """ 两数相乘 """

        return a*b


# 定义模型
model=ChatOllama(model="mistral")
# model=ChatOllama(model="deepseek-r1:8b")


# 绑定模型
tools=[my_add,my_multiple]
model_with_tools=model.bind_tools(tools=tools,tool_choice="any")  #tool_choice 强制无论在什么场景都要选择


# 创建消息列表,添加要传递给聊天模型的消息
messages=[
HumanMessage("2乘3等于多少？6加4等于多少？")
]

ai_messgaes=model_with_tools.invoke(messages)
print(ai_messgaes)
messages.append(ai_messgaes)


#构造ToolMessage，并添加消息列表进去
for too_call in ai_messgaes.tool_calls:
    selected_tool={"my_add":my_add,"my_multiple":my_multiple}[too_call["name"].lower()]
    tool_message=selected_tool.invoke(too_call)
    messages.append(tool_message)
print(messages)
print(model.invoke(messages).content)


# content='' additional_kwargs={} response_metadata={'model': 'mistral', 'created_at': '2026-04-09T04:04:36.0738545Z', 'done': True, 'done_reason': 'stop',
# 'total_duration': 15123755200, 'load_duration': 11694500, 'prompt_eval_count': 168, 'prompt_eval_duration': 121869500, 'eval_count': 109, 'eval_duration': 14923811300, 'logprobs': None, 'model_name': 'mistral', 'model_provider': 'ollama'}
# id='lc_run--019d7069-9554-7e31-9815-7c3088629dcd-0' tool_calls=[{'name': 'my_multiple', 'args': {'a': 2, 'b': 3}, 'id': '8525e917-d3a1-4f0f-b282-3d38c3bf006e', 'type': 'tool_call'}, {'name': 'my_add', 'args': {'a': 6, 'b': 4}, 'id': '8dd85470-dabe-441d-88da-79c4c85e95ad', 'type': 'tool_call'}]
# invalid_tool_calls=[] usage_metadata={'input_tokens': 168, 'output_tokens': 109, 'total_tokens': 277}
#  The result of the multiplication is 6 and the result of addition is 10.
# 调用工具
# print(model_with_tools.invoke("你是谁"))