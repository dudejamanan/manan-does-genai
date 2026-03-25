from langchain_community.document_loaders import TextLoader

loader= TextLoader('document loaders\cricket.txt',encoding='utf-8')

docs = loader.load()
print(docs)
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)