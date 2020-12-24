with open('file4.txt', encoding='utf-8') as file_4:
    content = [line.strip() for line in file_4.readlines()]
    keys = []
    values = []
    for el in content:
        mini_list = el.split(' - ')
        keys.append(mini_list[0])
        values.append(mini_list[1])
    orig_dict = dict(zip(keys, values))
    my_dict = {'Один': 'One', 'Два': 'Two', 'Три': 'Three', 'Четыре': 'Four'}

    #что-то я в тупике









