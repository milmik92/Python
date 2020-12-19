from itertools import count
from math import factorial

n = int(input('Введите число n = '))


def fact(n):
    for el in count(1):
        if el > n:
            break
        else:
            yield factorial(el)


generator = fact(n)
print(generator)

for el in fact(n):
    print(el)
