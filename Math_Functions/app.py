import math

print(math.ceil(2.9))
print(math.floor(2.9))

# Print total number of possible combinations
print(math.comb(7, 5))  # 7C5 -> 21
# Returns the remainder of x/y
print(math.fmod(7, 5))  # 2

# compare the closeness of two values
print(math.isclose(1.233, 1.2466))  # false
print(math.isclose(1.233, 1.233))  # true

# Checks whether a number is finite or not
print(math.isinf(3.1416))  # false

# Returns the value of x to the power of y
print(math.pow(3, 2))  # 9.0

print(math.pi)

x = 2.9
print(round(x))  # 3
print(abs(-x))  # 2.9

# check more math module function -->
# https://www.w3schools.com/python/module_math.asp
# https://docs.python.org/3/library/math.html
