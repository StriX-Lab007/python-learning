a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) # True
print(a is b) # False
print(a is c) # True

x = 256
y = 256
print(x is y) # True

x = 257
y = 257
print(x is y) # False
print(x is None) # Correct usage
