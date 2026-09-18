#Challenge 01
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    university: str

student1 = Student("Sayed", 23, "ABC University")
student2 = Student("Alex", 25, "XYZ University")

print(student1)
"""

#Challegne 02
"""

from dataclasses import dataclass

@dataclass
class AIModel:
    name : str
    version : float
    framework : str

model1 = AIModel("ChatGpt", 4.2, "Transformer")
model2 = AIModel("Gemini", 3.2, "Transformer")
model3 = AIModel("ChatGpt", 4.2, "Transformer")

print(model2 == model3)
print(model1 == model3)
"""

#Challenge 03
"""

from dataclasses import dataclass

@dataclass
class User:
    name : str
    age : int
    country : str = "Bangladesh"

user1 = User("Sayed", 23, "USA")
user2 = User("Alex", 21)

print(user1)
print(user2)

"""
#Challenge 04
"""

from dataclasses import dataclass

@dataclass
class BankAccount():
    name: str
    balance :int

    def deposite(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        self.balance -= ammount

user = BankAccount("Sayed", 0)
user.deposite(1000)
user.withdraw(500)
print(user.balance)
"""

#Challenge 05
"""

from dataclasses import dataclass, field

@dataclass
class Developers:
    name : str
    skills : list = field(default_factory=list)

developer1 = Developers("Sayed", ["Python", "Java"])
print(developer1.skills)
developer2 = Developers("Alex")
print(developer2.skills)
"""

#Challenge 06
"""

from dataclasses import dataclass, field

@dataclass
class User:
    name : str
    email : str
    password : int = field(repr=False)

user1 = User("Sayed", "name@example.com", 12345678)
print(user1) #Not appared
print(user1.password) #But password appeared

"""
#Challenge 07
"""

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Coordinates:
    x : int
    y : int

point = Coordinates(30, 42)
print(point)


point.x = 20 #Will give frozen instance error
print(point)
"""

#Challenge 08
"""
from dataclasses import dataclass, field

@dataclass
class AIModelConfig:
    name : str
    version : float
    framework: str
    temperature: float = 0.7
    max_tokens : int = 1000

    def show_config(self):
        print(f"Name: {self.name} Version: {self.version} Framework:{self.framework} Temperatire:{self.temperature} Max_tokens: {self.max_tokens}")

model1 = AIModelConfig("GPT", 5.0, "Transformer", 0.7, 128000)
model2 = AIModelConfig("GPT", 5.0, "Transformer", 0.7, 128000)
model3 = AIModelConfig("Claude", 4.0, "Transformer", 0.7, 200000)

model1.show_config()
print(model1 == model3)
print(model1 == model2)
"""