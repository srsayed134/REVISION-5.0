# Challenge 01
"""
languages = ["Python", "Javascript", "React", "Django"]
print(languages[0])
print(languages[2])
print(languages[-1])
print(languages[1:])
"""
#Challenge 02
"""
print(languages[0:2])
print(languages[2:4])
"""
#Challenge 03
"""
skills = ["HTML", "CSS", "JavaScript"]
skills[0] = "Python"
skills.append("React")
skills.insert(2, "TypeScript")
print(skills)
"""
#Challenge 04
"""
languages = ["Python", "JavaScript", "React", "Django"]
languages.remove("JavaScript")
print(languages)
last_item = languages.pop()
print(languages)
print(last_item)
"""

#Challenge 05
"""
skills = ["Python", "SQL", "Machine Learning"]
if "Python" in skills:
    print("Python available")
else:
    print("Python not available")

if "React" in skills:
    print ("React avaiable")
else:
    print("React not avaiable")
"""

#Challenge 06
"""
skills = ["Python", "SQL", "Machine Learning", "Deep Learning"]

for language in skills:
    print(f"I am learning {language}")
"""
#Challenge 07
"""
numbers = [10, 20, 30, 40]

for number in range(len(numbers)):
    numbers[number] = numbers[number] * 2

print(numbers) 
"""
skills1 = ["Python", "SQL"]
skills2 = skills1

skills2.append("AI")
print(skills1) 
print(skills2) #Both skills 1 and 2 same because both refered as same list
