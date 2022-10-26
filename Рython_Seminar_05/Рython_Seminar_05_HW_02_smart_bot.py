# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход  определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

initial_amount_of_sweets = 121
min_number = 1
max_number = 28

# вспомогательный список для умного бота с крайними точками
list_gen01 = [i for i in range(0, initial_amount_of_sweets + 1, max_number + 1)]
print(list_gen01)

FirstPlayer = 'Smart Bot'
print("First Player")
print("My Name`s Smart Bot")
print("\n")

print("Second Player")
SecondPlayer = input("Specify the Name: ")
print("\n")

list_of_names = [FirstPlayer, SecondPlayer]
who_starts = random.choice(list_of_names)
print(f'Starts the player by name: ', who_starts)


def input_dat(name):
    x = int(input(f'How many sweets do you want to take (1 - 28), {name} ?'))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter the correct number of sweets: "))
    return x


def p_print(name, k, value):
    print(f"It was {name}'s turn, he took {k} sweets. Left on the table {value} sweets.")


count = 1
while initial_amount_of_sweets != 0:
    # 1-й случай, когда Smart Bot начинает первым или второй игрок (человек) берет недостаточно конфет до первой
    # критической точки (выигрыш Smart Botу обеспечен)
    if who_starts == FirstPlayer:
        n = initial_amount_of_sweets - list_gen01[-count]
        if 1 <= n <= 28:
            print(f'Smart Bot took {n} sweets.')
            initial_amount_of_sweets -= n
            p_print(who_starts, n, initial_amount_of_sweets)
            count += 1
        # 2-й случай, когда первым начинал второй игрок (человек) и тоже берёт крайние точки (выигрыш человеку
        # обеспечен, если только он будет идти по критическим точкам. Если человек ошибётся - Smart Bot выиграет)
        elif n == 0:
            print(f'Smart Bot says "Ah sly {SecondPlayer}".')
            n = random.randint(1, 28)
            initial_amount_of_sweets -= n
            p_print(who_starts, n, initial_amount_of_sweets)
            count += 1
        # 3-й случай, когда первым начинал второй игрок (человек) и перебрал конфет, т.е. пролетел первую критическую
        # точку (выигрыш Smart Botу обеспечен)
        elif n < 0:
            count += 1
            n = initial_amount_of_sweets - list_gen01[-count]
            if 1 <= n <= 28:
                print(f'Smart Bot took {n} sweets.')
                initial_amount_of_sweets -= n
                p_print(who_starts, n, initial_amount_of_sweets)
                count += 1

    elif who_starts == SecondPlayer:
        n = input_dat(SecondPlayer)
        initial_amount_of_sweets -= n
        p_print(who_starts, n, initial_amount_of_sweets)
        # count += 1

    if who_starts == FirstPlayer:
        who_starts = SecondPlayer
    else:
        who_starts = FirstPlayer

list_of_names.remove(who_starts)
print("\nGame Over.\n")
print(" **** " + list_of_names[0] + " won. ****")
