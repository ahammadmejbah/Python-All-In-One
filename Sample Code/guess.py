"""
number guessing game
The computer generates a random number between 1 and 100, which is guessed by humans According to the numbers guessed by the computer, the computer will give a hint of bigger/smaller/guess correctly

"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
     counter += 1
     number = int(input('Please input: '))
     if number < answer:
         print('bigger')
     elif number > answer:
         print('smaller')
     else:
         print('Congratulations on your guess!')
         break
print('You guessed %d times in total' % counter)
if counter > 7:
     print('Your IQ balance is obviously insufficient')