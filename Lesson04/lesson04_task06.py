"""
how to apply BREAK for Itertools count in List Comprehensions?
https://stackoverflow.com/questions/40201847/how-to-apply-break-for-itertools-count-in-list-comprehensions
How to specify where to start in an itertools.cycle function
https://docs.python.org/3/library/itertools.html#itertools.takewhile
https://stackoverflow.com/questions/42459582/how-to-specify-where-to-start-in-an-itertools-cycle-function
https://docs.python.org/3/library/itertools.html#itertools.dropwhile
https://advpyneng.readthedocs.io/ru/latest/book/15_itertools/dropwhile_takewhile.html
"""

from itertools import count, cycle, takewhile, dropwhile

init_number = int(input("Enter a initial number: "))
final_number = int(input("Enter a final number: "))

print(list(takewhile(lambda x: x <= final_number, count(init_number))))

init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
dw = dropwhile(lambda x: x < 3, cycle(init_list))
d = [next(dw) for _ in range(final_number)]
print(d)
