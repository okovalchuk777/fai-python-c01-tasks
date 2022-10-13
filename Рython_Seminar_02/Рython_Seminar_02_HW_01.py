# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

import re

a = input("Введите число (для дробных чисел в качестве разделителя можете использовать ',', '.', ' '): ")
a = re.split(';|; |,|, |\.|\. |\*|\n| ', a)  # :)

list01 = []
for i in range(len(a)):
    if a[i] == '':
        list01.append(i)
list01 = list01[::-1]
for i in range(len(list01)):
    del a[list01[i]]

total = 0  # total result of addition

if (len(a) == 1 and a[0].lstrip("-").isdigit()) or (len(a) == 2 and a[0].lstrip("-").isdigit() and a[1].lstrip(
        "-").isdigit()):  # :)
    if len(a) == 1:
        for i in range(len(a[0])):
            if a[0][i] == '-':  # a[0] = a[0].lstrip("-")
                continue
            total += int(a[0][i])
    elif len(a) == 2:
        for i in range(len(a[0])):
            if a[0][i] == '-':  # a[0] = a[0].lstrip("-")
                continue
            total += int(a[0][i])
        for i in range(len(a[1])):
            total += int(a[1][i])
else:
    print(f'Вы неправильно ввели значение в качестве числа.')

print(f'Сумма всех цифр равна: ', total)
