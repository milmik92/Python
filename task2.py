a = int(input('Введите время в секундах: '))
b = a // 3600
c = a % 3600
d = c // 60
f = c % 60
print(f"{b:02}:{d:02}:{f:02}")
