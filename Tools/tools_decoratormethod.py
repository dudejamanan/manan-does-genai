from langchain_core.tools import tool
#step1 - create a function
# def multiply(a,b):
#     '''multiply two numbers'''
#     return a*b

#step2 - app type hints
# def multiply(a:int,b:int) -> int:
#     '''multiply two numbers'''
#     return a*b

#step3 - add tool decorator
# @tool
# def multiply(a:int,b:int) -> int:
#     '''multiply two numbers'''
#     return a*b

@tool
def multiply(a:int,b:int) -> int:
    '''multiply two numbers'''
    return a*b

result = multiply.invoke({"a":3,"b":5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)