# import nltk
#
# # 下载缺失的资源
# nltk.download('gutenberg')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from langchain_core.prompts import PromptTemplate
# 1. 定义模板
prompt_template = PromptTemplate.from_template(

"Translate the following into{language}")

# 2. 实例化模板
print(prompt_template.invoke({"language": "Chinese"}))