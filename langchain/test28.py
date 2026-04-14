# 定义/嵌入模型
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.embeddings import DashScopeEmbeddings, HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# embeddings=OpenAIEmbeddings(
#     model="Qwen3-Embedding-8B",
# )
# embeddings=DashScopeEmbeddings(
#     model="Qwen3-Embedding-8B",
# )
# 拉取ollama 嵌入模型 nomic-embed-text
# embeddings=OllamaEmbeddings(
#     model="nomic-embed-text",
# )
#
# query_vector=embeddings.embed_query("hello")
# print(len(query_vector))
# 拉取ollama 嵌入模型 nomic-embed-text

# 拉取ollama 嵌入模型 nomic-embed-text
embeddings=OllamaEmbeddings(
    model="nomic-embed-text",
)

# 文本加载器
# single 模式，生成一个大文档
loader=UnstructuredMarkdownLoader("../Docs/makedown/Java - 基于 Spring 前后端分离版本的论坛系统(水印版).md")
# Documents列表
data=loader.load()
# 文本分割器
test_splitter=CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=400,
    chunk_overlap=50,
)
# 文档列表
docs=test_splitter.split_documents(data)
# 将文档列表转换为向量列表
# 注意:这⾥需要提取⽂档内容为字符串列表，才能传递给嵌⼊模型
text=[doc.page_content for doc in docs]
docs_vector=embeddings.embed_documents(text)
print(f"⽂档数量为：{len(docs)}，⽣成了{len(docs_vector)}个向量的列表")
print(f"第⼀个⽂档向量维度：{len(docs_vector[0])}")
print({docs_vector[0][:5]})
