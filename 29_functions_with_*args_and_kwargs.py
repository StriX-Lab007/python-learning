#Topic: Handling variable-length arguments

def create_profile(name, age, *hobbies, **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Additional Info: {additional_info}")

create_profile("Alice", 25, "reading", "swimming", "coding", city="New York", occupation="Engineer")
