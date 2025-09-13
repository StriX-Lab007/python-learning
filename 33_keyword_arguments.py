''' 
Keyword Arguments
Key Points:
Function is defined with positional parameters.
While calling, we can pass arguments as parameter=value pairs.
Order of arguments does not matter when using keyword arguments.
Positional arguments must come before keyword arguments in a function call.

'''


# Example : -Keyword Arguments


# kwd_arguments.py

def dispempinfo(eno, ename, sal, dsg):
    print("{}\t{}\t{}\t{}".format(eno, ename, sal, dsg))

# Main program
print("-" * 50)
print("EmpNo\tName\tSalary\tDesignation")
print("-" * 50)

# Function calls
dispempinfo(111, "RS", 5.6, "SE")  # All positional
dispempinfo(112, "DR", dsg="TL", sal=6.7)  # Mix of positional and keyword
dispempinfo(sal=3.4, dsg="SE", eno=113, ename="TR")  # All keyword
dispempinfo(114, sal=4.4, dsg="TR", ename="JG")  # Positional + keyword

# Below will cause an error because positional argument comes after keyword argument
# dispempinfo(sal=2.4, dsg="TR", ename="MC", 115)

print("-" * 50)


# Example Variable Lenght Arguments


# vip.py

def ck(*names):
    for n in names:
        print("Hello, {}".format(n))

# Function calls
ck("Hyderabad", "Secundrabad")  # 2 Args
ck("Chennai")                   # 1 Arg
ck("Village", "Town", "City")   # 3 Args


