# Challenge 1
"""
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Enter valid number")
else:
    print(f"Your age is {age}")
"""
#Challenge 2
"""
try:
    number1 = int(input("Enter number for division: "))
    number2 = int(input("Choose number for divide: "))
    result = number1 / number2

except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Enter a number except zero")
else:
    print(result)
finally:
    print("Calculation done")
"""

#Challenge 3
"""
user = {
    "name": "Sayedur",
    "country": "Bangladesh"
}

try:
    print(user["age"])
except KeyError as error:
    print("In user there have no any age key")
"""

#Challenge 4
"""
skills = ["Python", "SQL", "Machine Learning"]

try:
    print(skills.index("Javascript"))
    print(skills[4])
except ValueError:
    print("There have no value in this index")
except IndexError:
    print("There have no index in this address")
"""

#Challenge 5
"""
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number ,enter valid number")
else:
    print(f"{number}")
finally:
    print("Programme finished")
"""

#Challenge 6
"""
try:
    number = int(input("Enter a number: "))
except ValueError as error:
    print("This a value error")
"""

#Challenge 7
"""
def check_age(age):
    if age < 18:
        raise ValueError(print("You must be atleast 18"))
    else:
        print("Access granted")

try:
    age = int(input("Enter your age:"))
    check_age(age)
except ValueError as error:
    print("This is a value error")
"""

#Challenge 8
"""
def withdraw(balance, ammount):
    try:
        if balance < ammount:
            raise ValueError("Insuficient balance")
            return balance
        elif ammount == 0:
            raise ZeroDivisionError("Ammount cant be zero")
            return balance
        elif balance > ammount & ammount != 0:
            print(f"{ammount} withdraw successful")
            balance = balance - ammount

            return balance
    except ValueError:
        print(f"Insuficient balance, your balance {balance}")
    except ZeroDivisionError:
        print(f"Ammount can not be zero")
    finally:
        print("Bank Service End")    
try:
    balance = withdraw(5000, int(input("Enter your ammount: ")))
except ValueError as error:
    print("Invalid input")
else:
    print(f"Your balance is {balance}")
"""

#Challenge 9

def withdraw(balance, ammount):
    if ammount > balance:
        raise ValueError("Insuficient balance")
    elif ammount == 0:
        raise ZeroDivisionError("Ammount cant be zero")

    return balance - ammount

try: 
    ammount = int(input("Enter your ammount: "))
    net_balance = withdraw(5000, ammount)
except ValueError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print(f"Withdraw successful, Your balance left {net_balance} ")
finally:
    print("Bank service end")