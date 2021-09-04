"""
Python Join a list of integers
https://stackoverflow.com/questions/11139330/python-join-a-list-of-integers/11139365
"""

from random import randrange

output_file = "lesson05_05.txt"
with open(output_file, mode="w+", encoding="utf-8") as f_obj:
    random_list = [randrange(0, 1000) for i in range(50)]
    f_obj.write(f'{" ".join(map(str, random_list))}')
    f_obj.seek(0)
    content = f_obj.read()
    print(f'Файл состоит из следующей случайной последовательности чисел:\n{content}')
    f_obj.seek(0)
    for line in f_obj:
        list01 = line.split()
        print(f'Сумма всех чисел в случайной последовательности равна: {sum(map(int, list01))}')



