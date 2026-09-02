#Challenge 01

def show_goal():
    print("My goal is to become an AI engineer")

show_goal()

#Challenge 02
def greet(name):
    print(f"Hi {name}")

greet("Sayed")
greet("Nim")

#Challenge 03
def introduction(name, age, country):
    print(f"This is {name} age is {age} from {country}")

introduction("Sayed", 23, "BD")

# Challenge 04
def multiply(a, b):
    multiply = a * b
    return multiply #Return is useful because it can be reuseable in another function or something but print only output the thing

result = multiply(3, 4)
print(result)

#Challenge 05

def greet_user(name= "Nim"):
    print(name)

greet_user()

#Challenge 06
def create_profile(name, age, skills):
    print(name, age, skills)

create_profile(
    age=23,
    skills=["Python", "React", "Golang"],
    name="Sayed"
)

#Challenge 07

def calculate(a, b):
    add_num = a + b
    mult_num = a * b
    devide_num = a / b

    return add_num, mult_num, devide_num

add_num, mult_num, devide_num = calculate(20, 5)
print(add_num, mult_num, devide_num)

#Challenge 08

def total_price(price, quantity):
    total_price = price * quantity
    return total_price

def discounted_percentage(discount):
    discounted_percentage = 1 - discount / 100
    return discounted_percentage

def final_price(total_price, discounted_price):
    total_price = total_price * discounted_price
    return total_price

total_price = total_price(100, 5)
discounted_price = discounted_percentage(50)
final_price = int(final_price(total_price, discounted_price))
print(final_price)
