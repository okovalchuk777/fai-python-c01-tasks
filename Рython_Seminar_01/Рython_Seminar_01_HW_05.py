# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#https://stackoverflow.com/questions/28279732/how-to-type-negative-number-with-isdigit # lstrip("-")

import re

a = input("Введите координаты первой точки: ")
b = input("Введите координаты второй точки: ")
a = re.split(';|; |,|, |\.|\. |\*|\n| ', a)
b = re.split(';|; |,|, |\.|\. |\*|\n| ', b)
# print(a)
# print(b)
# if a != ['', ''] and len(a) == 2 and (a[0] != '' or a[0] != '0' or a[1] != '' or a[1] != '0'):
if len(a) == 2 and a[0].lstrip("-").isdigit() is True and a[1].lstrip("-").isdigit() is True and len(b) == 2 and \
        b[0].lstrip("-").isdigit() is True and b[1].lstrip("-").isdigit() is True:
    distance_between_points = ((int(b[1]) - int(a[1])) ** 2 + (int(b[0]) - int(a[0])) ** 2) ** 0.5
    print(f'{distance_between_points:.2f}')
else:
    print(f'Вы неправильно ввели координаты.')
