#Challenge 01
"""
def count_up(max_number):
    for number in range(1, max_number):
        yield number

count1 = count_up(6)

print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))
"""
#Challenge 02
"""
def generate_numbers(max_number):
    for number in range(1, max_number):
        yield number

numbers = generate_numbers(6)
for number in numbers:
    print(number)
"""
#Challenge 03

squares = (
    x**2
    for x in range(1, 11)
    if x % 2 == 0
)

for number in squares:
    print(number)

#Challenge 04
#Generator expression
data = [
    {"name": "Sayed", "score": 85},
    {"name": "Rahim", "score": 45},
    {"name": "Karim", "score": 92},
    {"name": "Hasan", "score": 60},
]

finds = (
    x
    for x in data
    if x["score"] >= 60    
)
for find in finds:
    print(find)

#Generator function

def high_score(data):
    for user in data:
        if user["score"] >= 60:
            yield user

users = high_score(data)
for user in users:
    print(user)

#Challenge 05

predictions = [
    {"model": "GPT", "score": 0.91},
    {"model": "Llama", "score": 0.62},
    {"model": "Gemini", "score": 0.88},
    {"model": "Mistral", "score": 0.45},
    {"model": "Claude", "score": 0.95},
]


def high_confidence(predict_datas):
    poutput = []
    for predict_data in predict_datas:
        if predict_data["score"] >= 0.80:
            poutput.append(predict_data)
    return poutput

poutput = high_confidence(predictions)

for data in poutput:
    print(data)
