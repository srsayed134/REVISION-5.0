#Challenge 01
languages = ("Python", "JavaScript", "React", "Django")
print(languages[0])
print(languages[2])
print(languages[-1])
print(languages[-2])

#Challenge 02
print(languages[0:2])
print(languages[2:])

#Challenge 03
skills = ("Python", "SQL", "Machine Learning")
# skills[0] = "Java"
print(skills)

#Challenge 04
person = ("Sayedur", 25, "Bangladesh")
name, age, country = person

print(name, age, country)

#Challenge 05
a = 10
b = 20

a, b = b, a
print(a)
print(b)

#Challenge 06
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))
print(numbers.index(30))

#Challenge 07
skills = ("Python", "SQL", "Machine Learning", "Deep Learning")
for skill in skills:
    print(skill)

if "Python" in skills:
    print("Python exist")
else:
    print("Python not available")

if "React" in skills:
    print("React exist")
else:
    print("React not available")

#Challenge 08
coordinates = (10, 20)
coordinates = (30, 40)

print(coordinates) #(30,40) #Because in the variable of coordinates new (30,40) value is reffered