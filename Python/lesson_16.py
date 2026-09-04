#Challenge 01
"""
import math
print(math.sqrt(144))
print(math.pow(2, 5))
"""
#Challenge 02
"""
import random
print(random.randint(1, 100))

#Challenge 03
from datetime import datetime

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
"""
#Challenge 04

"""
import lesson_16_1
print(lesson_16_1.add(20, 10))
print(lesson_16_1.subtract(20, 10))
print(lesson_16_1.multiply(20, 10))
print(lesson_16_1.divide(20, 10))
"""
#Challenge 05
"""
import lesson_16_1

print(lesson_16_1.add(20, 30))
"""

"""
from lesson_16_1 import add

print(add(30,40))
"""
"""
from lesson_16_1 import add as plus

print(plus(50, 70))
"""

# Challenge 06
"""
print(__name__)
name = __name__ == "__main__"
print(name)

from test_module1 import name
print(__name__ == "__main__")
print(name) #This is false because test_module1 is imported in main.py
"""

#Challenge 07
"""
#In lesson1.py file
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    print(greet("Sayedur")) #Return Hello Sayedur
"""
"""
#In lesson2.py file
from lesson1 import greet

greet("Sayed") #Nothing return 
"""


#Bonus_Challenge
#calculator.py
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""
#user.py
"""
def create_user(name, age, country):
    person = {}
    person["name"] = name
    person["age"] = age
    person["country"] = country
    return person
"""
#main.py
"""
from calculator import add, subtract
from user import create_user

user1 = create_user("Alex", 23, "USA")
user2 = create_user("Dimitri", 25, "Russia")
user3 = create_user("Shi jhao", 20, "China")


user1_age_after_two_years = add(user1["age"], 2)
user2_age_after_two_years = add(user2["age"], 2)
user3_age_after_two_years = add(user3["age"], 2)

print(user1_age_after_two_years, user2_age_after_two_years, user3_age_after_two_years)
"""