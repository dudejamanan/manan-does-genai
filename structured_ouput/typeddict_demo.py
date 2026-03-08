#TypedDict is often used to define expected structured outputs from LLMs.
#TypedDict becomes the schema contract.
from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'nitish', 'age':'35'}

print(new_person)


'''
Feature         	TypedDict	Pydantic
Runtime validation	 ❌	         ✅  mtlb run time pe validate ni hora if koi aur data type bhi hai toh vo bhi execute hojaega, typeddict bs btane ke liye hota hai , no validation 
Type checking	     ✅	         ✅
Automatic parsing	 ❌	         ✅
Data conversion	     ❌	         ✅


TypedDict is used when:

defining output schema
lightweight structure
simple structured responses

Pydantic is used when:

validating LLM outputs
converting types
building reliable pipelines
'''