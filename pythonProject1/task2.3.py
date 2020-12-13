a = int(input('Введите месяц в виде целого числа: '))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
if a in winter:
    print('Winter')
elif a in spring:
    print('Spring')
elif a in summer:
    print('Summer')
else:
    print('Fall')

seasons = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
           9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'}
print(seasons.get(a))
