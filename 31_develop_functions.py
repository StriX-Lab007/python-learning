# approach1.py
# INPUT: Takes inputs from function calls (outside)
# PROCESS: Process the input inside the function body
# OUTPUT: Function returns result to the caller (outside)

def sumop(a, b):
    # 'a' and 'b' are formal parameters
    c = a + b  # 'c' is a local variable
    return c

# Main program
x = int(input("Enter First Value: "))
y = int(input("Enter Second Value: "))
result = sumop(x, y)  # Function call
print("Sum of ({}, {}) is = {}".format(x, y, result))



# approach2.py
# INPUT: Takes inputs inside the function body
# PROCESS: Process inside the function body
# OUTPUT: Prints result inside the function body

def sumop():
    # INPUT
    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))
    # PROCESS
    c = a + b
    # OUTPUT
    print("Sum of ({}, {}) is = {}".format(a, b, c))
    # OR
    # print("Sum of", a, "and", b, "is =", c)

# Main program
sumop()  # Function call


# approach3.py
# INPUT: Takes inputs inside the function body
# PROCESS: Processes inside the function body
# OUTPUT: Returns result to the function call (outside)

def sumop():
    a = float(input("Enter First Value: "))
    b = float(input("Enter Second Value: "))
    c = a + b
    return "Sum of {} and {} = {}".format(a, b, c)

# Main program
result = sumop()  # Function call
print(result)




# approach4.py
# INPUT: Takes inputs from function call (outside)
# PROCESS: Process the input inside the function body
# OUTPUT: Prints the result inside the function body

def sumop(a, b):
    c = a + b
    print("Sum of ({}, {}) is = {}".format(a, b, c))

# Main program
a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))

sumop(a, b)  # Function call
