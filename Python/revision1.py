#Block 1 +++++++++++++++++++++
#Challenge 01
"""
name = input("Enter your name:")
age = int(input("Enter your age: "))
current_year = int(input("Enter current year"))
birth_year = int(input("Enter your birth year"))
age_next_year = current_year - birth_year

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Birth Year: {birth_year}")
print(f"Current Year: {current_year}")
print(f"Age Next Year: {age_next_year + 1}")
"""
#Challenge 02
"""
price = 1200
quantity = 3
discount = 10

total = price * quantity
print(total)
discount_amount = int(total * 10 / 100)
print(discount_amount) 
final_amount = total - discount_amount
print(final_amount)

"""
#Challenge 03
"""
x = 10
y = 3

print(x + y) #13
print(x / y) #3.333
print(x // y) # 3
print(x % y) # 1
print(x ** 2) #100
print(x > y and y > 0) #true
print(x == 10) #true

"""
#Challenge 04
"""
price = "1500"
quantity = "4"

price = int(price) 
quantity = int(quantity)

total = price * quantity
print(total)
"""
"""
#Quiz 1
# / use for divide value
# // use for round the divided value and it remove any 
#Quiz 2
# % return reminder

#Quiz 3
# "==" check equality of values and "=" use for asign value to a reference

#Quiz 4
# type(10) return int

#Quiz 5
# int("25") it make intiger from string and called it type conversion

#Quiz 6
#10 // 3 result of this 3

#Quiz 7 
#10 % 3 result of this 1

#Quiz 8
"""
#Block 2 ++++++++++++++
#Challenge 01
"""

text = "  Python Is Amazing  "

text1 = text.strip()
text2 = text1.lower()
text3 = text2.upper()
print(text3)
text4 = text3.replace("AMAZING", "POWERFUL")
print(text4)
text5 = len(text4)
print(text5)
"""

#Challenge 02
"""

first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()


fullName = first_name + last_name
fullName.split(" ")
fullName.join(".")
print(fullName)
"""

#Challenge 03
"""
sentence = input("Enter a sentence: ")
charecters = len(sentence)
Words = len(sentence.split())
first_char = sentence[0]
last_char = sentence[-1]
Contain_python = "python" in sentence.lower()
print(Contain_python)

"""
#Challenge 04
"""
while True:
    grade = "F"
    score = int(input("Enter your schore: (can't be greater 100 or -number)"))
    if score > 100 or score < 0:
        print("Invelid schore cant be negative or bigger than 100")
        break
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "c"
    elif score > 60:
        grade = "D"
    else:
        score 
    print(f"Your schore is = {score}")
    print(f"Your grade is {grade}")
    break
"""

#Challenge 05
"""
stored_username = "Sayed"
stored_password  = 12345678

check_username = input("Enter your username: ")
check_password = int(input("Enter your password: "))

if stored_username == check_username and stored_password == check_password:
    print("Login successful")
else:
    print("Login successful")
"""

#Challenge 05.1
"""

stored_username = "Sayed"
stored_password  = 12345678

check_username = input("Enter your username: ")
check_password = int(input("Enter your password: "))

if stored_username == check_username:
    if stored_password == check_password:
        print("You can enter")
    else:
        print("Your password incorrect")
else:
    print("Your username is incorrect")

"""
#Challenge 06
"""
input = int(input("Enter your number: "))

if input > 0:
    print(f"{input} is positive number")
elif input < 0:
    print(f"{input} is a negative number")
elif input == 0:
    print(f"{input} is zero")

if input % 2 == 0:
    print(f"{input} is even number")
else: 
    print(f"{input} is an odd number")

if input > 100:
    print(f"{input} is greater than 100")
"""

#Challenge 07
"""
from1 = 1
to = 20

while True:
    print(from1)
    if from1 == to:
        break
    from1 += 1
"""
#Challenge 07.1
"""

from1 = 1
to = 20

while True:
    if from1 % 2 == 0:
        print(from1)

    if from1 == 20:
        break

    from1 += 1

"""
#Challenge 07.2
"""

from1 = 1
to = 20

while True:
    print(to)
    if to == from1:
        break
    to -= 1
"""
#Challenge 8
"""

while True:
    numbers = []
    while True:
        a_number = int(input("Enter a number: (type '0' to stop programme)"))
        if 0 == a_number:
         break
        numbers.append(a_number)

    total_sum = 0
    for number in numbers:
        total_sum += number

    average = total_sum / (len(numbers) - 1)
    print(total_sum)
    print(average)
    print(len(numbers))
    break
"""

#Quiz1
#lower() make everything small leter uppoer() make every string to capitalize title() make only first string capitalize
#Quiz2
#strip() remove whitespache on both side lstrip() left side rstrip() right side

