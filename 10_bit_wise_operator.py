x = 10  # Binary: 1010
y = 4   # Binary: 0100

print(x & y)   # 0
print(x | y)   # 14
print(x ^ y)   # 14
print(~x)      # -11
print(x << 1)  # 20
print(x >> 1)  # 5


x = 5
result = x << 2
print(f"Binary of {x}: {bin(x)}")      # 0b101
print(f"After << 2: {bin(result)}")   # 0b10100
print(f"Decimal result: {result}")    # 20

print(3 << 3) # Output: 24

x = 20
result = x >> 2
print(f"Binary of {x}: {bin(x)}")      # 0b10100
print(f"After >> 2: {bin(result)}")    # 0b101
print(f"Decimal result: {result}")     # 5

print(29 >> 2) # Output: 7
