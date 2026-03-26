from langchain_text_splitters import RecursiveCharacterTextSplitter

text =  '''
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.
Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap=0    
)  

result = splitter.split_text(text)
print(result)

'''
Splitting hierarchy:
\n\n → paragraphs
\n → lines
" " → words
characters (last resort)
'''

'''
this is used where the text already contains some natural structure like paragraphs, line breaks, or sections, so we don’t need to understand the meaning of the sentences to split it

in this, the splitting happens like, first we look for larger separators such as paragraph breaks (\n\n), if those are not present or chunks are still too large, then we move to smaller separators like line breaks (\n), then spaces (" "), and finally characters as a last option

the idea is to preserve as much natural structure as possible, so the splitter tries to break the text at positions where it already has some formatting instead of randomly cutting it, ensuring that the chunks remain readable and organized even without understanding the semantic meaning

'''