def hello():
    print("Hello")
x = hello()

def execute(func):
    func()

execute(hello)

def outer():
    def inner():
        print("Hello")
    return inner

result = outer()
result()

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def 