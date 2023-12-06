# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

"""
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""

from decimal import Decimal

MULTIPLICITY = 50  # кратность 50
WEALTH_AMOUNT = 5000000  # сумма богатства
WEALTH_TAX = 0.1  # вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
INTEREST_ACCRUAL = 0.03  # после каждой третей операции пополнения или снятия начисляются проценты - 3%
WITHDRAWAL_FEE = 0.015  # Процент за снятие — 1.5% от суммы снятия
WITHDRAWAL_FEE_MIN = 30  # но не менее 30
WITHDRAWAL_FEE_MAX = 600  # и не более 600 у.е.

transactions = 0
actions_list = []


def deposit(balance: Decimal, amount: Decimal) -> Decimal:
    # Пополнение счета
    global transactions, actions_list
    if balance > WEALTH_AMOUNT:
        print(
            f"Так как Вы богатый человек, то пришлось снять с Вас налог в размере {balance * Decimal(WEALTH_TAX):.2f}.")
        actions_list.append(f"Так как Вы богатый человек, то пришлось снять с Вас налог в размере "
                            f"{balance * Decimal(WEALTH_TAX):.2f}.")
        balance -= balance * Decimal(WEALTH_TAX)
    if amount % MULTIPLICITY != 0:
        print("Сумма пополнения должна быть кратной 50 у.е.")
        actions_list.append("Сумма пополнения должна быть кратной 50 у.е.")
        return balance  # Если сумма не кратна 50, возврат без изменения баланса
    balance += amount
    transactions += 1
    print(f"Вы пополнили счет на {amount:.2f} у.е.")
    actions_list.append(f"Вы пополнили счет на {amount:.2f} у.е.")
    return balance


def withdraw(balance: Decimal, amount: Decimal) -> Decimal:
    # Снятие средств
    global transactions, actions_list
    if balance > WEALTH_AMOUNT:
        print(
            f"Так как Вы богатый человек, то пришлось снять с Вас налог в размере {balance * Decimal(WEALTH_TAX):.2f}.")
        actions_list.append(f"Так как Вы богатый человек, то пришлось снять с Вас налог в размере "
                            f"{balance * Decimal(WEALTH_TAX):.2f}.")
        balance -= balance * Decimal(WEALTH_TAX)
    if amount % MULTIPLICITY != 0:
        print("Сумма снятия должна быть кратной 50 у.е.")
        actions_list.append("Сумма снятия должна быть кратной 50 у.е.")
        return balance  # Если сумма не кратна 50, возврат без изменения баланса

    withdrawal_fee = amount * Decimal(WITHDRAWAL_FEE)
    if withdrawal_fee < WITHDRAWAL_FEE_MIN:
        withdrawal_fee = WITHDRAWAL_FEE_MIN
    if withdrawal_fee > WITHDRAWAL_FEE_MAX:
        withdrawal_fee = WITHDRAWAL_FEE_MAX
    if amount + withdrawal_fee > balance:
        print("Недостаточно средств на счете.")
        actions_list.append("Недостаточно средств на счете.")
        return balance  # Если недостаточно средств, возврат без изменения баланса

    balance -= amount + withdrawal_fee
    transactions += 1
    print(f"Вы сняли {amount:.2f} у.е.")
    actions_list.append(f"Вы сняли {amount:.2f} у.е.")
    print(f"Процент за снятие {withdrawal_fee:.2f} у.е.")
    actions_list.append(f"Процент за снятие {withdrawal_fee:.2f} у.е.")
    return balance


def apply_interest(balance: Decimal, num_of_transactions: int) -> Decimal:
    # Начисление процентов
    global actions_list
    if num_of_transactions % 3 == 0:
        interest = Decimal(INTEREST_ACCRUAL) * balance
        balance += interest
        print(f"Начислены проценты: {interest:.2f} у.е.")
        actions_list.append(f"Начислены проценты: {interest:.2f} у.е.")
    return balance


def check_balance(balance: Decimal) -> None:
    # Проверка баланса
    global actions_list
    print(f"Ваш баланс: {balance:.2f} у.е.")
    actions_list.append(f"Ваш баланс: {balance:.2f} у.е.")


def atm_menu():
    global transactions, actions_list
    balance = 0
    actions_list.append(f'Начальный баланс = {balance}')

    while True:
        print("\nМеню банкомата:")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")
        actions_list.append(f'Выбрано действие = {choice}')

        if choice == '1':
            amount = Decimal(input("Введите сумму для пополнения: "))
            actions_list.append(f'Введена сумма для пополнения = {amount}')
            balance = deposit(balance, amount)
            balance = apply_interest(balance, transactions)
            check_balance(balance)
        elif choice == '2':
            amount = Decimal(input("Введите сумму для снятия: "))
            actions_list.append(f'Введена сумма для пополнения = {amount}')
            balance = withdraw(balance, amount)
            balance = apply_interest(balance, transactions)
            check_balance(balance)
        elif choice == '3':
            print("До свидания!")
            actions_list.append("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
            actions_list.append("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    atm_menu()
    print('\n\nВывод действий пользователя:\n')
    for num, action in enumerate(actions_list, 1):
        print(f'{num}. {action}')
