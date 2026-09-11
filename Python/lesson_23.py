#Challenge 01
"""
class Engine:
    def start(self):
        print("Engine is running")

    def stop(self):
        print("Engine is stop")

class Car:

    def start(self):
        self.start = Engine().start()
        print("Car Started")

    def stop(self):
        self.stop = Engine().stop()
        print("Car is stoped")

car1 = Car()
car1.start()
car1.stop()
"""

#Challenge 01.1
"""
class Engine:
    def start(self):
        print("Engine is running")
    
    def stop(self):
        print("Engine is stop")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print(f"Car started")

    def stop(self):
        self.engine.stop()
        print(f"Car is stopped")

car1 = Car()
car1.start()
car1.stop()
"""

#Challenge 02
"""
class CPU:
    def process(self):
        print("CPU is processing data")

class RAM:
    def load(self):
        print("RAM is loading data")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()

computer1 = Computer()
computer1.cpu.process()
computer1.ram.load()
"""

#Challenge 03
"""
class Computer:

    def computer_code(self, language):
        print(f"Computer is running {language}")

class AIEngineer:
    def __init__(self, name):
        self.ename = name
        self.ecode = Computer()

    def code(self, language):
        print(f"{self.ename} is codding {language}")
        self.ecode.computer_code(language)

engineer1 = AIEngineer("Sayed")
engineer1.code("Python")
"""

#Challenge 04
"""
a = Inheritance
b = Composition
c = Inheritence
d = Composition
e = Inheritence
"""

#Challenge 05 
"""

class Model:
    def predict(self):
        print("Model is predicting")

class AIApplication:
    def __init__(self, model):
        self.model = model

    def run(self):
        self.model.predict()
app = AIApplication(Model())
app.run()
"""

#Challenge 06
"""
class TextModel:
    def predict(self):
        print("Generating text")
class ImageModel:
    def predict(self):
        print("Generating image")

class AIApplication:
    def __init__(self, model):
        self.model = model

    def run(self):
        self.model.predict()

app = AIApplication(TextModel())
app.run()
app1 = AIApplication(ImageModel())
app1.run()
"""

#Challenge 07

"""
class Computer:
    def run_code(self):
        print("Computer code")

class CloudComputer:
    def run_code(self):
        print("Cloude computer code")

class AIEngineer:
    def __init__(self, name, model):
        self.ename = name
        self.emodel = model

    def code(self):
        print(f"Our ai engineer is {self.ename} and he is runnig ") 
        self.emodel.run_code()
computer = Computer()
cloud = CloudComputer()
engineer = AIEngineer("Sayed", computer)
engineer1 = AIEngineer("Alex", cloud)
engineer.code()
engineer1.code()

"""
#Challenge 08
"""
class Model:
    def predict(self):
        print("Model is predicting")

class TextModel(Model):
    def predict(self):
        print("Text model is generating text")

class ImageModel(Model):
    def predict(self):
        print("Image model is generating image")

class Test(Model):
    pass

class AIApplication:
    def __init__(self, model):
        self.model = model

    def run(self):
        self.model.predict()

app = AIApplication(TextModel())
app1 = AIApplication(Model())
app2 = AIApplication(ImageModel())
app3 = AIApplication(Test()) #It will inherite predict form parent method
app.run()
app1.run()
app2.run()
app3.run()

"""


