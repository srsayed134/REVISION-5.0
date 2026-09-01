#Challenge 01
"""
person = {
    "name": "Sayedur",
    "age": 25,
    "country": "Bangladesh"
}
print(person["name"])
print(person["age"])
print(person["country"])
"""
#Challenge 02
"""
person["goal"] = "AI Engineer"
person["age"] = 26
print(person)
"""
#Challenge 03
"""
email = person.get("Email")
email2 = person.get("Email", "Email not available")
print(email) #In person reference there is not email key that is why its none
print(email2) #In person reference there is not email and for that reason default value have been printed and it prevent error
"""
#Challenge 04
"""
user = {
    "name": "John",
    "age": 30,
    "country": "USA"
}
poped_age = user.pop("age")
print(poped_age)
print(user)
del user["country"]
print(user)
"""
#Challenge 05

person = {
    "name": "Sayedur",
    "age": 25,
    "country": "Bangladesh"
}
for key,value in person.items():
    print(key, value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

#Challenge 06
person = {
    "name": "Sayedur",
    "age": 25,
    "country": "Bangladesh"
}

if "name" in person.keys():
    print("Name key is available")
else:
    print("Name key is not available")
    
if "Sayedur" in person.values():
    print("Sayedur value is available")
else:
    print("Sayedur value is available")

if person.get("email"):

    print("Email is avilable")
else:
    print("Email is not available")

#Challenge 07
"""
user = {
    "name": "Sayedur",
    "skills": {
        "language": "Python",
        "database": "SQL",
        "field": "AI"
    }
}
pg_language = user["skills"]["language"]
pg_database = user["skills"]["database"]
pg_field = user["skills"]["field"]
print(pg_language)
print(pg_database)
print(pg_field)
"""

#Challenge 08

person = {
   "name": "Sayedur Rahman",
   "age": 22,
   "country": "Bangladesh",
   "skills": ["Pthon", "React", "Javascript"],
   "education": {
       "academic": "Intermediate",
       "courses": ["HTML","CSS","Javascript","React", "Python"]
   } 
}

name = person["name"]
second_skill = person["skills"][1]
qualification = person["education"]["courses"][2]

print(name)
print(second_skill)
print(qualification)