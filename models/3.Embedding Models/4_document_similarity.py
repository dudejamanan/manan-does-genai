from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

document = [
    "virat kohli is an indian cricketer known for his aggressive batting and leadership",
    "ms dhoni is a former indian captain famous for his calm demeanor and finishing skills",
    "sachin tendulkar, also know as the 'god of cricket' , holds many batting records",
    "rohit sharma is known for his elegant batting and record-breaking double centuries",
    "jasprit bumrah is an indian fast bowler known for his unorthodox action and yorkers"
]

query = 'tell me about virat kohli'

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

similarities = cosine_similarity([query_embedding],doc_embeddings)
print(similarities)


best_match_index = np.argmax(similarities)
print("Most relevant document:")
print(document[best_match_index])