"""
Enter a non-negative integer n to calculate n!
"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
     result *= x
print('%d! = %d' % (n, result))