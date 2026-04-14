# RAG流程
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter

# 1.创建Document文档
Document=[
Document(
    # 文本内容
    page_content="狗是忠实的宠物",
    # 元字典
    metadata={"source":"pets-doc"}
),
Document(
    page_content="猫是独立的宠物",
    metadata={"source":"pets-doc"}
)
]
# 2.创建文档加载器
# loader=PyPDFLoader(file_path="../Docs/pdf/Java - 基于 Spring 前后端分离版本的论坛系统(水印版).pdf")
# docs=loader.load()
loader = UnstructuredMarkdownLoader("../Docs/makedown/Java - 基于 Spring 前后端分离版本的论坛系统(水印版).md")
data = loader.load()
# 文本分割器（以文本长度分割）
text_splitter=CharacterTextSplitter(
    separator="\n\n",       #分隔符  有一个默认的分隔符优先级列表["\n\n","\n"]
    chunk_size=100,         #块大小
    chunk_overlap=20,       #块重叠大小
    length_function=len,    #测量字符长度的函数
    is_separator_regex=False,#是否正则表达式描写分隔符嘛？
)
documents=text_splitter.split_documents(data)
# 分割文档
for chunk in documents[:10]:
    print("*" * 30)
    print(documents)
# 输出 PDF 被切分成多少段文档
# print(f"pdf文档页数为：{len(docs)}")
# print(f"pdf文档文本内容为{docs[0].page_content[:200]}")
# # 切片只能给 字符串 / 列表 用！
# print(f"pdf文档元数据为: {str(docs[0].metadata)[:200]}")
