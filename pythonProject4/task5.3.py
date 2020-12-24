with open('file3.txt', encoding='utf-8') as file_3:
    content = [line.strip() for line in file_3.readlines()]
    salary = []
    unlucky = []
    for el in content:
        mini_list = el.split(' - ')
        if float(mini_list[1]) < 20000:
            unlucky.append(mini_list[0])
        salary.append(mini_list[1])
    salary = [float(el) for el in salary]
    print(f'Средняя величина дохода сотрудников составляет {sum(salary) / len(salary)}')
    print(f'Оклад менее 20000 получают сотрудники: {unlucky}')

