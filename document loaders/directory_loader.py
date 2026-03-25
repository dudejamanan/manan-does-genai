from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='document loaders\directory',
    glob='*.pdf', #jo bhi is type ki files ho unhe load krlo
    loader_cls=PyPDFLoader #ye wala loader we want 
)

docs=loader.load()
#docs=loader.lazy_load()
#we can also use laze_load instead of load, it is used when no of total documents are more,it brings documents what are required not all at a time

print(len(docs)) #25  mtlb teeno pdfs ko milake total no. of pages will be 25
print(docs[0].page_content) #1st pdf ka content
print(docs[0].metadata) #1st pdf ka metadata

#directory loader is used to load multiple files ,it can be of any type

for document in docs:
    print(document.metadata)