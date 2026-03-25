from langchain_community.document_loaders import csv_loader

loader = csv_loader(file_path='Social_Network_Ads.csv')

docs=loader.load()

print(len(docs))

#every row- one document object