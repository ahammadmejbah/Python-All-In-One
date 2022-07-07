"""
function arguments
- Positional parameters
- variable parameter
- keyword arguments
- named keyword arguments

"""


# parameter default value
def f1(a, b=5, c=10):
     return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# variable parameter
def f2(*args):
     sum = 0
     for num in args:
         sum += num
     return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# keyword arguments
def f3(**kw):
     if 'name' in kw:
         print('Welcome %s!' % kw['name'])
     elif 'tel' in kw:
         print('Your contact number is: %s!' % kw['tel'])
     else:
         print('No personal information found!')


param = {'name': 'Luo Hao', 'age': 38}
f3(**param)
f3(name='Luo Hao', age=38, tel='13866778899')
f3(user='Luo Hao', age=38, tel='13866778899')
f3(user='Luo Hao', age=38, mobile='13866778899')