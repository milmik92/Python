from sys import argv

script_name, name, salary_per_hour, hours, bonus = argv


def salary():
    try:
        result = int(salary_per_hour) * int(hours) + int(bonus)
        print(f'{name} : {result}')
    except ValueError:
        return print('Error')

print(script_name)
print(salary())