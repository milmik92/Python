import json

with open('file7.txt', encoding='utf-8') as file_7:
    content = [line.strip() for line in file_7.readlines()]
    content_list = []
    for el in content:
        el = el.split(' ')
        content_list.append(el)
    my_list = sum(content_list, [])
    firms = my_list[::4]
    plus = list(map(float, my_list[2::4]))
    minus = list(map(float, my_list[3::4]))
    profits = []
    for i in range(len(plus)):
        profits.append(plus[i] - minus[i])
    real_profits = []
    for i in range(len(profits)):
        if profits[i] >= 0:
            real_profits.append(profits[i])
    result_list = [dict(zip(firms, profits)), {'average_profit': round(sum(real_profits) / len(real_profits), 2)}]
    print(result_list)

with open('file7.json', 'w') as file_7js:
    json.dump(result_list, file_7js)

    js_str = json.dumps(result_list)
    print(f'JSON-объект: {js_str}')