"""
Find all perfect numbers between 1 and 9999
A perfect number is a number whose sum of all factors except itself is exactly equal to the number itself
Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

"""
import math

for num in range(2, 10000):
     result = 0
     for factor in range(1, int(math. sqrt(num)) + 1):
         if num % factor == 0:
             result += factor
             if factor > 1 and num // factor != factor:
                 result += num // factor
     if result == num:
         print(num)