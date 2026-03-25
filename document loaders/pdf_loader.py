from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('document loaders\dl-curriculum.pdf')

docs= loader.load()

print(docs)
print(len(docs)) #we have 23 document objects here, as pypdf converts it into page wise object so every page is one object

print(docs[0].page_content)
print(docs[0].metadata)

#pypdf loader isused when the pdf mostly contains textual data, else wise it does not perform good

#more pdf loaders - 
#simple, clean pdfs: PyPDFLoader
#pdfs with tables/columns: PDFPlumberLoader
#scanned/image pdfs: UnstructuredPDFLoader or AmazonTextractPDFLoader
#need layout and image data: PyMuPDFLoader
#want best structure extraction: UnstructuredPDFLoader