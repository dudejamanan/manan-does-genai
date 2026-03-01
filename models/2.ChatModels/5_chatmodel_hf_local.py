from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5, #controls creativity
        max_new_tokens=100 #max token a model can generate in a response
    )
)
model = ChatHuggingFace(llm=llm) #This converts your raw text-generation pipeline into a chat-style model compatible with LangChain's chat interface.

result = model.invoke("What is the capital of India")

print(result.content)