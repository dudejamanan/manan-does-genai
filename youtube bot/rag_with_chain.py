from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

#step1-a - Indexing (Document Ingestion)
yt_api = YouTubeTranscriptApi()


video_id = "Gfr50f6ZBvo"
try:
    #if you dont care which language, this returns the best one
    transcript_list = yt_api.fetch(video_id,languages=["en"])

    #flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video")
#now we have the document(transcript) loaded with us, the next step is to split it into chunks.


#step1-b - Indexing(text splitting)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.create_documents([transcript])
#now we have the chunks with us, the next step is to convert these chunks into vector embeddings



#step1-c - Indexing(Embedding generation and storing in vector store)


embeddings = HuggingFaceEmbeddings( #embedding model
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(chunks,embeddings)

#print(vector_store.index_to_docstore_id)
#now we have our vector space jisme sab chunks ki embeddings stored hai


#step2 - Retrieval 
retriever = vector_store.as_retriever(search_type='similarity',search_kwargs={"k":4}) #search_kwargs gives 4 similar vectors

#now we have created the retriever which takes the query and converts it into the embeddings and retrieves the most similar chunks.


#step3 - Augmentation
#augmentation means to combine both prompt and the context

prompt = PromptTemplate(
    template='''
        you are a helpful assistant. 
        Answer ONLY from the provided transcipt context.
        tf the context is insufficient, just say you dont know.

        {context}
        Question: {question}

''',
input_variables=['context','question']
)



#step4 - generation

llm = OllamaLLM(model="llama3.2") #text generation model


#building with chains
parser = StrOutputParser()

def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()

})

main_chain =  parallel_chain | prompt | llm | parser

main_chain.invoke("can you summarize the video?")