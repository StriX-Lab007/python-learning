# Basic list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With condition (even numbers only)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Nested loops (flattening a 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Real-world example: Filter students with marks above 50
students = [("Alice", 85), ("Bob", 45), ("Charlie", 92), ("Diana", 38)]
passed_students = [name for name, marks in students if marks > 50]
print(passed_students)  # Output: ['Alice', 'Charlie']
