#Challenge 01

name: str = "Sayed"
age: int = 25
height: float = 5.5
is_student: bool= True

print(name, age, height, is_student)

#Challenge 02

def calculate_area(length: float, width: float)-> float:
    return length * width

print(calculate_area(10.5, 5.2))

#Challenge 03

skills:list[str] = ["Python", "Javascript", "React", "SQL"]

def show_skills(language: list[str]) -> None:
    print (language[0])
    print (language[1])
    print (language[2])
    print (language[3])

show_skills(skills)

#Challenge 04

scores: dict[str, int] = {
    "Sayed": 23,
    "Alex": 45,
    "Dimtri": 50
}

def calculate_average(scores: dict[str, int])-> float:
    total: int = 0
    for key, value in scores.items():
        total += value

    average: int = total / len(scores)
    return average

print(calculate_average(scores))

#Challenge 05

user:tuple[str, int] = ("Sayed", 23)
skills:set[str] = {"Python", "React", "Java"}

def user_details(user: tuple[str, int], skills: set[str])-> str: 
    return f"The name of user is {user[0]} and his age is {user[1]} ,he have some skills like {",".join(skills)}"
print(user_details(user, skills))

#Challenge 06

user1:dict[str, str] = {
    "Name": "Sayed",
    "Email": "name@example.com"
}
user2:dict[str, str] = {
    "Name": "Alex",
    "Email": None
}

def users_email(users: list[dict[str, str]])-> str | None:
    for user in users:
        for key, value in user.items():
            if key == "Email":
                print(f"{value}")

users = [user1, user2]
users_email(users)

#Challenge 07

def product_price(price: int | float, vat: int |float)-> float:
    vat_percentage = price * vat / 100
    return price - vat_percentage

print(product_price(200.30, 5.5))

#Challenge 08

def create_ai_config(name: str, version:int | float, framework:str, temp:int | float, token:int)-> dict[str, str | int | float]:
    return{
        "Name": name,
        "Version": version,
        "Framework": framework,
        "Temperature": temp,
        "Max-token": token}

config = create_ai_config(
    "GPT",
    5.6,
    "Transformer",
    0.7,
    1000
)
print(type(config))

#Bonus challenge 

def calculate_token_cost(token:int, price_per_toke: int | float)-> int | float:
    return token * price_per_toke

print(calculate_token_cost(121525, 0.2))

    
