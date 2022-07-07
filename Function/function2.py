"""
Definition and use of functions - finding the greatest common divisor and the least common multiple
"""


def gcd(x, y):
     if x > y:
         (x, y) = (y, x)
     for factor in range(x, 1, -1):
         if x % factor == 0 and y % factor == 0:
             return factor
     return 1


def lcm(x, y):
     return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))