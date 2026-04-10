from typing import Optional, List, Annotated, Union

from langchain_community.chat_models import ChatTongyi
from pydantic import BaseModel, Field

#————————————————————————————————————————————————————————————————————————————————————————————————————————
model=ChatTongyi(model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")

# 第一种  Pydantic 对象
class Joke(BaseModel):
    """给用户讲笑话"""
    setup:str=Field(description="这是一个笑话的开头")
    punchline:str=Field(description="这是一个笑话的笑点")
    rating:Optional[int]=Field(default=None,description="从1到10分，给这个笑话打分")

class Respense(BaseModel):
    """ 以对话的方式回应"""
    content:str=Field(description="用于对用户查询的会话响应")
    # content: Annotated[str,"用于对用户查询的会话响应"]
class Final_Response(BaseModel):

    """最终回复，选择合适的输出结果"""
    final_output:Union[Joke,Respense]

model_with_structed=model.with_structured_output(Final_Response)
# model_with_structed=model.with_structured_output(Joke,include_raw=True)
print(model_with_structed.invoke("请讲一个关于唱歌的笑话"))
print(model_with_structed.invoke("你是谁"))