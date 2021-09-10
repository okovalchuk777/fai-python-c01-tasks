"""
Python Program to Add Two Matrices
https://www.programiz.com/python-programming/examples/add-matrix
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        self.result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                       range(len(self.matrix))]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.result]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


matrix1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
matrix2 = Matrix([[7, 8, 9], [9, 10, 11], [11, 12, 13]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
