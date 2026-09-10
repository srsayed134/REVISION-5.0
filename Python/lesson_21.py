#Challenge 01
"""
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()
"""

#Challenge 02
"""

class Employee:
    def __init__(self, name, age):
        self.ename = name
        self.eage = age

class AIEngineer(Employee):
    pass

engineer1 = AIEngineer("Sayd", 23)
print(engineer1.ename)
print(engineer1.eage)
"""
#Challenge 03
"""

class Employee:
    def __init__(self, name, age):
        self.ename = name
        self.eage = age

class AIEngineer(Employee):
    def __init__(self, name, age, skills):
        super().__init__(name, age)
        self.eskills = ",".join(skills)

engineer1 = AIEngineer(
    "Sayed",
      23,
      ["Python", "Java", "GoLang"]
)
print(engineer1.eskills) 
print(engineer1.ename) 
print(engineer1.eage) 
"""
#Challenge 04
"""

class Employee:
    def __init__(self, name, age, language):
        self.ename = name
        self.eage = age
        self.elanguage = ",".join(language)

    def introduce(self):
        print(f"Employe name is {self.ename} and age is {self.eage}")

class AIEngineer(Employee):
    def __init__(self, name, age, language):
        super().__init__(name, age, language)

    def show_skills(self):
        print(f"{self.ename} skills is {self.elanguage}")

engineer = AIEngineer(
    "Sayed",
    24,
    ["Pyhton", "JavaScript", "React"]
)

engineer.introduce()
engineer.show_skills()
"""
#Challenge 05
"""
class Employee:
    def work(self):
        print("Employee is working")

class AIEngineer(Employee):
    def work(self):
        print("AI Engineer is building AI system")

engineer1 = AIEngineer()
engineer1.work() #AI Engineer is building AI system
"""


#Challenge 06
"""
class Employee:
    def work(self):
        print("Employee is working")

class AIEngineer(Employee):
    def work(self):
        super().work()
        print("AI Engineer is building AI system")

engineer1 = AIEngineer()
engineer1.work()
"""

#Challenge 07
"""

class Employee:
    def work(self):
        print("This is from employee")

class Engineer(Employee):
    def write_code(self):
        print("This is from engineer")

class AIENgineer(Engineer):
    def train_model(self):
        print("This is from AIEngineer")

engineer1 = AIENgineer()
engineer1.work()
engineer1.write_code()
engineer1.train_model()
"""
#Challenge 08
"""
class Employee:
    def __init__(self, name, age):
        self.ename = name
        self.eage = age

    def introduce(self):
        print(f"This is {self.ename} and age is {self.eage}")

class Engineer(Employee):
    def __init__(self, name, age, programming_language):
        super().__init__(name, age)
        self.eprogramming_language = programming_language

    def write_code(self):
        print(f"{self.ename} is writing {self.eprogramming_language} code")

class AIENgineer(Engineer):
    def __init__(self, name, age, programming_language, specialization, skills):
        super().__init__(name, age, programming_language)
        self.especialization = specialization
        self.eskills = ",".join(skills)

    def build_model(self):
        print(f"{self.ename} is building {self.especialization} model")

engineer1 = AIENgineer("Sayedur", 25, "Python", "NLP", ["Python", "PyTorch", "Transformer"])

print(f"Name: {engineer1.ename} \n Age: {engineer1.eage} \n Language: {engineer1.eprogramming_language} \n Specialization: {engineer1.especialization} \n Skills:  {engineer1.eskills} ")
engineer1.introduce()
engineer1.write_code()
engineer1.build_model()
"""