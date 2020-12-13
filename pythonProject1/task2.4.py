a = list(input('Напишите что-нибудь: ').split())
for i, el in enumerate(a):
    el = el[0:10]
    print(i, el)
