# 1. Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

n = int(input('Введите значение округления числа пи от 1 до 10: '))
print (round(math.pi, n))
