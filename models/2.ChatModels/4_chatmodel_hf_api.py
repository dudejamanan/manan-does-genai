#huggingface - Connects LangChain to a Hugging Face text generation pipeline.
#chathuggingface - Wraps that pipeline so it behaves like a chat model (like ChatGPT-style interaction)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
#repo id is - which model to use
#task tells Hugging Face what type of inference you want

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)