from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, [number for number in range(100, 1001) if number % 2 == 0]))
