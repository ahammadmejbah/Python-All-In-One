"""
scope problem
"""


# local scope
def foo1():
     a = 5


foo1()
# print(a) # NameError

# global scope
b = 10


def foo2():
     print(b)


foo2()


def foo3():
     b = 100 # local variable
     print(b)


foo3()
print(b)


def foo4():
     global b
     b = 200 # global variable
     print(b)


foo4()
print(b)