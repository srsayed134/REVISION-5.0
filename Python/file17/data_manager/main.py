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