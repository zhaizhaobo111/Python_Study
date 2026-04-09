# 使用工具structured Tool
# 方式1
from typing import Tuple

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


#
# def my_add(a:int,b:int)->int:
#         # 文档字符串
#         """ 两数相加  """
#         return a+b
# result=StructuredTool.from_function(func=my_add)  #函数名直接传给工具，不加（）
# print(result.invoke({"a": 10, "b": 20}))

#————————————————————————————————————————————————————————————————————————————————————————————————————————
# 方法二

# class AddInput(BaseModel):
#     a:int=Field(...,description="这是第一个参数")
#     b:int=Field(...,description="这是第二个参数")
# def my_add(a:int,b:int)->int:
#
#         return a+b
# result=StructuredTool.from_function(func=my_add,
#                                     name="ADD",
#                                     description="两数相加",
#                                     args_schema=AddInput)
# print(result.invoke({"a": 10, "b": 20}))
# print(f"工具名为：{result.name}")
# print(f"工具描述为：{result.description}")
# print(f"工具参数为：{result.args}")
#————————————————————————————————————————————————————————————————————————————————————————————————————————
# 方式三

class AddInput(BaseModel):
    a:int=Field(...,description="这是第一个参数")
    b:int=Field(...,description="这是第二个参数")
def my_add(a:int,b:int)->Tuple[str,list[int]]:
        nums=[a,b]
        content=f"{nums}两数相加结果是：{a+b}"

        return content,nums
result=StructuredTool.from_function(func=my_add,
                                    name="ADD",
                                    description="两数相加",
                                    args_schema=AddInput,
                                    response_format="content_and_artifact")  #工具结果
# 输出要改成大模型的方式
print(result.invoke({
    "name": "ADD",
    "args": {"a": 10, "b": 20},
    "type": "tool_call",  #必填，类型
    "id": "1111"  #必填，id号
}))
# print(result.invoke({"a": 10, "b": 20}))
print(f"工具名为：{result.name}")
print(f"工具描述为：{result.description}")
print(f"工具参数为：{result.args}")