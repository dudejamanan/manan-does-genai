from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Aarav", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=350,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)

#this splitting technique is same as the text_structure based text splitting just the splitting parameters are different, in this we specify that which is the language , then according to it it decides the parameters , like class can be one parameter , one can be def etc etc.

'''
this is used where the text is actually source code, and instead of normal paragraphs or sentences, the structure is defined by programming constructs like functions, classes, loops, and indentation, so splitting should respect these boundaries to avoid breaking logic

in this, the splitting happens like, first we try to identify larger code blocks such as classes or functions, if the code is still too large, then we move to smaller units like methods, loops, or conditional blocks, and if needed, we further split based on lines while making sure the syntax and indentation are preserved

the idea is to keep each chunk logically complete so that it can be understood or executed independently, instead of randomly cutting code which might break variables, scopes, or statements, ensuring that the chunks remain meaningful even without analyzing the deeper semantics of the code
'''