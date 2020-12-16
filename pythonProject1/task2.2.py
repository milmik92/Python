a = list(input('Напишите что-нибудь: ').split( ))
for el in range(1, len(a), 2):
    a[el], a[el + 1] = a[el + 1], a[el]
    print(a)
#не понимаю, в чем ошибка