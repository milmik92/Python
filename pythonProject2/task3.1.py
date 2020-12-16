def division():
    try:
        dividend = float(input("Введите число-делимое: "))
        divisor = float(input("Введите число-делитель: "))
        result = dividend / divisor
    except ZeroDivisionError:
        return "На ноль делить нельзя."

    return round(result, 5)


print(division())
