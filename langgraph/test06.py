"""协调者-⼯作者模式（Orchestrator-Workers）"""
import operator
from typing import TypedDict, Annotated, List

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.types import Send
from pydantic import BaseModel


#定义状态
class State(TypedDict):
    # 输入主题
    topic:str
    # 生成总计划（仓库）
    sections:list
    # 工作完成的结果
    completed_sections:Annotated[list,operator.add]
    # 汇总结果
    final_report:str
# 定义数据结构-结构化输出
# BaseModel 强制ai输出格式
class Section(BaseModel):
    name:str
    description:str

class Sections(BaseModel):
    # sections 模具
    sections:List[Section]
# 定义模型（结构化输出）
model=init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0)

planner=model.with_structured_output(Sections)
# 定义节点
# 定义协调器节点
def orchestrator(state: State):
    """协调者：分析任务并制定执⾏计划"""
    report_sections = planner.invoke([
        HumanMessage(content=f"为主题'{state['topic']}'制定报告⼤纲，包含3个章节")
    ])
    return {"sections": report_sections.sections}

# 定义工作节点
def work1(state: State):
    """⼯作者：根据分配的任务⽣成内容"""
    # section：具体的章节
    # state["section"] 就是通过 Send 对象传递过来的状态
    section=state["section"]
    result=model.invoke([
        HumanMessage(content=f"编写报告章节:{section.name},内容介绍：{section.description}")
    ])

    return {
        "completed_sections":[result.content]
    }
# 定义汇总节点
def synthesizer(state: State):
    """汇总所有⼯作者的成果"""
    completed_sections=state["completed_sections"]
    final_report="\n------\n".join(completed_sections)
    return {
        "final_report":final_report
    }

# 定义图
builder=StateGraph(State)
# 添加节点
builder.add_node(orchestrator)
builder.add_node(work1)
builder.add_node(synthesizer)
# 添加固定边
builder.add_edge(START,"orchestrator")
# 添加条件边
def assign_workers(state: State):
    """为每个任务创建⼯作者"""
    # 为每个章节创建⼀个⼯作者任务
    work_tasks=[]
    sections=state["sections"]
    for section in sections:
        work_tasks.append(
            Send("work1", {"section": section})#send 是一个对象： 参数1：节点 参数二：发送给节点的状态
        )
    return work_tasks #send
builder.add_conditional_edges(
    "orchestrator",
    assign_workers,
)
builder.add_edge("work1","synthesizer")
# 编译图
worker=builder.compile()
#
response =worker.invoke({"topic": "ai发展史"})
print(response)


