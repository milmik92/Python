def anketa(**kwargs):
    for key, value in kwargs.items():
        name = input("Введите ваше имя: ")
        surname = input("Введите вашу фамилию: ")
        year = input("Введите год вашего рождения: ")
        city = input("Введите город вашего проживания: ")
        email = input("Укажите ваш email: ")
        phone = input("Укажите ваш номер телефона: ")
        print(
            f'Вас зовут {name} {surname}, {year} года рождения, город проживания {city}, контактные данные: {email}, {phone}.')
        return value


print(anketa(name="", surname="", year="", city="", email="", phone=""))
