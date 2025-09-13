# Syntax for Function Definition:
def functionname(param1, param2, ..., param_n):
    # Function body
    # Statements
    return value  # Optional

# Syntax for Function Call:
functionname(arg1, arg2, ..., arg_n)

# Here arg1 → param1, arg2 → param2, etc.
# Number of arguments must match the number of parameters (unless default or variable-length arguments are used).




# Example 1: - Positional Arguments (or Parameters)

# papy.py
# Positional Arguments Example

def dispstuddet(stno, sname, marks):
    print("{}\t{}\t{}".format(stno, sname, marks))

# Main program
print("\n---")
print(" Student Information ")
print("---")
print("StNo\tName\tMarks")
print("---")

dispstuddet(10, "Raju", 34.56)
dispstuddet(20, "Satya", 24.56)
dispstuddet(30, "Chandu", 84.56)

print("---")


# Example 2: - Default Parameters / Arguments

# defaultparam.py
# Example using Default Parameters

def dispstuddet(stno, sname, marks, course="PP", dept="IT"):
    print("{}\t{}\t{}\t{}\t{}".format(stno, sname, marks, course, dept))

# Main program
print("\n---")
print("Student Information:")
print("---")
print("StNo\tName\tMarks\tCourse\tDepartment")
print("---")

dispstuddet(10, "Raju", 34.56)
dispstuddet(20, "Manas", 24.56)
dispstuddet(30, "Hari", 84.56)
dispstuddet(40, "Gopi", 14.56, "Java")
dispstuddet(50, "Roja", 11.56)
dispstuddet(60, "KTR", 14.56, "C", "CSE")
dispstuddet(70, "KCR", 17.56, "DS")

print("---")
