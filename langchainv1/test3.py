from langchain.agents.middleware import ModelRequest, ModelResponse, wrap_model_call
from langchain_openai import ChatOpenAI

basic_model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=apikey,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1" # 百炼兼容网关
)
@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler, advanced_model=None) -> ModelResponse:
    """根据对话⻓度选择模型。"""
    message_count = len(request.state["messages"])
    if message_count > 10:
    # ⻓对话使⽤⾼级模型
        model = advanced_model
    else:
    # 短对话使⽤基础模型
        model = basic_model
    return handler(request.override(model=model))

@wrap_model_call
def state_based_tools(request: ModelRequest, handler) -> ModelResponse:
    is_authenticated = request.state.get("authenticated", False)
    if not is_authenticated:
        # 只保留名称以 "public_" 开头的⼯具
        public_tools = [t for t in request.tools if t.name.startswith("public_")]
        request = request.override(tools=public_tools)
    return handler(request)