from langchain_ollama import ChatOllama
# ollama 本地部署
ollama_model=ChatOllama(model="deepseek-r1:8b",base_url="http://127.0.0.1:11434")
print(ollama_model.invoke("who are you").content)