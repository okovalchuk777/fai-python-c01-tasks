# 1. Напишите функцию для транспонирования матрицы

def transposed_matrix_func(array: list[list] | list[tuple] | tuple[list] | tuple[tuple]) -> list[tuple]:
    return list(zip(*array))


list1 = [['a', 'b'], ['c', 'd'], ['e', 'f']]

print(transposed_matrix_func(list1))
