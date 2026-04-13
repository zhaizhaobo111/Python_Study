from typing import Optional, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import tool_example_to_messages
from openai import BaseModel
from pydantic import Field
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 第⼀步：定义结构化返回对象。
class Person(BaseModel):
    """⼀个⼈的信息。"""
    name: Optional[str] = Field(default=None, description="这个⼈的名字")
    hair_color: Optional[str] = Field(default=None, description="如果知道这个⼈头发的颜⾊")
    skin_color: Optional[str] = Field(default=None, description="如果知道这个⼈的肤⾊")
    height_in_meters: Optional[str] = Field(default=None, description="以⽶为单位的⾼度")

class Data(BaseModel):

    """提取关于⼈的数据。"""

    people: List[Person]=Field(description="人员列表")
# 第⼆步：定义两个关键⽰例，每个⽰例中包含【⽂本】和【希望输出】
examples = [
(
    "海洋是⼴阔⽽蓝⾊的。它有两万多英尺深。",
    Data(people=[]), # 没有⼈物信息的情况
),
(
    "⼩强从中国远⾏到美国。",
    Data(people=[
    Person(name="⼩强", height_in_meters=None, skin_color=None,hair_color=None),
    ]), # 部分信息缺失的情况
),
]
# 第三步：定义提⽰词模板。
prompt_template=ChatPromptTemplate(
    [
    SystemMessage(content="你是⼀个提取信息的专家，只从⽂本中提取相关信息。如果您不知道要提取的属性的值，属性值返回null"),

    MessagesPlaceholder("example_messages"),
    ("user", "{new_message}"),
    ]

)
# 第四步：构造请求的消息列表。处理逻辑：
# 样例消息列表
examples_messages=[]
# 遍历⽰例对，将每个⽰例构造消息
for txt,tool_call, in examples:
    # 根据提取结果⽣成AI响应⽂本
    if tool_call.people:
        ai_response = "检测到⼈"
    else:
        ai_response = "未检测到⼈"
    # 将⽰例转换为模型可理解的消息格式
    examples_messages.extend(tool_example_to_messages(
        txt,
        [tool_call],
        ai_response=ai_response,
    )
    )


with_structured_model=model.with_structured_output(schema=Data)
chain=prompt_template| with_structured_model
print(chain.invoke({
    "example_messages": examples_messages,
    "new_message": "篮球场上，⾝⾼两⽶的中锋王伟默契地将球传给⼀⽶七的后卫挚友李明，完成⼀记绝杀。"
                   "这对⽼友⽤⼗年配合弥补了⾝⾼的差距。"
}))
