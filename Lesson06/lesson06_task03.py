class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f'Full name of employee: {self.name} {self.surname}.')

    def get_total_income(self):
        return print(f'Salary including bonuses is {self._income["wage"] + self._income["bonus"]}.')


a = Position('Василь', 'Петров', 'руководитель', 30000, 15000)
a.get_full_name()
a.get_total_income()
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
