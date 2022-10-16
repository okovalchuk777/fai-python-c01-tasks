# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число в десятичном формате: "))


def decimal_to_bin(num):
    list01 = []
    while num not in [0, 1]:
        remainder = num % 2
        num = num // 2
        list01.append(remainder)
    list01.append(num)
    binary_num = ''.join(map(str, list01[::-1]))
    return binary_num


print(f'Число в двоичном формате: ', '0b' + decimal_to_bin(n))
print(f'Проверка через функцию bin: ', bin(n))
