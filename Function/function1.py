"""
Definition and Use of Functions - Calculating the Combination Number C(7,3)
"""


# Encapsulate the function of factorial into a function
def factorial(n):
     result = 1
     for num in range(1, n + 1):
         result *= num
     return result


print(factorial(7) // factorial(3) // factorial(4))