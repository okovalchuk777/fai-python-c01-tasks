# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from numpy.polynomial import Polynomial

k = int(input('Введите степень полинома: '))
list01 = [random.randint(0, 100) for i in range(k)]

p = str(Polynomial(list01)) + ' = 0'
print(p)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(p)
