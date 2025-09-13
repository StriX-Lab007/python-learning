'''
Key Points:
Defined using lambda keyword.
Single-line function (no return keyword needed).
Often used for instant operations.
'''


varname = lambda parameters: expression

# Example 1: Celsius to Fahrenheit
tempconvert = lambda c: 1.8 * c + 32
print("Temp in Fahrenheit =", tempconvert(34))

# Example 2: Multiplication
mulop = lambda a, b: a * b
a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))
print("Mul of ({}, {}) = {}".format(a, b, mulop(a, b)))

# Example 3: Find biggest number
findbig = lambda a, b: a if a > b else b
print("Big number:", findbig(10, 20))

# Example 4: Check even/odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(10))  # Even
print(check_even(7))   # Odd

# Example 5: Lambda in Dictionary
operations = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y
}
print(operations["add"](5, 3))  # 8
print(operations["mul"](5, 3))  # 15



# Sort list of tuples by second value using lambda
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second element:", sorted_pairs)

# Filter even numbers using lambda
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# Map to squares using lambda
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

