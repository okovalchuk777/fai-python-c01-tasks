# Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/
# wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i), end=' ')
