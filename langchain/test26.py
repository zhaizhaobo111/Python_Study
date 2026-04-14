from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

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
# 文本加载器
loader = UnstructuredMarkdownLoader("../Docs/makedown/Java - 基于 Spring 前后端分离版本的论坛系统(水印版).md")
data = loader.load()


# 文本分割器（以token为单位分割）

text_splitter=CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", #cl100k_base 是分词器的一种分割形式
    chunk_size=100,         #块大小
    chunk_overlap=20,       #块重叠大小
)
documents=text_splitter.split_documents(data)

#———————————————————————————————————————————————————————————————————————————————————————————————————————
# 文本分割器（以token为单位分割）
# RecursiveCharacterTextSplitter  强制分割，硬性约束⻓度拆分
text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    separator=["\n\n","\n"," "],    #分隔符  有一个默认的分隔符优先级列表["\n\n","\n"]
    chunk_size=100,         #块大小
    chunk_overlap=20,       #块重叠大小
    length_function=len,    #测量字符长度的函数
    is_separator_regex=False,#是否正则表达式描写分隔符嘛？
)