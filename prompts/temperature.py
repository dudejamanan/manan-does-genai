from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",   # or "gemini-1.5-pro"
    temperature=1.5
)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
