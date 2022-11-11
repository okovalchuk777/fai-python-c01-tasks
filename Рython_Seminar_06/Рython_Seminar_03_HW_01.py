# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
from functools import reduce

n = int(input("Введите число в десятичном формате: "))

list01 = [random.randint(0, 99) for _ in range(n)]
print(list01)

# OLD
# result = 0
# for i in range(len(list01)):
#     if i % 2 != 0:
#         result += list01[i]

# Refactoring
result = reduce(lambda x, y: x + y, [x for x in list01 if list01.index(x)%2 != 0])

print(result)


