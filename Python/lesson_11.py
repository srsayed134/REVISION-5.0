#Challenge 01
numbers = {1, 2, 2, 3, 3, 4, 5, 5}
print(numbers) #Some values disappers because set does not support duplicate values

#Challenge 02
skills = {"Python", "SQL", "React"}
skills.remove("React")
print(skills)
skills.discard("Java")
print(skills) #Because discard not raise an error if item was not found

#Challenge 03
skills = {"Python", "SQL", "MAchine learning"}
if "Python" in skills:
    print("Python available")
else:
    print("Python not available")

if "React" in skills:
    print("React available")
else:
    print("React not available")

#Challenge 04
languages = [
    "Python",
    "JavaScript",
    "Python",
    "React",
    "JavaScript",
    "Django"
]
unique_languages = set(languages)
print(unique_languages) #Set is useful because finding and sorting duplicate datas in array or set are very complecated with logic and algorithm

#Challenge 05
frontend = {"HTML", "CSS", "JavaScript"}

backend = {"Python", "SQL", "JavaScript"}

unique_skills = frontend | backend
print(unique_skills)
unique_skills2 = frontend.union(backend)
print(unique_skills2)

#Challenge 06
common_skills = frontend.intersection(backend)
print(common_skills)
common_skills2 = frontend & backend
print(common_skills2)

#Challenge 07
unique_fronend_skills = frontend - backend
unique_backend_skills2 = backend - frontend
print(unique_fronend_skills)
print(unique_backend_skills2)

#Challenge 08
user_ids = [
    101,
    102,
    103,
    101,
    104,
    102,
    105
]

unique_ids = set(user_ids)
print(unique_ids)
print(len(unique_ids))

if 103 in unique_ids:
    print("103 is avaiable")
else:
    print("103 is not avaiable")
