from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32) #dimension compresses the output to a 32-dimensional vector.
result = embedding.embed_query("Delhi is the capital of India")
print(str(result))