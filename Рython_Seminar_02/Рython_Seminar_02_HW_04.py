# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = 25  # выдуманная длина списка
filename = 'Python_Seminar_02_file.txt'
number_of_variables_for_multi = 5  # выдуманное количество элементов списка для перемножения

list01 = []
for i in range(n):
    list01.append(random.randint(-n, n))
print(f'Начальный список:\n', list01, sep='')

with open(filename, 'w', encoding='utf-8') as f:
    for i in range(n * 2):
        f.write(str(random.randint(0, n - 1)))
        f.write('\n')

with open(filename, 'r', encoding='utf-8') as f:
    data = f.read().rstrip('\n')

with open(filename, 'w') as f:
    f.write(data)

multi_result = 1
for i in range(number_of_variables_for_multi):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        line_value = random.choice(lines)
        print(line_value)
        multi_result *= list01[int(line_value)]
print(f'Результат перемножения случайно выбранных {number_of_variables_for_multi} элементов', multi_result)

multi_result02 = 1
list02 = [3, 4, 7, 10]
for i in list02:
    with open(filename, 'r', encoding='utf-8') as f:
        #content = f.readlines()
        content = f.read().splitlines()
        print(content[i])
        # print(content[0:3])
        multi_result02 *= list01[int(content[i])]
print(f'Результат перемножения НЕслучайно выбранных элементов', multi_result02)
