#Topic: Creating dictionaries and sets using comprehensions
# 
# # Dictionary comprehension
students = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]
marks_dict = {student: mark for student, mark in zip(students, marks)}
print(marks_dict)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Dictionary comprehension with condition
products = {"apple": 1.2, "banana": 0.8, "orange": 1.5, "milk": 2.5}
cheap_products = {item: price for item, price in products.items() if price < 2.0}
print(cheap_products)  # {'banana': 0.8, 'orange': 1.5}

# Set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # {1, 2, 3, 4, 5}

# Real-world example: Unique cities from employee data
employees = [
    {"name": "Alice", "city": "New York"},
    {"name": "Bob", "city": "Boston"},
    {"name": "Charlie", "city": "New York"},
    {"name": "Diana", "city": "Chicago"}
]
unique_cities = {emp["city"] for emp in employees}
print(unique_cities)  # {'New York', 'Boston', 'Chicago'}
