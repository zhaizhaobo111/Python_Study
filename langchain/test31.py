
"""
# 在线检索  检索——>——>——>
"""
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore

# 构建链：完成RAG能力
# 构建组件，构建链
# 嵌入模型
embeddings=OllamaEmbeddings(
    model="nomic-embed-text",
)
# 聊天模型
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
# 向量库
# 1.先从知识库中检索
# Redis配置
redis_url = "redis://192.168.100.238:6379"
config = RedisConfig(
        index_name="qa",
        redis_url=redis_url,
        metadata_schema=[
        {"name": "category", "type": "tag"},
        {"name": "num", "type": "numeric"},
],
)
# 向量库
vector_store=RedisVectorStore(
    embeddings=embeddings,
    config=config,
)
# 检索器
prompt=retriever=vector_store.as_retriever()
# 2.将检索结果+查询语句 构建为提示词（提示词模板） 发送给LLM
# 提示词模板
ChatPromptTemplate.from_messages(
    [
        "human",
        """你是负责回答问题的助手，使用以下检索到的上下文判断回答问题，如果你不知道答案就说不知道答案，最多回复三句话的结果，回答要简洁扼要
        Question:{question}
        Context:{context}
        Answer:"""

    ]
)
# 将检索到的文档转化成文本传递给提示词模板
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in  docs)
# 3.将消息发送给LLM（实例化消息，交出链完成）
# 定义链  执行question
# 检索器+format_docs question  (同时传递)
chain=(
        # 检索器+format_docs 分支1
        # question          分支2：RunnablePassthrough()在链中透传数据
    {"context": retriever|format_docs,"question" :RunnablePassthrough()}
    |prompt
    |model
    |StrOutputParser()
)
# 4.打印字符串结果（流式）
# 输出解析器
for chunk in chain.stream("介绍一下项目"):
    print(chunk,end="|",flush=True)