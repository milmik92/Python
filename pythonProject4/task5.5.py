from functools import reduce

try:
    with open("file5.txt", "w", encoding="utf-8") as file_5:
        content = input('Введите набор чисел, разделенных пробелом: \n')
        file_5.writelines(content)
        my_list = content.split(' ')
        numbers = []
        for el in my_list:
            numbers.append(int(el))
        def result(prev_el, el):
            return prev_el + el
        print(reduce(result, numbers))
except IOError as err:
    print(err)