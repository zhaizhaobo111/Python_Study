from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# 定义嵌入模型
embeddings=OllamaEmbeddings(
    model="nomic-embed-text",
)

# 内存向量存储
vector_store=InMemoryVectorStore(embedding=embeddings)

# 文本加载器
# 获取文档列表
loader=UnstructuredMarkdownLoader("../Docs/makedown/论坛系统.md")
# Documents列表
data=loader.load()
# 文本分割器
test_splitter=CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=200,
    chunk_overlap=20,
)
# 文档列表
docs=test_splitter.split_documents(data)
# 存储文档到向量存储中
# add_documents ： 将要存储的文档列表进行编译索引
ids=vector_store.add_documents(docs)
print(f"共有{len(docs)}个文档，编译了{len(ids)}个索引")
print(f"前三个文档的索引：{ids[:3]}")

docs_2=vector_store.get_by_ids(ids[:2])
