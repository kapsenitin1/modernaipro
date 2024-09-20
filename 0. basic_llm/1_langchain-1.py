# Note:
# Use something like this: conda create --name modernaipro python=3.11 --file requirements.txt
# conda activate modernaipro
# Install gemma2 model on your local machine
# ollama pull gemma2:2b
# 2b represents 2 billion parameters of the model
# Execute <BasePath>\modernaipro\0. basic_llm> python .\1_langchain-1.py
from langchain_community.llms import Ollama
llm = Ollama(model="qwen") # try qwen2 / llama3/gemma2:2b if you have that model


for chunks in llm.stream("Write me a poem about Ramayan in 3 sentences"):
    print(chunks, end='\n')
