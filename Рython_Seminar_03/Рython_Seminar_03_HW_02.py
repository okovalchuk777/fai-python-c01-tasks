# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Why use enumerate() instead of range() in your python's loops
# https://themeptation.medium.com/why-use-enumerate-instead-of-range-in-your-pythons-loops-d33bfd9c7531
# enumerate() is faster when you want to repeatedly access the list/iterable items at their index.  When you just want
# a list of indices, it is faster to use len() and range().

#Why does append() always return None in Python? [duplicate]
#https://stackoverflow.com/questions/16641119/why-does-append-always-return-none-in-python

import random

n = int(input("Введите число в десятичном формате: "))

list01 = [random.randint(0, 99) for _ in range(n)]
print(list01)


def func_multi():
    list02 = []
    for i in range(len(list01) // 2):
        list02.append(list01[i] * list01[-i - 1])
    return list02


if len(list01) % 2 == 1:
    x = list01.pop(n // 2) ** 2
    print(func_multi() + [x])
else:
    print(func_multi())
