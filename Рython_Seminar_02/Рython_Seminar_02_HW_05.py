# Реализуйте алгоритм перемешивания списка.

import random

n = 25  # выдуманная длина списка
cycles = 777  # сколько циклов перемешивания, можно ставить любое значение:)

list01 = []
for i in range(n):
    list01.append(random.randint(1, 999))
print(f'Начальный список:\n', list01, sep='')

list02 = list01.copy()
for cycle in range(cycles):
    for i in range(n):
        y = random.randint(0, n - 1 - i)
        z = list02.pop(y)
        list02.append(z)
print(f'Перемешанный список:\n', list02, sep='')
