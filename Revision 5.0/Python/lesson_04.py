# Operators
"""
# Challenge 1
result1 = 25 + 7 #32
result2 = 25 - 7 #18
result3 = 25 * 7 #175
result4 = 25 / 7 #3.57
result5 = 25 // 7 #3
result6 = 25 % 7 #4
result7 = 25 ** 2 #625
print(result6)
"""
"""
#Challenge 2
age = 25

print(age == 25) #True
print(age != 30) #True
print(age > 18) #True
print(age <18) #False
print(age >= 25) #True
print(age <= 20) #False
"""
"""
#Challenge 3
age = 25
has_id = True

driving_license = age >= 18 and has_id
print(driving_license) #True

student_lab_access = age < 18 or has_id
print(student_lab_access) #True

door_access = not has_id
print(door_access) #False
"""

#Challenge 4
language = "Python"

py_check = "Py"  in language
java_check = "Java" in language
java_check1 = "Java" not in language
print(py_check) #True
print(java_check) #False
print(java_check1) #True

#Challenge 5
x = 10
y = 5

result = (x > y) and (x % 2 == 0) 
result1 = True and True #True
print(result) #True

#Challenge 6

value = None
print(value is None) #True
print(value == None) #True