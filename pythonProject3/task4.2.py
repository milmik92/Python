my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(new_list[1:])
#не додумалась, как по-другому