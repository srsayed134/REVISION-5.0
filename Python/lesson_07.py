#Challenge 01
"""
age = 25
if age > 18:
    print("You are an adult")
"""

#Challenge 02
"""
age = int(input("What is your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("Your are a minor")
"""

#Challenge 03
"""
grade = int(input("What is your grade: "))
if grade >= 90:
    print("A+")
elif grade >= 80:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
else:
    print("F")
"""

#Challenge 04
"""
age = 19
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else: 
    print("Access denied")
"""

#Challenge 05
"""
name = ""
if name:
    print("Name exist")
else:
    print("Name is empty") #This #Because name reffered value is false when "", {}, [], 0.0, none, () are reffered something to a variable this variable is always be a falsy
"""

#Challenge 06
"""
score = 95

if score >= 60:
    print("c") #This will be output because first condition is already true
elif score >= 90:
    print("A+")
else:
    print("f")
"""

#Challenge 07
"""
age = int(input("What is your age: "))

if age >= 60:
    print(f"You ticket price is $7 because your age is {age}")
elif age >= 18:
    print(f"Your ticket price is $12 because your age is {age}")
elif age >= 13:
    print(f"You ticket price is $8 because your age is {age}")
elif age >= 5:
    print(f"Your ticket price is $5 because your age is {age}")
else:
    print(f"You don't need any ticket because your age is {age}")
"""