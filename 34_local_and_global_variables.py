'''
Local Variables
Defined inside a function.
Accessible only within that function.
Scope and lifetime are limited to that function.
Global Variables
Defined outside any function.
Accessible throughout the entire program.
Can be modified inside a function using the global keyword.
'''

# Global variable
global_variable = value

def function_name():
    # Local variable
    local_variable = value
    
    # Access global variable
    print(global_variable)
    
    # Define new global variable inside function
    global new_global_variable
    new_global_variable = value


# Example: -

# global_local.py

city = "Hyderabad"   # Global
state = "Telangana"  # Global

def student():
    name = input("Enter Student Name: ")  # Local
    course = input("Enter Course: ")      # Local
    print("Student Name:", name)
    print("Course Studying:", course)
    print("City:", city)   # Accessing global
    print("State:", state)

def employee():
    name = input("Enter Employee Name: ")  # Local
    role = input("Enter Employee Role: ")  # Local
    print("Employee Name:", name)
    print("Employee Role:", role)
    print("City:", city)
    print("State:", state)

# Main program
student()
employee()
