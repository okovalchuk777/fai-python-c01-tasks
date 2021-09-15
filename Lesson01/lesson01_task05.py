revenue = int(input("Enter a revenue in US dollars: "))  # выручка
costs = int(input("Enter costs in US dollars: "))  # издержки

if revenue > costs:
    print(f'Profit is {revenue - costs} in US dollars')  # прибыль
    print(f'Profitability is {(revenue - costs)/revenue:.2f}')  # рентабельность
    number_employees = int(input("Enter a number of employees: "))  # численность сотрудников фирмы
    print(f'Company profit per employee is {(revenue - costs)/number_employees:.2f} in US dollars')
elif costs > revenue:
    print(f'Loss is {costs - revenue} in US dollars')  # убыток
else:
    print(f'Profit is 0 in US dollars')  # нулевая прибыль
