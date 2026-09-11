#Challenge 01
"""
class Dog:
    def speak(self):
        print("WOOF")

class Cat:
    def speak(self):
        print("MEWWO")

sounds = [
    Dog(),
    Cat()
]

for sound in sounds:
    sound.speak()
"""

#Challenge 02
"""

class Employee:
    def work(self):
        print("Employee is working")

class AIEngineeer(Employee):
    def work(self):
        print("AIEngineer is working")

class DataScientist(Employee):
    def work(self):
        print("Data scientist is working")

works = [
    Employee(),
    AIEngineeer(),
    DataScientist()
]
for work in works:
    work.work()
"""

#Challenge 03
"""
class AIEngineer:
    def work(self):
        print("AIEngineer is working")

class Robot:
    def work(self):
        print("Robot is working")

class Freelencer:
    def work(self):
        print("Freelencer is working")



def start_work(workder):
    workder.work()

start_work(AIEngineer())
start_work(Robot())
start_work(Freelencer())
"""

#Challenge 04
"""

class ImageModel:
    def predict(self):
        print("Image model is making image.....")

class TextModel:
    def predict(self):
        print("Text model is sending messages....")

class SpeechModel:
    def predict(self):
        print("Speech model is taking with user....")

models = [
    ImageModel(),
    TextModel(),
    SpeechModel()
]
for model in models:
    model.predict()
"""
#Challenge 05

"""
class CardPayment:
    def pay(self, ammount):
        print(f"{ammount} has been paid")
class BankPayment:
    def pay(self, ammount):
        print(f"{ammount} has been paid")
class CryptoPayment:
    def pay(self, ammount):
        print(f"{ammount} has been paid")

payments = [
    CardPayment(),
    BankPayment(),
    CryptoPayment()
]
for payments in payments:
    ammount = 1000
    payments.pay(ammount)
"""

#Challenge 06
"""
class AIEngineer:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"{self.name} is an AIEngineer")


class DataScientist:
    def __init__(self, name):
            self.name = name
    def introduce(self):
        print(f"{self.name} is a data scientist")


class MLResearcher:
    def __init__(self, name):
            self.name = name
    def introduce(self):
        print(f"{self.name} is a machine learning researcher")


aiengineer1 = AIEngineer("Sayed")
datascientist1 = DataScientist("Alex")
mlresearcher1 = MLResearcher("Dimitri")

def intoduce_person(person):
     person.introduce()

intoduce_person(aiengineer1)
intoduce_person(datascientist1)
intoduce_person(mlresearcher1)
"""

#Challenge 07
"""
class Employee:
    def work(self):
        print("Employee is working")

class Engineer(Employee):
    def work(self):
        print("Engineer is working")

class AIEngineer(Engineer):
    def work(Self):
        print("AIEngineer is working")

Employee().work()
Engineer().work()
AIEngineer().work()

employee = [
    Employee(),
    Engineer(),
    AIEngineer()
]
for employe in employee:
    employe.work()
"""

#Challenge 08
"""

class AIModel:
    def predict(self):
        print("AIModel is running....")

class TextModel(AIModel):
    def predict(self):
        print("TextModel is running....")

class LLModel(TextModel):
    def predict(self):
        print("LLModel is running....")

class ImageModel(AIModel):
    def predict(self):
        print("ImageModel is running....")

models = [
    TextModel(),
    LLModel(),
    ImageModel()
]
for model in models:
    model.predict()
"""