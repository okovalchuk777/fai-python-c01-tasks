# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

frac_01_numerator = ''
frac_01_denominator = ''
frac_02_numerator = ''
frac_02_denominator = ''
frac_numerator_sum = ''
frac_denominator_sum = ''
frac_numerator_mul = ''
frac_denominator_mul = ''
hcf = 1

frac_01 = input(f'Введите первое дробное число в виде a/b, например, 3/4: ')
frac_02 = input(f'Введите второе дробное число в виде a/b, например, 3/4: ')

flag = False
for i in frac_01:
    while i != '/' and flag == False:
        frac_01_numerator += i
        break
    if i == '/':
        flag = True
        continue
    if flag:
        frac_01_denominator += i

flag = False
for i in frac_02:
    while i != '/' and flag == False:
        frac_02_numerator += i
        break
    if i == '/':
        flag = True
        continue
    if flag:
        frac_02_denominator += i

frac_01_numerator = int(frac_01_numerator)
frac_01_denominator = int(frac_01_denominator)
frac_02_numerator = int(frac_02_numerator)
frac_02_denominator = int(frac_02_denominator)

# Сложение дробей

if frac_01_denominator == frac_02_denominator:  # одинаковые знаменатели
    frac_numerator_sum = frac_01_numerator + frac_02_numerator
    frac_denominator_sum = frac_01_denominator
else:  # разные знаменатели - нужно найти наименьшее общее кратное (НОК)
    if frac_01_denominator > frac_02_denominator:
        greater = frac_01_denominator
    else:
        greater = frac_02_denominator
    while (True):
        if ((greater % frac_01_denominator == 0) and (greater % frac_02_denominator == 0)):
            frac_denominator_sum = greater
            break
        greater += 1
    frac_numerator_sum = frac_01_numerator * (int(frac_denominator_sum / frac_01_denominator)) + frac_02_numerator * (
        int(frac_denominator_sum / frac_02_denominator))

# Произведение дробей
frac_numerator_mul = frac_01_numerator * frac_02_numerator
frac_denominator_mul = frac_01_denominator * frac_02_denominator

# Нахождение наибольшего общего делителя (НОД)

# для суммы
if frac_numerator_sum > frac_denominator_sum:
    smaller = frac_denominator_sum
else:
    smaller = frac_numerator_sum
for i in range(1, smaller + 1):
    if ((frac_numerator_sum % i == 0) and (frac_denominator_sum % i == 0)):
        hcf = i

result_sum = f'Сумма дробей (на коленках) равна {str(int(frac_numerator_sum / hcf)) + '/' + str(int(frac_denominator_sum / hcf))}'
result_sum_using_m_fractions = f'Сумма дробей (используя модуль fractions) равна {Fraction(frac_01) + Fraction(frac_02)}'

print(result_sum)
print(result_sum_using_m_fractions)

# для произведения
if frac_numerator_mul > frac_denominator_mul:
    smaller = frac_denominator_mul
else:
    smaller = frac_numerator_mul
for i in range(1, smaller + 1):
    if ((frac_numerator_mul % i == 0) and (frac_denominator_mul % i == 0)):
        hcf = i

result_mul = f'Произведение дробей (на коленках) равно {str(int(frac_numerator_mul/hcf)) + '/' + str(int(frac_denominator_mul/hcf))}'
result_mul_using_m_fractions = f'Произведение дробей (используя модуль fractions) равно {Fraction(frac_01) * Fraction(frac_02)}'

print(result_mul)
print(result_mul_using_m_fractions)