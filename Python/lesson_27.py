"""
#Challenge 01 Typevar

from typing import TypeVar

T = TypeVar("T")

def get_first(items: list[T]) -> T:
    return items[0]

numbers = [10, 20, 30]
names = ["Sayed", "Alex", "Rahim"]

print(get_first(numbers))
print(get_first(names))

#Challenge 02 Generic

from typing import TypeVar, Generic

U = TypeVar("U")

class Box(Generic[U]):
    def __init__(self, value: U):
        self.value = value

number_box = Box[int](100)
name_box = Box[str]("Sayed")
print(number_box.value)
print(name_box.value)

#Challenge 03 TypeDict

from typing import TypedDict

class AIModel(TypedDict):
    name: str
    version: float
    framework: str
    parameters: int

model1: AIModel = {
    "name": "GPT",
    "version": 5.6,
    "framework": "PyTorch",
    "parameters": 100000000,
}

print(model1["name"])
print(type(model1))

#Challenge 04 Type allias

#Alias Name
User_id = int
Skills = list[str]

user_id: User_id = 23
skills:Skills = ["Python", "Java", "C++"]

#Challenge 05 Callable

from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int)-> int:
    return a * b

def calculate(calc: Callable[[int, int], int], a: int, b: int) -> int:
    return calc(a, b)

print(calculate(add, 3,4))
print(calculate(multiply, 3,4))

#Challenge 06 Literal

from typing import Literal

Enviornment = Literal["development", "staging", "production"]

def deploy(enviornment: Enviornment)-> str:
    return f"Deploying to {enviornment}"

print(deploy("development"))
print(deploy("staging"))
print(deploy("production"))

#Challenge 07 Protocol

from typing import Protocol

class Saveable(Protocol):
    def save(self):
        ...

class Dataclass:
    def save(self) -> None:
        print("Data save to dataclass")

class FileStorage:
    def save(self)-> None:
        print("File save to file storage")

def save_data(storage: Saveable)-> None:
    storage.save()

save_data(Dataclass())
save_data(FileStorage())

#Challenge 08 Type narrowing

def process(value: int | str):
    if isinstance(value, int):
        return value + 10
    else:
        return value.upper()

#Challenge 09

def process1(value: int | str):
    if isinstance(value, int):
        print(value * 2)
    else:
        print(value.upper())

process1(23)

process1("Name")
"""
"""
#Challenge 01

from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

number_box = Box[int](100)
name_box = Box[str]("Sayed")

print(number_box.value)
print(name_box.value)

#Challenge 02
from typing import TypedDict

class AIModel(TypedDict):
    name : str
    version: str
    framework: str
    parameters: int

ModelList = list[AIModel]

models: ModelList = [
     {
        "name": "GPT",
        "version": "5.6",
        "framework": "PyTorch",
        "parameters": 1000000000
    },
    {
        "name": "Llama",
        "version": "3.1",
        "framework": "PyTorch",
        "parameters": 8000000000
    }
]

for model in models:
    print(model["name"])

#Challenge 03

from typing import Literal, Callable

def add(a: int, b: int)->int:
    return a + b

def multiply(a: int, b: int)-> int:
    return a * b

Operation = Literal["Add", "Multiply"]

def calculate(operation: Operation, func: Callable[[int, int], int], a: int, b: int)-> int:
    return func(a, b)

print(calculate("Add", add, 10,15))
print(calculate("Multiply", multiply, 10,15))
# print(calculate("Subtract", add, 10,15)) #Mypy type checker give error

#Challenge 04

from typing import Protocol

class Runable(Protocol):
    def run(self)-> None:
        ...

class Car():
    def run(self)-> None:
        print("Car is running")

class Bike():
    def run(self)-> None:
        print("Bike is runnin")

def execute(obj:Runable):
    return obj.run()

car1 = Car()
bike1 = Bike()

print(execute(car1))
print(execute(bike1))


class Startable(Protocol):
    def start(self):
        ...
    def stop(self):
        ...

class Ship():
    def start(self):
        print("Ship it starting")
    def stop(Self):
        print("Ship is stooped")

class Plane():
    def start(self):
        print("Plane it starting")
    def stop(Self):
        print("Plane is stooped")

def exicute(obj: Startable):
    return obj.start(), obj.stop()


ship1 = Ship()
plane1 = Plane()

exicute(ship1)

#Challenge 05

def process(value: int | str)-> None:
    if isinstance(value, int):
        print (value * 2)
    else:
        print (value.upper())

process(5)
process("Python")

"""
#Challenge 06

from typing import TypedDict

class Model(TypedDict):
    name : str
    version: float
    parameters: int

Models = list[Model]
models: Models = [
    {"name": "GPT",
     "version": 2.3,
     "parameters":200000
     },
    {
    "name": "gemini",
    "version": 4.3,
    "parameters":340000
    }
]

def get_model(models:Models, name: str)-> Model | None:
    for model in models:
        if model["name"] == name:
            return model
    return None

found_model = get_model(models, "GPT")

if found_model is not None:
    print(found_model["name"])
    print(found_model["version"])
else:
    print("Model not found")
