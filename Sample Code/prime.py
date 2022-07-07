"""
Print the prime numbers between 2 and 99
"""

import math

for num in range(2, 100):
     is_prime = True
     for factor in range(2, int(math. sqrt(num)) + 1):
         if num % factor == 0:
             is_prime = False
             break
     if is_prime:
         print(num, end=' ')