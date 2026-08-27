# Challenge 1
"""
language = "Python"
print(language[0])
print(language[2])
print(language[-1])
sliced_python = language[1:]
print(sliced_python)
print(language)
"""

# Challenge 2
"""
language = "Python"
sliced_python1 = language[0:3]
sliced_python2 = language[2:]
sliced_python3 = language[::-1]
print(sliced_python1)
print(sliced_python2)
print(sliced_python3)
"""

#Challenge 3
"""
text = "   I am learning Python and AI   "
striped_text = text.strip()
uppered_text = striped_text.upper()
replaced_ai= striped_text.replace("AI", "Artificial Intelligence")
"""

#Challenge 4
"""
skills = "Python,SQL,Machine Learning,Deep Learning"
skills_list = skills.split(",")
joinded_list = " | ".join(skills_list)
print(joinded_list)
"""

#Challenge 5
"""
name = "Sayedur Rahman"
age = 25
goal = "AI Engineer"

description = f"My name is {name}, I am {age} years old, My goal is to become an {goal}"
print(description)
"""

#Challenge 6
text = "Pyhon"
print(text[0]) #P
print(text[-1]) #n
print(text[1:4]) #yhon
print(text[::-1]) #nohyP

#Challenge 7
text = "Python"
text2 = text.upper()
print(text) #Python #Because text string is immutable 
print(text2) #PYTHON #Because  modified text is stored in text2 , and original text with string is immutable that is why

