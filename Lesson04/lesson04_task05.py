from functools import reduce


def multiplication(x, y):
    return x * y


print(reduce(multiplication, [el for el in range(100, 1001) if el % 2 == 0]))
