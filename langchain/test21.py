from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
example_prompt=PromptTemplate.from_template("Question:{question}\n{answer}")
examples=[
{
        "question": "李⽩和杜甫，谁更⻓寿？",
        "answer": """
        是否需要后续问题：是的。
        后续问题：李⽩享年多少岁？
        中间答案：李⽩享年61岁。
        后续问题：杜甫享年多少岁？
        中间答案：杜甫享年58岁。
        所以最终答案是：李⽩
        """
},
{
        "question": "腾讯的创始⼈什么时候出⽣？",
        "answer": """
        是否需要后续问题：是的。
        后续问题：腾讯的创始⼈是谁？
        中间答案：腾讯由⻢化腾创⽴。
        后续问题：⻢化腾什么时候出⽣？
        中间答案：⻢化腾出⽣于1971年10⽉29⽇。
        所以最终答案是：1971年10⽉29⽇
        """,
},
{
        "question": "孙中⼭的外祖⽗是谁？",
        "answer": """
        是否需要后续问题：是的。
        后续问题：孙中⼭的⺟亲是谁？
        中间答案：孙中⼭的⺟亲是杨太夫⼈。
        后续问题：杨太夫⼈的⽗亲是谁？
        中间答案：杨太夫⼈的⽗亲是杨胜辉。
        所以最终答案是：杨胜辉
        """,
},
{
        "question": "电影《红⾼粱》和《霸王别姬》的导演来⾃同⼀个国家吗？",
        "answer": """
        是否需要后续问题：是的。
        后续问题：《红⾼粱》的导演是谁？
        中间答案：《红⾼粱》的导演是张艺谋。
        后续问题：张艺来⾃哪⾥？
        中间答案：中国。
        后续问题：《霸王别姬》的导演是谁？
        中间答案：《霸王别姬》的导演是陈凯歌。
        后续问题：陈凯歌来⾃哪⾥？
        中间答案：中国。
        所以最终答案是：是
        """,
},
]
# 测试：实例化第⼀个⽰例
# print(example_prompt.invoke(examples[0]).to_string())

few_shot_prompt=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:{input}",   #suffix 表示在示例之后的模板字符串  prefix表示之前
    input_variables=["input"],   #input_variable 输入变量列表
)
chain=few_shot_prompt | model
chain.invoke({"input":"《教父》和《星球大战》的导演是否来自一个国家"}).pretty_print()