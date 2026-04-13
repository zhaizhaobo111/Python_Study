# 示例选择器
# 反义词⽰例集合
from sys import prefix

from langchain_chroma import Chroma
from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.example_selectors import LengthBasedExampleSelector, SemanticSimilarityExampleSelector, \
    MaxMarginalRelevanceExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings

examples = [
        {"input": "happy", "output": "sad"},
        {"input": "tall", "output": "short"},
        {"input": "energetic", "output": "lethargic"},
        {"input": "sunny", "output": "gloomy"},
        {"input": "windy", "output": "calm"},
]
# 示例(提示词)模板
prompt_template=PromptTemplate.from_template("Input:{input}\nOutput:{output}")
#———————————————————————————————————————————————————————————————————————————————————————————————————————
# # 示例选择器(长度选择)
# example_selector=LengthBasedExampleSelector(
#     examples=examples,
#     example_prompt=prompt_template,
#     max_length=25
# )
#———————————————————————————————————————————————————————————————————————————————————————————————————————
# 示例选择器(语义相似性)
# example_selector=SemanticSimilarityExampleSelector.from_examples(
#     examples,
#     OpenAIEmbeddings(),
#     Chroma,
#     K=1,
# )
#———————————————————————————————————————————————————————————————————————————————————————————————————————
# 示例选择器(MMR)
# example_selector=MaxMarginalRelevanceExampleSelector.from_examples(
#     examples,
#     OpenAIEmbeddings(),
#     Chroma,
#     K=1,
# )
#———————————————————————————————————————————————————————————————————————————————————————————————————————
example_selector=NGramOverlapExampleSelector(
    examples=examples,
    example_prompt=prompt_template,
    threshold=-1.0,
)
#———————————————————————————————————————————————————————————————————————————————————————————————————————
# 少样本模板
# 转换message
few_shot_prompt=FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=prompt_template,
    prefix="给输出每个词的反义词",
    suffix="input:{adjective}\noutput:",
    input_variables=["adjective"]
)
print(few_shot_prompt.invoke({"adjective": "big"}).to_messages()[0].content)
