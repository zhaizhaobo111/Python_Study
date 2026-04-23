"""并行化模式"""
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph


class AnalysisState(TypedDict):
    concept: str # 概念
    market: str # 市场分析
    competitor: str # 竞品分析
    tech: str # 技术分析
    report: str # 汇总报告

def market_task(state: AnalysisState):
    """市场分析"""
    return {"market": "⽤⼾关注续航、重量、防盗，对骑⾏社交有兴趣..."}
def competitor_task(state: AnalysisState):
    """竞品分析"""
    return {"competitor": "传统品牌智能化不⾜，互联⽹品牌续航和售后差..."}
def tech_task(state: AnalysisState):
    """技术分析"""
    return {"tech": "轻量化电池⻋⾝、GPS防盗、社交App集成..."}
# 汇总结果
def combine_results(state: AnalysisState):
    """⽣成最终报告"""
    report = f"产品分析报告\n\n"
    report += f"市场分析：\n{state['market']}\n\n"
    report += f"竞品分析：\n{state['competitor']}\n\n"
    report += f"技术分析：\n{state['tech']}\n\n"
    report += "建议：聚焦续航、防盗、社交功能的平衡发展"
    return {"report": report}
# 创建图 添加节点、边
builder=StateGraph(AnalysisState)
builder.add_node(market_task)
builder.add_node(competitor_task)
builder.add_node(tech_task)
builder.add_node(combine_results)

builder.add_edge(START,"market_task")
builder.add_edge(START,"competitor_task")
builder.add_edge(START,"tech_task")

builder.add_edge("market_task","combine_results")
builder.add_edge("competitor_task","combine_results")
builder.add_edge("tech_task","combine_results")
builder.add_edge("combine_results",END)

workflows=builder.compile()
result = workflows.invoke({"combine_results": "城市通勤智能电动⾃⾏⻋"})
print(result["report"])

