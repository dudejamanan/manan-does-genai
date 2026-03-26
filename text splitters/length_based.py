#use this site to visualize any type of chunking -  https://chunkviz.up.railway.app/ 

from langchain_text_splitters import CharacterTextSplitter

text =  '''
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.
Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
'''

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0, #this is used so that previous wala bhi thoda lele and abruptly beech mei break na ho and context retain kr paae better    
    separator=''
)  

result = splitter.split_text(text)
print(result)

'''
this is used where we do not rely on any structure or meaning in the text, and the only goal is to divide the text into chunks of a fixed size, which is useful when we just need uniform chunks for processing

in this, the splitting happens like, we take the text and cut it after a fixed number of characters or tokens defined by chunk_size, and then continue this process for the entire text, optionally keeping some overlap between consecutive chunks to maintain continuity

the idea is to ensure that all chunks are of similar size so that they can be processed efficiently by models with input limits, even though this method may break sentences, paragraphs, or logical units since it does not consider structure or semantic meaning
'''