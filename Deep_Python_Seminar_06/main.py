from sys import argv

from queens import module1, module2

# Terminal = python.exe .\main.py 1,2 5,3 0,7 4,6 3,6 1,5 4,6 7,7

for coord in [*argv[1:]]:
    i, j = coord.split(',')
    module1.board[int(i)][int(j)] = 1

for i in module1.board:
    print(i)

for coord in [*argv[1:]]:
    i, j = coord.split(',')
    print(f'Ферзь на позиции {i},{j} под ударом' if module1.attack(int(i), int(j)) else f'Ферзь на позиции {i},'
                                                                                        f'{j} НЕ под ударом')

print('Возможный вариант размещения 8-ми ферзей представлен ниже')

module2.n_queens(module2.N)
for i in module2.board:
    print(i)