#Quiz3
#True because python is case sensetive
#False ''

#Quiz 4
# "=" is use for assign value to reference, "==" identify quality, "!=" idintify not equality

#Qyiz 5
# "if" is taking condition it condition is true then "if" goes to "elif" if there is another condition to explore truty of false and finally "else" not take any condition it gives result all the time what is default to do

#Quiz 6
#it will print from 1 to 5 last is exculde

#Quiz 7
#it will print from 2 to 11 is exculded after 2 step

#Quiz 8
#break meanse stop the loop and continue means run the loop although need to stop

#Block 3

#Challenge 01
"""
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
numbers.append(60)
print(numbers)
numbers.remove(20)
print(numbers)
numbers[1] = 35
print(numbers)
print(len(numbers))
check_40 = 40 in numbers
print(check_40)
"""

#Challenge 02
"""
numbers = [5, 12, 7, 20, 3, 18, 10]

for number in numbers:
    print(number)
"""
"""

for number in numbers:
    if number > 10:
        print(number)
"""
"""

total_number = 0
for number in numbers:
    total_number += number
print(total_number)

average = total_number / len(numbers)
print(average)
"""
"""

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)
"""
"""

smallest_number = numbers[0]

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print(smallest_number)
"""
#Challenge 03
"""

student = ("Sayed", 25, "Python", "Bangladesh")
print(student[0])
print(student[1])
print(student[-1])
print(len(student))
print("Python" in student)
# student[0] = "Md. Sayed"
print(student) #Error because tuple is unchangeable
"""

#Challenge 04
"""
skills = {"Python", "JavaScript", "Python", "React", "SQL"}
print(skills)
skills.add("Django")
print(skills)
skills.remove("JavaScript")
print(skills)
print("Python" in skills)

backend = {"Python", "Django", "SQL", "Node"}
frontend = {"JavaScript", "React", "HTML", "CSS"}

print(backend.union(frontend))
print(backend.intersection(frontend))
print(backend.difference(frontend))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))
"""
#Challenge 05
"""

student = {
    "name": "Sayed",
    "age": 25,
    "country": "Bangladesh",
    "skills": ["Python", "JavaScript"]
}
print(student["name"])
print(student["skills"])
student["skills"].append("React")
print(student)
student["email"] = "sayed@example.com"
print(student)
student["age"] = 26
print(student["age"])
print("age" in student)
print(student.get("country"))

for key in student.keys():
    print(key)

for value in student.values():
    print(value)
"""

#Challenge06
"""

users = [
    {"name": "Sayed", "age": 25, "role": "Developer"},
    {"name": "Rahim", "age": 30, "role": "Designer"},
    {"name": "Karim", "age": 22, "role": "Developer"},
]
for user_name in users:
    print(user_name["name"])

for user_role in users:
    if user_role["role"] == "Developer":
        print(user_role["name"])


total_age = 0
for user_age in users:
    total_age += user_age["age"]

avarage_age = total_age / len(users) 
print(avarage_age)

oldest_user = users[0]["age"]
for user in users:
    if user["age"] > oldest_user:
        oldest_user = user["age"]

print(oldest_user)

new_user = []
for user in users:
    if user["role"] == "Developer":
        new_user.append(user)

print(new_user)
"""

#Challenge 07
"""
def claculate_funtion(price, quantity):
    return price * quantity

total = claculate_funtion(1200, 3)
print(total)

def calculate_discount(total, discount_percent = 0):
    discount =  total * discount_percent / 100
    return total - discount

print(calculate_discount(total, 10))
"""

#Challenge 08
"""
numbers = [10, 20, 5, 30, 15]

def analyze_numbers(numbers):
    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number

    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    counts_of_number = len(numbers)

    return total, average, largest_number, smallest_number, counts_of_number

total, average, largest_number, smallest_number, counts_of_number =analyze_numbers(numbers)
print(total)
print(average)
print(largest_number)
print(smallest_number)
print(counts_of_number)
"""

#Quiz1
#numbers[0] means first value of list,tupple ,  numbers[-1] is last value, numbers [1:4] from second position of value to thirt position 4 is exclude

#Quiz2
#append() add a single element to the very end of list
#insert(index, item) insert and item at specific position of list, and shifting subsequent items to the right
#extend() add all element from iterable like(list, tuple, set)

#Quiz3 numbers = [1, 2, 3] numbers[0] = 100 this change the index position to 100 so [100, 2, 3] student = ("Sayed", 25) student[0] = "Rahim" cant posiblle because tupple is immutable

#Quiz4 list, tuple, set difference is list is mutable, organise, can have duplicates items, tuple is immutable can have multipe items, set is mutable but unorder, cant have multiple items but you can add value, update value, remove value 

