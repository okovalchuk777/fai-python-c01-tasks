# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход  определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

initial_amount_of_sweets = 121

print("First Player")
FirstPlayer = input("Specify the Name: ")
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


while initial_amount_of_sweets != 0:
    if who_starts == FirstPlayer:
        n = input_dat(FirstPlayer)
        initial_amount_of_sweets -= n
        p_print(who_starts, n, initial_amount_of_sweets)
    elif who_starts == SecondPlayer:
        n = input_dat(SecondPlayer)
        initial_amount_of_sweets -= n
        p_print(who_starts, n, initial_amount_of_sweets)

    if who_starts == FirstPlayer:
        who_starts = SecondPlayer
    else:
        who_starts = FirstPlayer

list_of_names.remove(who_starts)
print("\nGame Over.\n")
print(" **** " + list_of_names[0] + " won. ****")
