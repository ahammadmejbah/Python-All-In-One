"""
Enter a positive integer to determine if it is a prime number
"""
from math import sqrt

num = int(input('Please enter a positive integer: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
     if num % x == 0:
         is_prime = False
         break
if is_prime and num != 1:
     print('%d is a prime number' % num)
else:
     print('%d is not a prime number' % num)