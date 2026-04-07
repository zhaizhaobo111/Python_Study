from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from openai import api_key

# # 1.基本用法
# qianwen_model=init_chat_model(model=" qwen-plus",model_provider="openai",temperature=0,api_key="sk-3b066661f42f49c9971861631950c710",base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
# print(f"qianwen-chat:{qianwen_model.invoke("早上好，千问").content}")

# 2.定义可配置模型
# config_model=init_chat_model(temperature=0.3)
# messages=[
#     SystemMessage(content="请补全一段话十个字以内"),
#     HumanMessage(content="一只可爱小狗在__?"),
# ]
# # invoke()的config参数真正意义上定义了模型
# # print(f"config_model:{config_model.invoke(input=messages, config={"configurable": {"model": "qwen-plus"}}).content}")


# 3.可配置的模型
model=init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-3b066661f42f49c9971861631950c710",
    temperature=0.1,
    max_tokens=1024,
    configurable_fields=("max_tokens",),
    config_prefix="first"
)
messages=[
    SystemMessage(content="请补全一段话100个字以内"),
    HumanMessage(content="一只可爱小狗在__?"),
]
result=model.invoke(
    input=messages,
    config={
        "configurable":{
        "first_max_tokens":10,
    }
    }
)
print(result.content)