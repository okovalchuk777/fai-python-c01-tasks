"""
https://tproger.ru/translations/unicode-and-encoding-python-guide/
латиница нижнего регистра
В таблице ASCII символы сегментированы следующим образом:
от 97 до 122	Буквы английского алфавита в нижнем регистре
"""


def int_func(init_string):
    final_list = []
    for i in init_string:
        final_list.append(i.capitalize())
        y = list(i)
        for k in y:
            # print(ord(k))
            if 97 > ord(k) or ord(k) > 122:
                final_list.remove(i.capitalize())
                break
    return print(" ".join(final_list))


input_string = input("Enter a string of multiple words separated by spaces: ").split()

int_func(input_string)
