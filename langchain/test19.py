
# 提示词网址  https://smith.langchain.com/hub/
# ： hardkothari/prompt-maker 。
# Create a LangSmith API in Settings > API Keys
# Make sure API key env var is set:
# import os; os.environ["LANGSMITH_API_KEY"] = "<your-api-key>"
from langchain_community.chat_models import ChatTongyi
from langsmith import Client

client = Client()
prompt = client.pull_prompt("hardkothari/prompt-maker")
model=ChatTongyi(model="qwen-turbo",api_key="sk-3b066661f42f49c9971861631950c710")
chain=prompt|model

while True:
    task = input("\n你的任务是什么？（输⼊ quit 退出聊天）\n")
    if task == 'quit':
        break

    lazy_prompt = input("\n你当前的提⽰是什么？（输⼊ quit 退出聊天）\n")
    if lazy_prompt == 'quit':
        break

    chain.invoke({
            "task": task,
            "lazy_prompt": lazy_prompt
        }).pretty_print()