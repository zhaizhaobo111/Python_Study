# """路由模式"""
# from typing import TypedDict, Literal
#
# from langchain.chat_models import init_chat_model
# from langchain_core.messages import HumanMessage
# from langgraph.constants import START, END
# from langgraph.graph import StateGraph
# from pydantic import BaseModel, Field
#
#
# class State(TypedDict):
#     # 用户输入
#     input:str
#     # 路由决策
#     decision:str
#     # 用户输出
#     output:str
# class Route(BaseModel):
#     step:Literal["pre_sale", "after_sale", "technical"]=Field(
#         description="根据⽤⼾问题类型决定路由到售前、售后还是技术处理"
#     )
# def model_call_router(state: State):
#     """分析⽤⼾输⼊，决定问题类型"""
#     model=init_chat_model(
#     model="qwen-plus",
#     model_provider="openai",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     api_key="sk-3b066661f42f49c9971861631950c710",
#     temperature=0
#     )
#     decision=model.with_structured_output(Route).invoke(
#         [
#             HumanMessage(content=state["input"])
#         ]
#     )
#     return {
#         "decision":decision.step
#     }
# # 三个不同的处理节点
# def pre_sale_handler(state: State):
#     """处理售前咨询"""
#     return {
#         "output": "售前咨询已处理，处理内容....."
#     }
# def after_sale_handler(state: State):
#     """处理售后问题"""
#     return {"output": "售后问题已处理，处理内容....."}
# def technical_handler(state: State):
#     """处理技术问题"""
#     return {"output": "技术问题已处理，处理内容....."}
# builder=StateGraph(State)
# builder.add_node(model_call_router)
# builder.add_node(pre_sale_handler)
# builder.add_node(after_sale_handler)
# builder.add_node(technical_handler)
# builder.add_edge(START,"model_call_router")
#
# def route_decision(state: State):
#     if state["decision"] == "pre_sale":
#         return "pre_sale_handler" # 去售前处理节点
#     elif state["decision"] == "after_sale":
#         return "after_sale_handler" # 去售后处理节点
#     elif state["decision"] == "technical":
#         return "technical_handler" # 去技术处理节点
#
# builder.add_conditional_edges(
#     "model_call_router",
#     route_decision,
#     ["pre_sale_handler","after_sale_handler","technical_handler"]
# )
# builder.add_edge("pre_sale_handler",END)
# builder.add_edge("after_sale_handler",END)
# builder.add_edge("technical_handler",END)
#
# workflows=builder.compile()
# test_cases = [
#     "我想了解⼀下你们产品的价格和功能", # 售前咨询
#
#     "我购买的产品有质量问题，需要退货", # 售后问题
#     "这个软件安装后⽆法正常运⾏，报错代码0x80070005", # 技术问题
#     "请问你们的售后服务政策是什么", # 售前咨询
#     "我的订单已经发货但还没收到", # 售后问题
#     "如何配置数据库连接参数" # 技术问题
# ]
# # for test_case in test_cases:
# #     print("*" * 50)
# #     result = workflows.invoke({"input": test_case})
# #     print(f"⽤⼾问题：{test_case}\n{result['output']}")
#
# with open("../Docs/pdf/graph3.png", "wb") as f:
#     f.write(workflows.get_graph().draw_mermaid_png())


from typing import TypedDict, Literal

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from pydantic import BaseModel, Field


class State(TypedDict):
    # 用户输入
    input: str
    # 路由决策
    decision: str
    # 用户输出
    output: str

class Route(BaseModel):
    step: Literal["pre_sale", "after_sale", "technical"] = Field(
        description="根据⽤⼾问题类型决定路由到售前、售后还是技术处理"
    )

def model_call_router(state: State):
    """分析⽤⼾输⼊，决定问题类型"""
    model = init_chat_model(
        model="qwen-plus",
        model_provider="openai",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key="sk-3b066661f42f49c9971861631950c710",
        temperature=0
    )
    # 修复：避免JSON解析报错，简化调用逻辑（适配qwen-plus）
    prompt = f"""用户问题：{state['input']}
仅返回关键词（pre_sale/after_sale/technical），不输出任何多余内容"""
    decision = model.invoke([HumanMessage(content=prompt)]).content.strip()
    return {
        "decision": decision
    }

# 三个不同的处理节点
def pre_sale_handler(state: State):
    """处理售前咨询"""
    return {
        "output": "售前咨询已处理，处理内容....."
    }

def after_sale_handler(state: State):
    """处理售后问题"""
    return {"output": "售后问题已处理，处理内容....."}

def technical_handler(state: State):
    """处理技术问题"""
    return {"output": "技术问题已处理，处理内容....."}

builder = StateGraph(State)
# 修复：必须指定字符串节点名（关键错误，导致流程图生成失败）
builder.add_node("model_call_router", model_call_router)
builder.add_node("pre_sale_handler", pre_sale_handler)
builder.add_node("after_sale_handler", after_sale_handler)
builder.add_node("technical_handler", technical_handler)

builder.add_edge(START, "model_call_router")

def route_decision(state: State):
    if state["decision"] == "pre_sale":
        return "pre_sale_handler"  # 去售前处理节点
    elif state["decision"] == "after_sale":
        return "after_sale_handler"  # 去售后处理节点
    elif state["decision"] == "technical":
        return "technical_handler"  # 去技术处理节点

builder.add_conditional_edges(
    "model_call_router",
    route_decision,
    ["pre_sale_handler", "after_sale_handler", "technical_handler"]
)

builder.add_edge("pre_sale_handler", END)
builder.add_edge("after_sale_handler", END)
builder.add_edge("technical_handler", END)

workflows = builder.compile()

# 测试用例（可选，注释可保留）
test_cases = [
    "我想了解⼀下你们产品的价格和功能",  # 售前咨询
    "我购买的产品有质量问题，需要退货",  # 售后问题
    "这个软件安装后⽆法正常运⾏，报错代码0x80070005",  # 技术问题
    "请问你们的售后服务政策是什么",  # 售前咨询
    "我的订单已经发货但还没收到",  # 售后问题
    "如何配置数据库连接参数"  # 技术问题
]
# for test_case in test_cases:
#     print("*" * 50)
#     result = workflows.invoke({"input": test_case})
#     print(f"⽤⼾问题：{test_case}\n{result['output']}")

# 关键：生成流程图到指定路径 ../Docs/pdf/graph3.png
# 注意：确保 ../Docs/pdf 文件夹已创建（若未创建，会报错“找不到路径”）
try:
    with open("../Docs/pdf/graph3.png", "wb") as f:
        f.write(workflows.get_graph().draw_mermaid_png())
    print("流程图生成成功！路径：../Docs/pdf/graph3.png")
except Exception as e:
    print(f"流程图生成失败，原因：{str(e)}")
    print("提示：请先创建 Docs/pdf 文件夹（上级目录下），再重新运行")

