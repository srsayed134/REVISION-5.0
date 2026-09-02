#Challenge 01
def create_message():
    message = "I am learning python"
    print(message)

create_message()
# print(message) #message is a local scope in create_message function 

#Challenge 02
country = "Bangladesh"

def your_contry():
    country = "USA"
    print(country)

your_contry() #USA #This variable shadowing
print(country) #Bangladesh #Because this country variable rom global scope

#Challenge 03

score = 100
def increase_score():
    global score
    score = score + 1
    return score

print(increase_score()) #Use of global keyword make harder test debug code

#Challenge 04

def introduce(name, age, country):
    print(name, age, country)

introduce("Sayed", 22, "BD")
introduce(
    age=23,
    name="Sayed",
    country="UK"
)
#Challenge 05

def calculate_sum(*args):
    total = 0
    for num in args:
        total = total + num
    print(total)

calculate_sum(10,20)
calculate_sum(10,20,30,40)

#Challenge 06

def show_user(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_user(
    name="Sayed",
    age= 23,
    country= "BD",
    goal= "Ba an ai engineer",
)

#Challenge 07
def multiply_by_two(number):
    return number * 2

def add_five(number):
    return number + 5

total = add_five(multiply_by_two(10))
print(total)

#Challenge 08
def create_ai_profile(name, *skills, **details):
    Skills = []
    Details = {}
    for skill in skills:
        Skills.append(skill)
    for key, value in details.items():
        Details[key] = value

    print(f"Name: {name}")
    print(f"Skills: {skills}")
    print(f"Skills_List: {Skills}") #For list
    print(f"Details: {Details}")


create_ai_profile(
    "Sayedur",
    "Python",
    "SQL",
    "Machine Learning",
    country="Bangladesh",
    goal="AI Engineer",
    experience="Beginner"
)