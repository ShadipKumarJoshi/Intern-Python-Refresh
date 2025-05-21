# Write a program that uses the math module to calculate square root and power.

import math

#  Square root
num = 2
sqrt = math.sqrt(num)
sqrt = round(sqrt,2)    # 2 decimal
print(f"Square root of {num} is {sqrt}")

#  Power 

num1 = 3
exponent = 4
power = math.pow(num1, exponent)
print(f'{num1} to the power of {exponent} is {power}')