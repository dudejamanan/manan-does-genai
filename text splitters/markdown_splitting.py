from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


text = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.

## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=150,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)

#this splitting technique is same as the text_structure based text splitting just the splitting parameters are different, in this we specify that which is the language,in this case its markdown , then according to it it decides the parameters , like # can be one parameter , one can be - etc etc.

'''
this is used where the text is written in markdown format, where structure is defined using elements like headings, subheadings, lists, and code blocks, so splitting should follow these markers instead of treating the text as plain sentences

in this, the splitting happens like, first we look for major sections using headings such as #, ##, ###, if the content under a heading is too large, then we further split based on subheadings, lists, or paragraphs, and if required, we finally split into smaller parts while making sure that code blocks and formatting are not broken

the idea is to preserve the hierarchical structure of the document so that each chunk represents a meaningful section, instead of randomly cutting across headings or code blocks, ensuring that the chunks remain well-organized and easy to understand even without analyzing the semantic meaning
'''