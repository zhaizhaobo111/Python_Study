from typing import TypedDict, Optional, Literal

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command

'''保存审批状态，有条件便觉得后续流程'''
# class ApprovalState(TypedDict):
#     action_details: str # 操作详情（如"转账30000元"）
#     status: Optional[Literal["等待", "批准", "拒绝"]] # 审批状态
#
# def approval_node(state:ApprovalState):
#     decision=interrupt({
#         "question":f"是否批准此操作",
#         "details":state["action_details"],
#         "options":"请输入 批准 或 拒绝",
#     })
#     return {
#         "status":decision
#     }
#
# def proceed_node(state:ApprovalState):
#     print("")
#     return {
#
#     }
# def cancel_node(state:ApprovalState):
#     print("")
#     return {
#
#     }
#
# builder = StateGraph(ApprovalState)
# builder.add_node("approval", approval_node)
# builder.add_node("proceed", proceed_node)
# builder.add_node("cancel", cancel_node)
# builder.add_edge(START, "approval")
# def approval_node(state:ApprovalState):
#     if state["status"]=="批准":
#         next_node="proceed"
#     else:
#         next_node = "cancel"
#     return next_node
# builder.add_conditional_edges(
#     "approval",
#     approval_node,
#     ["proceed","cancel"]
# )
# # builder.add_edge("proceed", END)
# # builder.add_edge("cancel", END)
# config={"configurable":{"thread_id":123}}
# graph = builder.compile(checkpointer=InMemorySaver())
#
# result1=graph.invoke({"action_details": "转账3000"},config)
# print(result1)
# print(result1["__interrupt__"][0].value)
# result2=graph.invoke(Command(resume="批准"),config=config)
# print(result2)

# --------------------------------------------------------------------------
"""节点中，直接判断后续执行流程"""
class ApprovalState(TypedDict):
    action_details: str # 操作详情（如"转账30000元"）
    status: Optional[Literal["等待", "批准", "拒绝"]] # 审批状态

def approval_node(state:ApprovalState):
    decision= interrupt({
        "question":f"是否批准此操作",
        "details":state["action_details"],
        "options":"请输入 批准 或 拒绝",
    })
    if decision=="批准":
        next_node="proceed"
    else:
        next_node="cancel"
    return Command(goto=next_node)

def proceed_node(state:ApprovalState):
    print("批准")
    return {
        "status":"批准"
    }
def cancel_node(state:ApprovalState):
    print("取消")
    return {
        "status":"取消"
    }

builder = StateGraph(ApprovalState)
builder.add_node("approval", approval_node)
builder.add_node("proceed", proceed_node)
builder.add_node("cancel", cancel_node)
builder.add_edge(START, "approval")
builder.add_edge("proceed", END)
builder.add_edge("cancel", END)
config={"configurable":{"thread_id":123}}
graph = builder.compile(checkpointer=InMemorySaver())

result1=graph.invoke({"action_details": "转账3000"},config)
print(result1)
print(result1["__interrupt__"][0].value)
result2=graph.invoke(Command(resume="批准"),config=config)
print(result2)
