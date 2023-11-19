# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_COUNTS_ATTEMPTS = 10

count_attempts = 0
result = None


num_generated = randint(LOWER_LIMIT, UPPER_LIMIT)
#print(num_generated)

print(f'Попробуйте за {MAX_COUNTS_ATTEMPTS} попыток отгадать число в диапазоне от {LOWER_LIMIT} до {UPPER_LIMIT} включительно.')

while count_attempts < MAX_COUNTS_ATTEMPTS:
    num_predicted_str = input(f'У Вас осталось {MAX_COUNTS_ATTEMPTS - count_attempts} попыток. Введите предполагаемое число: ')
    if not num_predicted_str.isnumeric():
        count_attempts += 1
        print(f'Вы либо вводите отрицательное число либо символы. Попробуйте ввести положительное число из разрешенного диапазона.')
        continue
    num_predicted = int(num_predicted_str)
    if num_predicted < LOWER_LIMIT or num_predicted > UPPER_LIMIT:
        count_attempts += 1
        print(f'Вы вводите число вне диапазона разрешённых чисел. Попробуйте ввести число из разрешенного диапазона.')
        continue
    elif num_predicted == num_generated:
        print(f'Поздравляем!!! Вы угадали число за {count_attempts + 1} попыток.')
        break
    elif num_predicted < num_generated:
        count_attempts += 1
        print(f'Ваше число МЕНЬШЕ задуманного числа.')
        continue
    elif num_predicted > num_generated:
        count_attempts += 1
        print(f'Ваше число БОЛЬШЕ задуманного числа.')
        continue

if count_attempts == MAX_COUNTS_ATTEMPTS:
    print(f'Вам не удалось отгадать число. Задуманное число было {num_generated}. Игра окончена')
else:
    print('Игра окончена')
