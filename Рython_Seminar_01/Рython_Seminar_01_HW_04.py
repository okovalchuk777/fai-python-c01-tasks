# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).
import re

a = input("Введите номер четверти: ")
#print(a)
a = re.split(';|; |,|, |\.|\. |\*|\n| ', a)
#print(a)
if len(a) == 1 and a[0].lstrip("-").isdigit() is True and int(a[0]) in range(1, 5):
    if int(a[0]) == 1:
        print(f'Возможный диапазон координат точек: x > 0, y > 0')
    elif int(a[0]) == 2:
        print(f'Возможный диапазон координат точек: x < 0, y > 0')
    elif int(a[0]) == 3:
        print(f'Возможный диапазон координат точек: x < 0, y < 0')
    elif int(a[0]) == 4:
        print(f'Возможный диапазон координат точек: x > 0, y < 0')
else:
    print(f'Вы неправильно ввели значение четверти.')
