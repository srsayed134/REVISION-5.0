#Challenge 01
"""
class CountDown:
    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
       if self.max_value >= 1:
            value = self.max_value
            self.max_value -= 1
            return value
       raise StopIteration

counter = CountDown(5)

for count in counter:
    print(count)
"""

#Challenge 02
"""

def get_number():
    return int(input("Enter Number: "))

iterator = iter(get_number, 0)

for number in iterator:
    print(number)

"""
#Challenge 03
"""
numbers = [10, 20, 30, 0]
num_iterator = iter(numbers)

def get_number():
    return next(num_iterator)

iterator = iter(get_number, 0)
for number in iterator:
    print(number)

"""
#Challenge 04
"""

numbers = [10,20,30]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

iterator2 = iter(numbers)
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
"""

#Challenge 05

class DataIterator:
    def __init__(self, data):
        self.current_data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.current_data):
            raise StopIteration
        item = self.current_data[self.index]
        self.index += 1
        return item
        

data = ["image_1", "image_2", "image_3", "image_4", "image_5"]

dataset = DataIterator(data)
for item in dataset:
    print(f"Processing {item}")