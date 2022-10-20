# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))


# функция проверки является ли число простым
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


list01 = []

for y in range(2, (n // 2) + 1):
    if is_prime(y):
        if n % y == 0:
            list01.append(y)
print(list01)
