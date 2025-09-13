#Topic: Creating, inserting, updating, and using built-in methods

# Creating empty dictionaries
d1 = {}
d2 = dict()
print(type(d1), type(d2))  # <class 'dict'> <class 'dict'>

# Adding items to an empty dictionary
d1[10] = "Sunday"
d1[100] = 100000
print(d1)  # {10: 'Sunday', 100: 100000}

# Creating non-empty dictionary
d = {10: "Tajmahal", "a": "Apple", 28: "February"}
print(d)  # {10: 'Tajmahal', 'a': 'Apple', 28: 'February'}

# Assignment operation for insertion and update
d["Wl"] = "Welcome to India"
d["a"] = "Amazing Apple"
print(d)

# Using built-in methods
d = {"name": "John", "age": 25, "city": "New York"}
print(d.get("name", "Not Found"))  # John
print(d.get("country", "Not Found"))  # Not Found

d.update({"age": 26, "country": "USA"})
print(d)

city = d.setdefault("city", "Unknown")
state = d.setdefault("state", "California")
print(city, state)
print(d)
