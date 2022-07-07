"""
Python's built-in functions
- Math related: abs / divmod / pow / round / min / max / sum
- Sequence correlation: len / range / next / filter / map / sorted / slice / reversed
- Type conversion: chr / ord / str / bool / int / float / complex / bin / oct / hex
- Data structure: dict / list / set / tuple
- Other functions: all / any / id / input / open / print / type

"""


def myfilter(mystr):
     return len(mystr) == 6


# help()
print(chr(0x9a86))
print(hex(ord('Luo')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)