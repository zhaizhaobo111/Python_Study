# 定义输出结构：Pydantic 类
from typing import Optional

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import PydanticOutputParser,  JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
class Joke(BaseModel):
    """给⽤⼾讲⼀个笑话。"""
    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(
    default=None, description="从1到10分，给这个笑话评分"
)
#解析结构化对象输出
# parser=PydanticOutputParser(pydantic_object=Joke)
# 解析 JSON 输出
parser = JsonOutputParser(pydantic_object=Joke)
prompt_template = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    # partial_variables：提⽰模板携带的部分变量的字典，⽆需在每次调⽤提⽰时都传⼊它们。
    # 类型为 Mapping[str, Any]，传⼊template携带的部分变量的字典。
    partial_variables={"format_instructions":
    parser.get_format_instructions()},
    input_variables=["query"],
)
chain=prompt_template|model|parser
# print(chain.invoke({"query": "讲一个关于爱情的笑话"}))
for chunk in chain.stream({"query": "讲一个关于爱情的笑话"}):
    print(chunk, end="|")