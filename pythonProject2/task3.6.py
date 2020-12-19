def int_func():
    my_list = input("Напишите строку из слов, написанных латинскими буквами в нижнем регистре: ").split()
    for el in my_list:
        my_len = 0
        for symbol in el:
            if 97 <= ord(symbol) <= 122:
                my_len += 1
        print(el.title() if my_len == len(el) else "Введите слово корректно.")


int_func()