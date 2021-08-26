"""
Исключения в python. Конструкция try - except для обработки исключений
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-
isklyuchenij.html
"""


def func_number_division(dividend, divisor):
    try:
        div = dividend / divisor
    except ZeroDivisionError:
        print("Деление на ноль недопустимо.")
    else:
        return print(f"Результат деления равен: {div:.5f}")


number01 = float(input("Введите делимое: "))
number02 = float(input("Введите делитель: "))

func_number_division(number01, number02)
