def my_func(arg_1, arg_2, arg_3):
    try:
        my_list = [arg_1, arg_2, arg_3]
        sorted_list = sorted(my_list)
        result = sum(sorted_list[1:4])
    except TypeError:
        return "Error"

    return result


print(my_func(1, 2, 3))
