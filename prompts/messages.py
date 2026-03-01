from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages=[   #role-based messages.
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)


'''
SystemMessage → defines behavior

HumanMessage → user input

AIMessage → model output
'''

'''
Single string
↓
PromptTemplate
↓
ChatPromptTemplate
↓
Manual conversation memory
↓
Agents
'''