#Challenge 01
"""
class Student:

    school = "ABC School"
    def __init__(self, name, age):
        self.sname = name
        self.sage = age

student1 = Student("Sayed", 25)
student2 = Student("Alex", 22)

print(student1.sname)
print(student1.sage)
print(student1.school)

print(student2.sname)
print(student2.sage)
print(student2.school)
"""

#Challenge 02
"""

class AIEngineer:

    company = "AI Corp"

    def __init__(self, name, age):
        self.sname = name
        self.sage = age

engineer1 = AIEngineer("Sayed", 23)
engineer2 = AIEngineer("Alex", 22)
engineer3 = AIEngineer("Dimtri", 21)

print(engineer1.sname)
print(engineer1.sage)
print(engineer1.company)
print(engineer2.sname)
print(engineer2.sage)
print(engineer2.company)
print(engineer3.sname)
print(engineer3.sage)
print(engineer3.company)
"""
#Challenge 03
"""

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.sname = name

student1 = Student("Sayed")
student2 = Student("Nim")

print(student1.school)
print(student2.school)
Student.school = "XYZ School"

print(student1.school)
print(student2.school)
"""

#Challenge 04
"""

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.sname = name

student1 = Student("Sayed")
student2 = Student("Alex")

print(student1.school) # "ABC School"
student1.school = "Private school"

print(Student.school) # "ABC School"
print(student1.school) # "Private school"
print(student2.school) # "ABC School"
"""

#Challenge 05
"""

class AIEnginner:

    company = "AI Corp"
    @classmethod

    def show_company(cls):
        print(f"This \"{cls.company}\" is the name of my company")

AIEnginner.show_company()

"""
#Challenge 06
"""

class AIModel:
    company = "OLD AI"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

print(AIModel.company)
AIModel.change_company("New AI")
print(AIModel.company)
"""
#Challenge 07
"""
class AIModel:

    company = "AI Research Lab"
    model_count = 0

    def __init__(self, name, version, framework):
        self.sname = name
        self.sversion = version
        self.sframework = framework

    @classmethod
    def show_model_count(cls):
        print(f"Total models: {cls.model_count}")

models = []

while True:
    name = str(input("Name: (for stop type 'quit')"))
    if name.lower() == "quit":
        break
    version = float(input("Version: "))
    framework = str(input("Framework: "))

    models.append(AIModel(name, version, framework))
    AIModel.model_count += 1

print(AIModel.model_count)
"""

#Challenge 08
"""
class AIModel:

    def __init__(self, name, version, framework):
        self.mname = name
        self.mversion = version
        self.mframework = framework

    @classmethod
    def from_string(cls, data):
        name, version, framework = data.split(",")
        return cls(name, float(version), framework)

model1 = AIModel.from_string("GPT, 5.5, PyTorch")

print(model1.mname)
print(model1.mversion)
print(model1.mframework)

"""