#Quiz5 skills is set and set cant have multiple same value

#Quiz6 student["email"] can return error if there has no email key but student.get("email") will return none it prevent crash from error

#Quiz7 for key in student: if you want corresponding value you need [] this but for key, value in student.items(): already give keys and values

#Quiz8 def add(a, b): return a + b it return value where is called and print(a + b) give output instant when called

#Quiz9 def greet(name="Sayed"): if paranmeter have no value default argument is Sayed when greet("Rahim") call have value default argument will not use as argument in funtion 

#Quiz10 def calculate(a, b):
    #total = a + b
    #return total

#result = calculate(10, 20)

#print(result) #30

#Block 4
#Challenge 01
"""
name = "Sayed"

def show_name():
    global name
    print(name)

show_name() #function name is reciving name from its local scpope
print(name) #This name is from global scope name

show_name() #Sayed because we use global before name

"""
#Challenge 02
"""
def calculate_total(*numbers):
    total_number = 0
    for number in numbers:
        total_number += number
    return total_number

def find_largest(*numbers):
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


print(calculate_total(10, 20))
print(calculate_total(10, 20, 30, 40))
print(calculate_total(5, 10, 15, 20, 25))

print(find_largest(5, 10, 15, 20, 25))
"""
#Challenge 03
"""
def show_profile(**details):
    for key, values in details.items():
        print(key, values)

def create_user(**details):
    keys = []
    values = []
    for key, value in details.items():
        keys.append(key)
        values.append(value)
    return keys, values
        

show_profile(
    name = "Sayed",
    age = 24,
    country= "Bangladesh",
    profession= "Developer"
)
print(create_user(
    name = "Sayed",
    age = 24,
    country= "Bangladesh",
    profession= "Developer"))
"""

#Challenge 04
"""
def introduce(name, *skills, **details):
    name = name
    skill = []
    for one_skill in skills:
        skill.append(one_skill)
    print(f"Name: {name}")
    print(f"Skills: {", ".join(skill)}")

    for key, vaule in details.items():
        print(f"{key}: {vaule}")


introduce(
    "Sayed",
    "Python",
    "JavaScript",
    "React",
    age=25,
    country="Bangladesh"
)
"""
#Challenge 05
"""

def devide(a, b):
    return a / b
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result = devide(a, b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Zero cant be enter")
else:
    print(result)
finally:
    print("Division is done")
"""

#Challenge 06
"""

def withdraw(balance, amount):
    if amount <= 0:
        raise ZeroDivisionError
    elif balance <= ammount:
        raise ValueError
    else:
        return balance - amount

try:
    balance = 1000
    ammount = int(input("Enter your ammount: "))
    result = withdraw(balance, ammount)
except ValueError:
    print("Can't process this transection")
except ZeroDivisionError:
    print("Ammount cant be zero or minus")
else:
    print(f"Your balance remain {result}")
finally:
    print("Transection complete")
"""

#Challenge 07
"""

math_tools.py


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


main.py

import math_toots

print(math_toots.add(10, 20))
print(math_toots.divide(20, 10))

from math_toots import add as plus

print(plus(10,30))

"""

#Challenge 08

user1 = {
    "name": "Sayed",
    "age": 25,
    "profession": "developers"
}

user2 = {
    "name": "alex",
    "age": 24,
    "profession": "lawyer"
}

user3 = {
    "name": "robin",
    "age": 26,
    "profession": "developers"
}
user = [user1, user2, user3]
"""
import json
with open("users.json", "w") as file:
    json.dump(user, file, indent=4)

with open("users.json", "r") as file:
    details = json.load(file)
    for detail in details:
        print(detail["name"])

    for detail in details:
        if detail["profession"] == "developers":
            print(detail["name"])
"""
"""

import json
json_user = json.dumps(user)
print(json_user) #This is json string

json_dict = json.loads(json_user)
print(json_dict) #And this is dict from json string

"""

num = 1
while True:
    print(f"#Quiz{num}")
    if num == 10:
        break
    num += 1

#Quiz1 : local can only use in restrict enviornment but global variable can be used use anywhere in the progreem
#Quiz2 dont understand
#Quiz3 it contains tupple from arguments
#Quiz4 it contains dict from arguments
#Quiz5 immutable and mutable
#Quiz6 try is condcut running code except catch error else is if any except does not raise error elss will run and finally is run whether progremm got error or not it will run
#Quiz7 raise return error and print() output value
#Quiz8 import math import everything from math module but from math import sqrt inmport only specific thigs
#Quiz9 to see file is imported to any file or not
#Quiz10 dump is from json export in json file dumps is to referen json as string and load import json file in json formet and loads is import json file as json string



