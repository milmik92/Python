import re

with open('file6.txt', encoding='utf-8') as file_6:
    content = [line.strip() for line in file_6.readlines()]
    subjects = []
    mini_content = []
    for el in content:
        mini_list = el.split(': ')
        subjects.append(mini_list[0])
        mini_content.append(mini_list[1])
    my_list = []
    for el in mini_content:
        numbers = re.findall('\d+', el)
        my_list.append(numbers)
    result_list = []
    for el in my_list:
        result = sum(map(int, el))
        result_list.append(result)
    my_dict = dict(zip(subjects, result_list))
    print(my_dict)
