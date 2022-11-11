# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from functools import reduce

n = 35  # выдуманная длина списка

list01 = [round((1 + 1 / n)**n, 3) for n in range(1, n + 1)]
print(list01)

# OLD
# sum_values = 0
# for i in range(n):
#     sum_values += list01[i]

# Refactoring
sum_values = reduce(lambda x, y: x + y, list01)
print(f'Сумма значений элементов последовательности равна: ', round(sum_values, 3))
