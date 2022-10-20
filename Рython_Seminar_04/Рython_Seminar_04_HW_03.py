#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

import random

# Формирую список случайных чисел с точным дубляжем
list01 = [random.randint(0, 5) for i in range(10)]
list02 = [random.randint(6, 99) for i in range(10)]
list03 = list01 + list02
print(list03)

list04 = []
list05_diplicate = []

for i in list03:
    if i in list04 and i not in list05_diplicate:
        list04.remove(i)
        list05_diplicate.append(i)
    if i not in list04 and i not in list05_diplicate:
        list04.append(i)
print(list04)
