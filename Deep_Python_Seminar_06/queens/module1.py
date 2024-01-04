# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


__all__ = ['attack']

N = 8

board = [[0] * N for n in range(N)]


def attack(i, j):
    board[i][j] = 0
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            board[i][j] = 1
            return True
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    board[i][j] = 1
                    return True
    board[i][j] = 1
    return False


if __name__ == '__main__':
    pass