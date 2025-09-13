#Topic: Basic functions, arguments, and return

# Function without return
def Add_Two_Values(a, b):
    c = a + b
    print("Sum of Two values is =", c)

x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))
Add_Two_Values(x, y)

# Function with return
def Multiply(a, b):
    c = a * b
    return c

result = Multiply(10, 20)
print("Multiplication result:", result)
