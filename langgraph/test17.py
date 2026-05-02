from langchain.chat_models import init_chat_model
from langchain_core.messages import tool, SystemMessage, ToolMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import MessagesState, StateGraph
from langgraph.types import interrupt, Command


@tool
def send_mail(to:str,subject:str,body:str):
    """发送邮件给收件人"""
    result=interrupt({
        "action":"发送邮件",
        "to":"to",
        "subject":"subject",
        "body":"body",
        "message":"同意发送这封邮件吗",
    })
    # return "同意"/"不同意"
    if result.get("action")=="同意":
        final_to=result.get("to",to)
        final_subject=result.get("subject",subject)
        final_body=result.get("body",body)
        final_email=f"收件人:{final_to}，主题：{final_subject}，正文：{final_body}"
        print(f"发送邮件{final_email}")
        return final_email
    return "用户取消发送"

# model_with_tool=init_chat_model(
#     model="qwen-turbo",
#     model_provider="openai",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     api_key="sk-3b066661f42f49c9971861631950c710",
#     temperature=0)
# ).bind_tools([])
model_with_tool = ChatOpenAI(
    model="qwen-turbo",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0
).bind_tools([send_mail])

def llm_call(state:MessagesState):
    """LLM决定是否调用工具"""
    messages=model_with_tool.invoke(
        [SystemMessage(content="你支持的调用工具进行邮件发送")]

    )+state["messages"]
    if messages.tool_calls:
        tool_call=messages.tool_calls[0]
        tool_result=send_mail.invoke(tool_call["args"])
        return {
            "messages":[ToolMessage(content=tool_result,tool_call_id=tool_call["id"])]
        }
    return {
        "messages":messages
    }
builder = StateGraph(MessagesState)
builder.add_node("llm_call", llm_call)
builder.add_edge(START, "llm_call")
builder.add_edge("llm_call", END)
graph = builder.compile(checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "email-workflow"}}
initial = graph.invoke(
    {"messages": [HumanMessage(content="发送电⼦邮件⾄alice@example.com，主题是：请假，内容是：理由如下...")]},
    config=config
)
print(initial["__interrupt__"]) # -> [Interrupt(value={'action': '...', ...})]
# ⽤批准和可选编辑的参数恢复
resumed = graph.invoke(
# Command(resume={"action": "同意", "subject": "病假"}),
Command(resume={"action": "不同意"}),config=config,)
print(resumed["messages"][-1]) #