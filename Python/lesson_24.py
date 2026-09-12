"""
class Init:
    def __init__(self, name, age):
        self.iname = name
        self.iage = age
    def intro(self):
        print(f"{self.iname} is {self.iage} years old")
    def __str__(self):
        return (f"{self.iname} is {self.iage} yoear old")
    def __repr__(self):
        return (f"Student (name= '{self.iname}' and age= '{self.iage}')")

init_example = Init("Sayed", 13)
print(init_example)
print(repr(init_example))

class Len:
    def __init__(self, skills):
        self.skills = skills

    def __len__(self):
        return len(self.skills)

len_example = Len(["Python", "JavaScript", "Java"])
print(len(len_example))

class Eq:
    def __init__(self, name, age):
        self.ename = name
        self.eage = age

    def __eq__(self, other):
        return self.ename == other.ename and self.eage == other.eage

eq_example = Eq("Sayed", 23)
eq_example1 = Eq("Sayed", 23)
eq_example3 = Eq("Sayed", 23)

print(eq_example == eq_example3)

"""
"""
class Add:
    def __init__(self, num):
        self.anum = num

    def __add__(self, other):
        return self.anum + other.anum

add_example = Add(22)
add_example1 = Add(25)

total = add_example1 + add_example
print(total)
"""
"""

class Add:
    def __init__(self, num):
        self.anum = num

    def __add__(self, other):
        return Add(self.anum + other.anum)

add_example = Add(22)
add_example1 = Add(25)

total = add_example1 + add_example
print(total.anum)

class GetItem:
    def __init__(self, skills):
        self.gskills = skills

    def __getitem__(self, key):
        return self.gskills[key]

getitem_example = GetItem(["Python", "Java", "React"])
print(getitem_example[2])


class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, item):
        return item in self.members

team1 = Team(["Alex", "Niom", "Dimitri"])
print("Alex" in team1)
print("Sayed" in team1)
"""
#Challenge 01
"""

class Student:
    def __init__(self, name, age):
        self.sname = name
        self.sage = age
    def __str__(self):
        return f"{self.sname} is {self.sage} years old"

student1 = Student("Sayed", 23)
print(student1)
"""

#Challenge 02
"""
class AIModel:
    def __init__(self, name, version, framework):
        self.mname = name

        self.mversion = version
        self.mframework = framework

    def __repr__(self):
        return (f"AIModel (name = '{self.mname}' version = '{self.mversion} framework = '{self.mframework})")

aimodel1 = AIModel("GPT", "5.5", "Pytorch")
print(repr(aimodel1))

"""
#Challenge 03
"""
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team1 = Team(["Sayed", "Alex", "Nim"])
print(len(team1))
"""

#Challenge 04

class Student:
    def __init__(self, name, language, score):
        self.sname = name
        self.slanguage = language
        self.sscore = score

    def __eq__(self, value):
        return self.sname == value.sname and self.slanguage == value.slanguage and self.sscore == value.sscore

student1 = Student("Sayed", "Python", 82)
student2 = Student("Sayed", "Python", 82)
student3 = Student("Alex", "Java", 85)

print(student1 == student2)
print(student1 == student3)
print(student2 == student3)

#Challenge 05

class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __str__(self):
        return f"{self.amount}"

money = Money(250)
money1 = Money(248)

total = money + money1
print(type(total.amount)) #<class 'int'>
print(type(total)) #<class '__main__.Money'> #Because total is from main class

#Challenge 06

class Skills:
    def __init__(self, skills):
        self.skills = skills
    def __getitem__(self, key):
        return self.skills[key]
    def __contains__(self, item):
        return item in self.skills

person1 = Skills(["Pyhton", "React", "Javascript", "Java"])
print(person1[2])
print(person1[1])
print(person1[0])

#Challenge 07
person2 = Skills(["Pyhton", "React", "Javascript", "Java"])
print("React" in person2) #True
print("GoLang" in person2) #False

#Challenge 07

class AIModel:
    def __init__(self, name, version, framework):
        self.mname = name
        self.mversion = version
        self.mframework = framework

    def __str__(self):
        return (f"Model name: {self.mname}, Model version: {self.mversion}, Model Framework: {self.mframework}")

    def __repr__(self):
        return (f"AIModel: (Name: '{self.mname}',Name: '{self.mversion}',Name: '{self.mframework}' )")
    def __eq__(self, value):
        return self.mname == value.mname and self.mversion == value.mversion and self.mframework == value.mframework

model1 = AIModel("GPT", "5.6", "PyTorch")
model2 = AIModel("GPT", "5.6", "PyTorch")
model3 = AIModel("BERT", "1.0", "PyTorch")

print(model1)
print(model2)
print(model3)

print(repr(model1))
print(repr(model2))
print(repr(model3))

print(model1 == model2) #True
print(model2 == model3) #False
print(model1 == model3) #False

