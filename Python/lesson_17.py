"""
with open("lesson_17_1.txt", "r") as file:
    print(file.read())

with open("lesson_17_1.txt", "w") as file1:
    file1.write("Python\n")
    file1.write("SQL\n")
    file1.write("React\n")

with open("lesson_17_1.txt", "a") as file2:
    file2.write("Java\n")
    file2.write("JavaScript\n")

with open("lesson_17_1.txt", "r") as file3:
    for line in file3:
        print(line.strip())

with open("file17/user.txt", "r") as file4:
    for line in file4:
        print(line.strip())
"""
"""
import json

user = {
    "name": "Sayedur",
    "age": 25,
    "skills": ["Python", "SQL", "AI"]
}

json_data = json.dumps(user)
print(json_data)
"""
"""

import json

json_data = '{"name": "something", "age": 30}'

dict_data = json.loads(json_data)
print(dict_data["age"])

"""
"""
import json

user = {
    "name": "Sayedur",
    "age": 23,
    "country": "BD",
    "skills": ["Python", "JavaScript", "Java", "SQL"]
}

with open("lesson_17.json", "w") as file:
    json.dump(user, file, indent=4)

import json

with open("lesson_17.json", "r") as file2:
    user = json.load(file2)

print(user["name"])
"""
"""

import json

with open("file17/config.json", "r") as config_file:
    config = json.load(config_file)

print(config["model"])
print(config["learning_rate"])
print(config["epochs"])
print(config["batch_size"])

import csv

with open("lesson_17.csv", "r") as csv_file:
    user = csv.reader(csv_file)
    for row in user:
        print(row)
"""

#Challenge 01
"""
with open("file17/skills.txt", "w") as file:
    file.write("Python\n")
    file.write("SQL\n")
    file.write("Machine Learning\n")
    file.write("Deep Learning\n")
"""

#Challenge 02
"""
with open("file17/skills.txt", "r") as file:
    for skill in file:
        print(skill.strip())
"""
#Challenge 03
"""
with open("file17/skills.txt", "a") as file:
    file.write("Aritificial Intelligence")
"""
#Challenge 04

import json

user = {
    "name": "Sayedur",
    "age": 25,
    "country": "Bangladesh",
    "skills": ["Python", "SQL", "AI"]
}

json_user = json.dumps(user)
print(json_user)

dic_user = json.loads(json_user)
print(dic_user)

#Challenge 05

import json

with open("file17/user.json", "w") as file:
    json.dump(dic_user, file, indent=4)

with open("file17/user.json", "r") as file1:
    user = json.load(file1)
    print(user["name"])
    print(user["age"])
    print(user["country"])
    print(user["skills"])
    print(user)

#Challenge 06

user["goal"] = "AI Engineer"

with open("file17/user.json", "w") as file2:
    json.dump(user, file2, indent=4)

with open("file17/user.json", "r") as file3:
    user = json.load(file3)
    print(user)

#Challenge 07

#main.py
import json

user1 = {
    "name": "Sayedur",
    "age": 25,
    "skills": ["Python", "SQL"]
}
user2 = {
    "name": "Alex",
    "age": 23,
    "skills": ["Java", "Kotlin"]
}
user3 = {
    "name": "Dimitri",
    "age": 20,
    "skills": ["JavaScript", "React"]
}
user = [user1, user2, user3]


with open("users.json", "w") as file:
    json.dump(user, file, indent=4)

with open("users.json", "r") as file:
    users = json.load(file)
    for user in users:
        print(user["name"])
        print(user["age"])
        print(user["skills"])

#users.json
[
    {
        "name": "Sayedur",
        "age": 25,
        "skills": [
            "Python",
            "SQL"
        ]
    },
    {
        "name": "Alex",
        "age": 23,
        "skills": [
            "Java",
            "Kotlin"
        ]
    },
    {
        "name": "Dimitri",
        "age": 20,
        "skills": [
            "JavaScript",
            "React"
        ]
    }
]
#skills.txt