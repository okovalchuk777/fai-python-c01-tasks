# Теория вероятностей и математическая статистика (семинары)
# Урок 9. Линейная регрессия Логистическая регрессия
#
# Задача 3 (Градиентный спуск с использованием intercept).
# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (С intercept).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

ZP = np.array(zp)
KS = np.array(ks)

n = len(ks)
alpha = 0.000072  # скорость обучения
B0 = 0.1  # стартовый коэффициент B0 (intercept)
B1 = 0.1  # стартовый коэффициент B1

for i in range(1000000):
    B0 -= alpha * (2 / n) * np.sum((B0 + B1 * ZP) - KS)
    B1 -= alpha * (2 / n) * np.sum(((B0 + B1 * ZP) - KS) * ZP)
    KS_pred = B0 + B1 * ZP
    if i % 20000 == 0:
        print(f'Iteration = {i}, B0 = {B0}, B1 = {B1}, mse = {mean_squared_error(KS, KS_pred)}')

# Iteration = 980000, B0 = 444.1773573235816, B1 = 2.620538882408492, mse = 6470.414201176657
# Полученное нами значение mse (намного больше 0) говорит о том. что наша модель, построенная на базе линейной регрессии, не точна и необходимо использовать другие модели анализа данных.
