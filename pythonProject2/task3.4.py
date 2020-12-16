def my_func(x, y):
    if x >= 0 and y < 0 and type(y) is int:
        result = x ** y
        return result
    else:
        return "Введите корректное значение аргументов."


print(my_func(2, -2))


def my_func(x, y):
    while x >= 0 and y < 0:
        if type(y) is int:
            x = 1 / x
            y = -y
            result = 0
            x *= result
            #как повторить действие y - количество раз???=(((

            return (result)
