from typing import Optional, List, TypedDict, Annotated

from langchain_community.chat_models import ChatTongyi
from pydantic import BaseModel, Field, SecretStr
# 结构化输出格式
model=ChatTongyi(model="qwen-max",api_key="sk-3b066661f42f49c9971861631950c710")

# 第一种  Pydantic 对象
# class Joke(BaseModel):
#     """给用户讲笑话"""
#     setup:str=Field(description="这是一个笑话的开头")
#     punchline:str=Field(description="这是一个笑话的笑点")
#     rating:Optional[int]=Field(default=None,description="从1到10分，给这个笑话打分")
#
# class Data(BaseModel):
#     """获取关于笑话的数据列表"""
#     Jokes:List[Joke]
#————————————————————————————————————————————————————————————————————————————————————————————————————————
# 第2种 TypedDict
class Joke(TypedDict):
    """给用户讲笑话"""
    setup:Annotated[str,...,"这是一个笑话的开头"]
    punchline:Annotated[str,...,"这是一个笑话的笑点"]
    # Optional[int] = 可填数字，也可以不填
    rating:Annotated[Optional[int],None,"从1到10分，给这个笑话打分"]

#————————————————————————————————————————————————————————————————————————————————————————————————————————
# JsonScheme
json_schema = {
    "title": "joke",
    "description": "给⽤⼾讲⼀个笑话。",
    "type": "object",
    "properties":
                {
    "setup": {
    "type": "string",
    "description": "这个笑话的开头",
    },
    "punchline": {
    "type": "string",
    "description": "这个笑话的妙语",
    },
    "rating": {
    "type": "integer",
    "description": "从1到10分，给这个笑话评分",
    "default": None,
                    },
                    },
    "required": ["setup", "punchline"],
    }
model_with_structed=model.with_structured_output(json_schema)
# model_with_structed=model.with_structured_output(Joke,include_raw=True)
print(model_with_structed.invoke("请讲一个关于唱歌的笑话"))

# print(model.invoke("请分别讲一个关于唱歌跳舞的笑话").content)