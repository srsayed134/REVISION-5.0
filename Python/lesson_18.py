#Challenge 01
"""
class Student:
    pass

student_1 = Student()
student_1.name = "Sayedur"
student_1.age = 5
print(student_1.name)
print(student_1.age)
"""

#Challenge 02
"""
class Student:
    def intro(self):
        print(f" Name: {self.name}\n Age: {self.age}\n Country: {self.country}")


student1 = Student()
student1.name = "Sayedur"
student1.age = 23
student1.country = "BD"

student1.intro()

#Challenge 03

student2 = Student()
student2.name = "Alex"
student2.age = 22
student2.country = "USA"
student2.intro()


student3 = Student()
student3.name = "Dimitri"
student3.age = 23
student3.country = "Russia"
student3.intro()

#Challenge 04
"""
#Challenge 05

class Student:
    def introduce(self):
        name = self.name
        goal = self.goal
        print(f"I am {name}")
        print(f"My goal is to become {goal}")

student1 = Student()
student1.name = "Sayed"
student1.goal = "AI Engineer" 

student1.introduce()

#Challenge 06

class AIEngineer:
    def show_profile(self):
        name = self.name
        age = self.age
        skills = self.skills
        skill = ",".join(skills)
        print(f"I am {name} age is {age} i am skilled in {skill}")


user1 = AIEngineer()
user1.name = "Sayed"
user1.age = 25
user1.skills = ["Python, Django"]

user2 = AIEngineer()
user2.name = "Alex"
user2.age = 23
user2.skills = ["Java", "Kotlin"]

user3 = AIEngineer()
user3.name = "Dimitri"
user3.age = 23
user3.skills = ["JavaScript", "React"]

user1.show_profile()
user2.show_profile()
user3.show_profile()

#Challenge 07

class AIModel:
    def show_model(self):
        name = self.name
        version = self.version
        framework = self.framework

        print(f" Name: {name} \n Version: {version} \n Framework: {framework}")

model1 = AIModel()
model1.name = "GPT"
model1.version = 5.5
model1.framework = "Sonnet"

model2 = AIModel()
model2.name = "Claude"
model2.version = 4.5
model2.framework = "Mythos"

model3 = AIModel()
model3.name = "Gemini"
model3.version = 3.3
model3.framework = "Flash_lite"

model1.show_model()
model2.show_model()
model3.show_model()