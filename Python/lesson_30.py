"""
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

def hello():
    print("Hello2")

result = decorator(hello)

result()

def greetings(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@greetings
def good_morning():
    print("Good morning")

good_morning()

from functools import wraps
def repeat(times):
    def calc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                print("Before")
                result = func(*args, **kwargs)
                print("After")
            return result
        return wrapper
    return calc


@repeat(4)
def sum(a, b):
    return a + b

print(sum(6,7))

#Final challenge 1

from functools import wraps
import time
def require_login(func):
    @wraps(func)
    def wrapper(is_logged_in, *args, **kwargs):
            print("Before")
            before_time = time.perf_counter()
            if not is_logged_in:
                print("Access denied")
                result = None
            else:
                result = func(*args, **kwargs)
            after_time = time.perf_counter()
            time_spent = after_time - before_time
            print(f"{time_spent:.6f}")
            print("After")
            return result
    return wrapper

@require_login
def calc(a, b):
    return a + b

result = calc(True, 6, 7)
print(result)
result1 = calc(False, 7, 8)
print(result1)
"""

#Final challenge 02

from functools import wraps
import time

def require_login(func):
    def wrapper(is_logged_in, *args, **kwargs):
        print("Before")
        if not is_logged_in:
            print("Access denied")
            print("After")
            return None
        
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        before_time = time.perf_counter()
        result = func(*args, **kwargs)
        after_time = time.perf_counter()
        time_elapsed = after_time - before_time
        print(time_elapsed)
        return result
    return wrapper

@timer
@require_login
def calculator(a, b):
    return a + b 

result = calculator(False, 6,7)
print(result)




    