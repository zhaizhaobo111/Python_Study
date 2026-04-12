from typing import Optional, List

from openai import BaseModel
from pydantic import Field


class Person(BaseModel):
    """⼀个⼈的信息。"""
    name: Optional[str] = Field(default=None, description="这个⼈的名字")
    hair_color: Optional[str] = Field(default=None, description="如果知道这个⼈头发的颜⾊")
    skin_color: Optional[str] = Field(default=None, description="如果知道这个⼈的肤⾊")
    height_in_meters: Optional[str] = Field(default=None, description="以⽶为单位的⾼度")

class Data(BaseModel):

    """提取关于⼈的数据。"""

    people: List[Person]