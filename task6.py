a = float(input("Введите результат в первый день: "))
b = float(input("Введите желаемый результат: "))
c = 1
while a < b:
    a = a + a * 0.1
    c = c + 1
print(f"Спортсмен достигнет результата на {c} день.")
