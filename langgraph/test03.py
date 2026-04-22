"""个智能的⽂档问答系统"""
from langchain_community.chat_models import ChatTongyi
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.messages import HumanMessage, filter_messages
from langchain_core.tools import create_retriever_tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.constants import START, END
from langgraph.graph import MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel, Field

# 第⼀步：准备"知识库"（数据加载与处理）
# 1.定义模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 2.定义嵌入模型
embeddings=OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
)
paths={
    "../Docs/makedown/新建 文本文档.md"
}
# 3. 加载所有 .md 文件
docs = [UnstructuredMarkdownLoader(path).load() for path in paths]
# 4. 把多层列表展平
docs_list = [item for sublist in docs for item in sublist]
# 5.定义文本分割器
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=1000,
    chunk_overlap=50
)
# 文档列表
doc_splits = text_splitter.split_documents(docs_list)
# 使⽤内存中向量存储和 OpenAI 嵌⼊
#  6. 存入内存向量库向量库
vectorstore = InMemoryVectorStore.from_documents(
    documents=doc_splits,
    embedding=embeddings
)


# 第⼆步：创建"检索⼯具"
# 创建检索器
retriever=vectorstore.as_retriever(search_kwargs={"k":2})
# 创建检索工具
retriever_tool=create_retriever_tool(
    retriever,
    "own_retrieve",
    "搜索并返回项目信息.",
)

# 第三步：设计"⼯作流程节点"

# 节点1：决策节点
# from langgraph.graph import MessagesState 提供了MessagesState
def generate_query_or_respond(state:MessagesState):
    """调⽤模型以基于当前状态⽣成响应。
    给定问题，它将决定使⽤检索⼯具检索，或者简单地响应⽤⼾。"""
    #  绑定工具
    result=model.bind_tools([retriever_tool]).invoke(state["messages"])
    return {
        "messages":[result]
    }
# 验证
# generate_query_or_respond({
#     "messages":[
#         {
#             "role":"user",
#             "content":"那些项目",
#         }
#     ]
# })["messages"][-1].pretty_print()
#  节点2：检索器⼯具节点
retriever_node=ToolNode([retriever_tool])
# 节点3：问题优化节点
REWRITE_PROMPT = (
    "查看输⼊并尝试推断潜在的语义意图/含义。\n"
    "这是最初的问题："
    "\n ------- \n"
    "{question}"
    "\n ------- \n"
    "提出⼀个改进后的问题："
)
def rewrite_question(state:MessagesState):
    """重写原始⽤⼾问题"""
    # 获取第一个消息 也就是HumanMessage
    question=state["messages"][0]
    # 将HumanMessage带入REWRITE_PROMPT 重写问题
    prompt=REWRITE_PROMPT.format(question=question)
    # result是写一个AImessage
    result=model.invoke([HumanMessage(content=prompt)])
    return {
        "messages":[HumanMessage(content=result.content)]
    }
# 节点4：答案⽣成节点
GENERATE_PROMPT = (
    "你是负责回答问题的助⼿。 "
    "使⽤以下检索到的上下⽂⽚段来回答问题。 "
    "如果你不知道答案，就说你不知道。 "
    "最多只⽤三句话，回答要简明扼要。\n"
    "Question: {question} \n"
    "Context: {context}"
)
def generate_answer(state:MessagesState):
    """⽣成答案"""
    # 答案是文本
    # 第一个问题 也是HumanMessage
    question=state["messages"][0].content
    # 最新的问题的检索结果
    context=state["messages"][-1].content
    prompt=GENERATE_PROMPT.format(question=question,context=context)
    result=model.invoke([HumanMessage(content=prompt)])
    return {
        "messages":[result]
    }
# 第四步：组装"⼯作流⽔线"
# 定义图
agent_builder=StateGraph(MessagesState)
# 添加点
agent_builder.add_node(generate_query_or_respond)
agent_builder.add_node("retrieve",retriever_node)
agent_builder.add_node(rewrite_question)
agent_builder.add_node(generate_answer)
# 添加普通边
agent_builder.add_edge(START,"generate_query_or_respond")

# 条件边1：LLM 决策是否需要进⾏知识库检索
agent_builder.add_conditional_edges(
    "generate_query_or_respond",
    # 判断最后一条AI消息是否包含工具调用
    tools_condition,
    {
        "tools":"retrieve",
        "__end__":END,
    }
)
# 条件边2：检测【检索到的⽂档】是否与【问题】相关
GRADE_PROMPT = (
    "你是⼀个评分员，评估检索到的⽂档与⽤⼾问题的相关性。 \n "
    "以下是检索到的⽂档： \n\n {context} \n\n"
    "以下是⽤⼾的问题： {question} \n"
    "如果⽂档包含与⽤⼾问题相关的关键字或语义，则将其评为相关。 \n"
    "给出⼀个⼆元分数“yes”或“no”，以表明该⽂档是否与问题相关。"
)
class GradeDocuments(BaseModel):
    score:str=Field(description="相关性评分：如果相关则为“yes”，如果不相关则为“no”")

def grade_documents(state:MessagesState):
    #问题+检索到的文档判断是否合格 (yes，no)
    #拿到最新的 HumanMessage（filter）
    user_messages=filter_messages(state["messages"],inclde_types="human")
    question=user_messages[-1].content
    context=state["messages"][-1].content
    # 获取提示词
    prompt=GRADE_PROMPT.format(question=question,context=context)
    result=model.with_structured_output(GradeDocuments).invoke(
        [HumanMessage(content=prompt)]
    )
    if result.score=="yes":
        return "generate_answer"
    else:
        return "rewrite_question"

agent_builder.add_conditional_edges(
    "retrieve",
    grade_documents,
    ["generate_answer","rewrite_question"]
)
agent_builder.add_edge("generate_answer",END)
agent_builder.add_edge("rewrite_question","generate_query_or_respond")
# 4.编译图
graph=agent_builder.compile()
# 5.执行图
# 流式输出
for chunk in graph.stream(
    {
        "messages":[HumanMessage(content="技术栈都有什么")]
    }
):
    print(chunk)