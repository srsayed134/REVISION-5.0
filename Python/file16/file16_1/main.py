from test_module1 import name
print(__name__ == "__main__")
print(name) #This is false because test_module1 is imported in main.py