# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

from decimal import Decimal

name_list = ['Миша', 'Паша', 'Наташа', 'Гриша']
salary_list = [100000, 70000, 80000, 110000, 150000]
bonus_list = ['5.25%', '3.75%', '10.25%', '15.00%', '7.55%', '17.85%']

dict_gen = {name: round(Decimal(salary) * Decimal(bonus[:-1]) * Decimal(0.01), 2) for name, salary, bonus in zip(
    name_list, salary_list, bonus_list)}

print(dict_gen)
print(dict_gen['Миша'])
