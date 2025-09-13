# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# Dictionary Comprehension
marks_dict = {name: mark for name, mark in zip(["Alice", "Bob"], [85, 92])}
print(marks_dict)

# Set Comprehension
unique_numbers = {x for x in [1, 2, 2, 3, 4]}
print(unique_numbers)
