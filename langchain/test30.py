from typing import List
from langchain_core.runnables import chain
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_text_splitters import CharacterTextSplitter
"""
# 离线数据处理 ： 文档加载——>文档拆分——>将文本存储入向量库
"""


# 定义嵌入模型
embeddings=OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
)
# 配置redis客户端
redis_url = "redis://192.168.100.238:6379"
config = RedisConfig(
        index_name="qa",
        redis_url=redis_url,
        metadata_schema=[
        {"name": "category", "type": "tag"},
        {"name": "num", "type": "numeric"},
],
)
# redis存储初始化
# 向量库
vector_store=RedisVectorStore(embeddings=embeddings,config=config)

# 定义文档加载器
loader=UnstructuredMarkdownLoader("../Docs/makedown/新建 文本文档.md")
data=loader.load()
# 定义文档分词器
text_splitter=CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=200,
    chunk_overlap=20
)
# # 文本列表
# doc=text_splitter.split_documents(data)
# # 将文本列表存储向量数据库
# vector_store.add_documents(doc)
#定义检索器
retriever=vector_store.as_retriever()
docs=retriever.invoke("要传入的信息")
for doc in docs:
    print("*"*30)
    print(f"{doc[:3]}")

# 通过 @chain 创建检索器
# 1.LangChain 检索器是⼀个 Runnable 的对象
# 2. LangChain 检索器输⼊为查询字符串，输出为⽂档列表（标准化的 LangChain ⽂档对象Document）
@chain
def retriever(query:str)->List[Document]:
    return vector_store.similarity_search(query,k=2)

docs=retriever.invoke("要传入的信息")
for doc in docs:
    print("*"*30)
    print(f"{doc[:3]}")