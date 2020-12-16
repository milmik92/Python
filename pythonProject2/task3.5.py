def my_func():
    my_input = (input("Введите числа, раздеденные пробелом или 'Q' для выхода из программы: ").upper())
    while True:
        if my_input == "Q":
            break

        my_list = my_input.split()
        result = [float(item) for item in my_list]
        return sum(result)


print(my_func())

#вроде написала с while true, а повторный ввод не запрашивает...