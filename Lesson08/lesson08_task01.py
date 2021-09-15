class Data:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'{self.data}'

    @classmethod
    def extraction(cls, data):
        data_list = str(data).split('-')
        return f'число месяца = {int(data_list[0])}, номер месяца = {int(data_list[1])}, год = {int(data_list[2])}'

    @staticmethod
    def verification(data):
        data_list = str(data).split('-')
        if 0 < int(data_list[0]) < 32:
            print(f'Число месяца введено корректно.')
        else:
            print(f'Число месяца введено НЕКОРРЕКТНО.')
        if 0 < int(data_list[1]) < 13:
            print(f'Номер месяца введен корректно.')
        else:
            print(f'Номер месяца введен НЕКОРРЕКТНО.')
        if 0 < int(data_list[2]) < 3000:
            print(f'Год введен корректно.')
        else:
            print(f'Год введен НЕКОРРЕКТНО.')


datum = Data('10-12-2021')
print(datum)
print(Data.extraction('10-12-2021'))
datum.verification('10-12-2021')
Data.verification('45-17-3002')
