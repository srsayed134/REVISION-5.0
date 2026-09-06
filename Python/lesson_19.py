#Challenge 01
"""
class Student:
    def __init__(self, name, age, country):
        self.sname = name
        self.sage = age
        self.scountry = country

student1 = Student("Sayed", 23, "BD")
print(student1.sname)
print(student1.sage)
print(student1.scountry)

#Challenge 02

student2 = Student("Alex", 24, "UK")
student3 = Student("Shin Chao", 18, "China")

print(student2.sname)
print(student2.sage)
print(student2.scountry)
print(student3.sname)
print(student3.sage)
print(student3.scountry)
"""

#Challenge 03
"""
class Student:
    def __init__(self, name, age, country):
        self.sname = name
        self.sage = age
        self.scountry = country

    def introduce(self):
        print(f"My name is {self.sname}")
        print(f"I am {self.sage} years old")
        print(f"I am from {self.scountry} ")

student1 = Student("Sayedur", 25, "Bangladesh")
student1.introduce()
"""
#Challenge 04:
"""
class AIEngineer:
    def __init__(self, name, age, skills):
        self.ename = name
        self.eage = age
        self.eskills = ",".join(skills)

    def show_profile(self):
        print(f"My name is {self.ename}, i am now {self.eage} and i am experienced in {self.eskills}")
"""
#Static
"""
engineer1_skill = ["Python", "React", "Java"]
engineer1 = AIEngineer("Sayed", 25, engineer1_skill)

engineer1.show_profile()
"""
#Dynamic input
"""
users = []

while True:
    print("\n Enter details for new user: ")
    name = input("Name (or type 'quit' to stop): ")
    if name.lower() == "quit":
        break

    age = int(input("Enter your age: "))
    skills = [
        skill.strip().capitalize()
        for skill in input("Skills (comma-separated): ").split(",")
        ]

    users.append(AIEngineer(name.capitalize(), age, skills))

for user in users:
    user.show_profile()
"""

#Challenge 05
"""
class AIEngineer:
    def __init__(self, name, age, country, experience="Junior"):
        self.ename = name
        self.eage = age
        self.ecountry = country
        self.eexperience = experience

engineer1 = AIEngineer("Sayedur", 23, "BD")
engineer2 = AIEngineer("Alex", 28, "USA", "Senior")

print(engineer1.ename)
print(engineer1.eage)
print(engineer1.ecountry)
print(engineer1.eexperience)

print(engineer2.ename)
print(engineer2.eage)
print(engineer2.ecountry)
print(engineer2.eexperience)
"""
#Challenge 06
"""
class Student:
    def __init__(self, name, age):
        self.sname = name
        self.sage = age
    def intro(self):
        print(f"I am {self.sname} and age is {self.sage}")

student1 = Student("Sayed", 23)
print(student1.sname) #Sayed
student1.sname = "Saied"
print(student1.sname) #Saied

"""

#Challenge 07

class AIModel:
    def __init__(self, name, version, framework, parameters, engines):
        self.mname = name
        self.mversion= version
        self.mframework= framework
        self.mparametrs= parameters
        self.mengines = ",".join(engines)
    def show_model(self):
        print(f"\n Model: {self.mname} \n Version: {self.mversion} \n Framework: {self.mframework} \n Parameters: {self.mparametrs} \n Engines: {self.mengines}")

models = []

while True:
    print("Enter details for new model: ")
    name = input("Name (for exit type 'Quit'): ")
    if name.lower() == "quit":
        break

    version = str(float(input("Version: ")))
    framework = str(input("Framework name: "))
    parameters = int(input("Parameters: "))
    engines = [
        engine.strip().capitalize()
        for engine in input("Enginge name(qumma-separated): ").split(",")]

    models.append(AIModel(name.capitalize(), version, framework, parameters, engines))

for model in models:
    model.show_model()