class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        self.result = int(self.number_of_cells + other.number_of_cells)
        return f'Сумма клеток равна {self.result}.'

    def __sub__(self, other):
        if self.number_of_cells < other.number_of_cells:
            return f'Размер второй клетки не может быть больше размера первой клетки.'
        else:
            self.result = int(self.number_of_cells - other.number_of_cells)
            return f'Результат вычитания клеток равен {self.result}.'

    def __mul__(self, other):
        self.result = int(self.number_of_cells * other.number_of_cells)
        return f'Результат умножения клеток равен {self.result}.'

    def __truediv__(self, other):
        try:
            self.result = int(self.number_of_cells // other.number_of_cells)
        except ZeroDivisionError:
            return f'Размер второй клетки не может быть равен нулю.'
        else:
            return f'Результат деления клеток равен {self.result}.'

    def make_order(self, row, printed_character):
        count = 0
        for i in range(int(self.number_of_cells / row)):
            i += 1
            print(f'{printed_character * row}')
        print(f'{printed_character * (self.number_of_cells % row)}')


cell1 = Cell(24)
cell2 = Cell(17)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell1.make_order(5, '*')
