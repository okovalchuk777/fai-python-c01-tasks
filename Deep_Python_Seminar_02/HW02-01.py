# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

MIN_VALUE = 1
MAX_VALUE = 100000
MAX_COUNTS = 3
HEX = 16

count = 0
num = None
result = ''

while count < MAX_COUNTS:
    num = input(f'Введите целое число в диапазоне от {MIN_VALUE} до {MAX_VALUE} включительно: ')
    if num.isdecimal() and MIN_VALUE <= int(num) <= MAX_VALUE:
        break
    else:
        count += 1
        print(f'Попробуте ввести целое число из диапазона. Осталось {MAX_COUNTS - count} попыток.')
        continue

if count == MAX_COUNTS:
    result = "Вы исчерпали количество попыток для корректного ввода числа. Попробуйте позже."
    quit()

number = int(num)
num = int(num)

while num > 0:
    res = num % HEX

    match res:
        case 10:
            res = 'a'
        case 11:
            res = 'b'
        case 12:
            res = 'c'
        case 13:
            res = 'd'
        case 14:
            res = 'e'
        case 15:
            res = 'f'
        case _:
            res = res

    result = str(res) + result
    num //= HEX

print(f'Наш результат: {result}')
print(f'Проверка с помощью функции hex: {hex(number)}')


