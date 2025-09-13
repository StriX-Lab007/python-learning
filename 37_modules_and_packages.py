#Import Technique
# 
# # Approach 1: Import entire module
import math
print(math.sqrt(16))

# Approach 2: Import with alias
import math as m
print(m.gcd(10, 5))

# Approach 3: Import specific functions
from math import sqrt, gcd
print(sqrt(16))

# Approach 4: Import with function alias
from math import sqrt as sq
print(sq(25))

# Approach 5: Import everything (not recommended)
from math import *
print(factorial(5))
