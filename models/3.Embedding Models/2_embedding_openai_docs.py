from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "delhi is the capital of india",
    "kolkata is the capital of west bengal",
    "paris is the capital of france"
]


embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
result = embedding.embed_documents(documents)
print(str(result))