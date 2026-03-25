from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.amazon.in/HARLEY-DAVIDSON-Motorcycle-Metallic-booking-Ex-Showroom/dp/B0FDGWRMMN/?_encoding=UTF8&pd_rd_w=r8wpo&content-id=amzn1.sym.19c1fe77-024a-484e-85dd-b22ab1977129&pf_rd_p=19c1fe77-024a-484e-85dd-b22ab1977129&pf_rd_r=X7EFDJF2BMEGPQ9H8G64&pd_rd_wg=TX2QX&pd_rd_r=98ac747c-76ab-4bd1-8cc7-b267661c8e34&ref_=pd_hp_d_btf_ls_gwc_pc_en4_&th=1'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)