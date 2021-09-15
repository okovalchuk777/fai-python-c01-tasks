"""
Сложение, умножение и деление комплексных чисел. Сопряжённые числа
https://function-x.ru/complex_numbers2.html

Сложение (алгебраическое)
(a1 + a2i) + (b1 + b2i) = (a1 + b1) + (a2 + b2)i
Умножение (алгебраическое)
(a1 + a2i)*(b1 + b2i) = (a1*b1 - a2*b2) + i(a1*b2 + a2*b1)
"""


class ComplexNumbers:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __str__(self):
        return f'Комплексное число: {self.a1} + {self.a2}i'

    def __add__(self, other):
        return (
            f'Результат сложения комплексных чисел будет равен {self.a1 + other.a1} + {self.a2 + other.a2}i.')

    def __mul__(self, other):
        return (
            f'Результат умножения комплексных чисел будет равен {self.a1 * other.a1 - self.a2 * other.a2} + {self.a1 * other.a2 + self.a2 * other.a1}i.')


complex01 = ComplexNumbers(2, 1)
complex02 = ComplexNumbers(3, 4)
print(complex01)
print(complex02)
print(complex01 + complex02)
print(complex01 * complex02)
