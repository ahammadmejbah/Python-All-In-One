"""
Determine whether the input positive integer is a palindrome
A palindrome is a number that arranges a positive integer from left to right and has the same value from right to left

"""

num = int(input('Please enter a positive integer: '))
temp = num
num2 = 0
while temp > 0:
     num2 *= 10
     num2 += temp % 10
     temp //= 10
if num == num2:
     print('%d is a palindrome' % num)
else:
     print('%d is not a palindrome' % num)