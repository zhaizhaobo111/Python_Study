# 特殊结构分割
# 字符串⽂档
from langchain_text_splitters import PythonCodeTextSplitter
import python_splitter
from langchain_text_splitters import PythonCodeTextSplitter
from nltk.book import texts

PYTHON_CODE = """
    def hello_world():
        print("Hello, World!")
    def hello_python():
        print("Hello, Python!")
"""
# PythonCodeTextSplitter.from_tiktoken_encoder(
#     encoding_name="gpt2",
#     model_name=None,

# )
spliter=PythonCodeTextSplitter(chunk_size=50, chunk_overlap=0)
python_docs = spliter.create_documents([PYTHON_CODE])
# python_docs=PythonCodeTextSplitter.create_documents([PYTHON_CODE])
for document in python_docs[:2]:
    print("*" * 30)
    print(f"{document}\n")