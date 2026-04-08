# 工具的使用
from langchain_core.tools import tool
# from pydantic import BaseModel, Field
from typing_extensions import Annotated


# 1.使⽤ @tool 装饰器创建⼯具
# @tool
# def my_add(a:int,b:int)->int:
#     # 文档字符串
#     """ 两数相加
#         Args:
#             a:第一个参数
#             b:第二个参数
#         """
#
#     return a+b

# 第二种
# class AddInput(BaseModel):
#     """
#     两数相加
#     """
#     a:int=Field(..., description="第一个整数")
#     b:int=Field(..., description="第二个整数")
# @tool(args_schema=AddInput)
# def my_add(a:int,b:int)->int:
#         # 文档字符串
#         """ 两数相加
#             Args:
#                 a:第一个参数
#                 b:第二个参数
#             """
#
#         return a+b

# 第三种：
@tool
def my_add(
        a:Annotated[int,...,"第一个整数"],
        b:Annotated[int,...,"第二个整数"])->int:
        # 文档字符串
        """ 两数相加
            Args:
                a:第一个参数
                b:第二个参数
            """

        return a+b
print(my_add.invoke({"a":10,"b":20}))
# 函数名、类型提⽰和⽂档字符串都是传递给⼯具 Schema 的⼀部分
#函数名、类型提⽰和⽂档字符串中获取相关属性，以此来声明⼀个⼯具，包括其名称、描述、输⼊参数、输出类型等等
print(my_add.name)#工具名称
print(my_add.description) #工具描述
print(my_add.args)#工具参数