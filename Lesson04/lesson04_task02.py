"""
How to create a list of random integers in python ?
https://moonbooks.org/Articles/How-to-create-a-list-of-random-integers-in-python-/
"""

from random import randrange

init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final_list = [init_list[i] for i in range(1, len(init_list)) if init_list[i] > init_list[i-1]]
print(init_list)
print(final_list)

init_list02 = [randrange(0, 1000) for i in range(20)]
final_list02 = [init_list02[i] for i in range(1, len(init_list02)) if init_list02[i] > init_list02[i-1]]
print(init_list02)
print(final_list02)
