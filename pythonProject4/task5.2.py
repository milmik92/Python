with open('file2.txt', encoding='utf-8') as file_2:
    content = file_2.readlines()
    print(f'Количество строк в файле составляет {len(content)}\n')
    my_list = [len(el.split(' ')) for el in content]
    for i in range(len(my_list)):
        print(f'Количество слов в {i + 1} строке соствляет {my_list[i]}')
