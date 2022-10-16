# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

list01 = [round(random.uniform(0.5, 175.5), 3) for i in range(10)]
print(list01)

list02 = [round((i % 1), 3) for i in list01]
print(list02)

result = max(list02) - min(list02)
print(round(result, 3))
