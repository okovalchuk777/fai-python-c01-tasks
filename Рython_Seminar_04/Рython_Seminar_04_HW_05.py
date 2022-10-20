# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов.

# How can I break out of multiple loops?
# My first instinct would be to refactor the nested loop into a function and use return to break out.

# функция проверки - есть ли в элементе списка буква
def func_find_isalpha_in_list_el(value):
    for el in value:
        if el.isalpha():
            index = value.index(el)
            return index
    else:
        return None


# функция считывания из файлв первой строки
def first_line_of_file_to_val(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return lines[0]


# эта функция преобразовывает строковый многочлен в словарь, в котором постоянные значения (со степенями) выступают в
# качестве ключа, а коэффициенты являются значениями ключей
def convert_string_polynomial_to_dictionary(string_polynomial):
    a = string_polynomial.replace(' ', '')

    list01 = [a[0]]

    count_el = 0
    for i in a[1:]:
        if i == '-' or i == '+':
            list01.append('')
            count_el += 1
        list01[count_el] += i

    list02 = []
    count_el02 = 0

    for j in list01:
        list03 = list(j)
        index = func_find_isalpha_in_list_el(j)
        if index is None:
            list02.append('')
            list02[count_el02] = [j] + ['']
            count_el02 += 1
        elif index == 0:
            list02.append('')
            list02[count_el02] = ['+1'] + [''.join(list03)]
            count_el02 += 1
        elif index != 0:
            list02.append('')
            list02[count_el02] = [''.join(list03[:index])] + [''.join(list03[index:])]
            count_el02 += 1

    dict01 = {}

    for i in range(len(list02)):
        dict01[list02[i][1]] = list02[i][0]

    for i in dict01:
        if dict01[i] == '+':
            dict01[i] = '+1'
        if dict01[i] == '-':
            dict01[i] = '-1'

    for i in dict01:
        dict01[i] = int(dict01[i])

    return dict01


print(first_line_of_file_to_val('input01.txt'))
x1 = convert_string_polynomial_to_dictionary(first_line_of_file_to_val('input01.txt'))
print(first_line_of_file_to_val('input02.txt'))
x2 = convert_string_polynomial_to_dictionary(first_line_of_file_to_val('input02.txt'))
print(x1)
print(x2)

# суммируем значения у одинаковых ключей
x3 = {i: x1.get(i, 0) + x2.get(i, 0) for i in set(x1).union(x2)}

list04 = []
for i in x3:
    if i == '':
        list04.append(str(x3.get(i)))
    elif x3.get(i) == 1:
        list04.append(i)
    elif x3.get(i) == -1:
        list04.append('-' + i)
    else:
        list04.append(str(x3.get(i)) + i)

list05 = []
for i in list04:
    if i[0] != '-':
        i = '+' + i
        list05.append(i)
    else:
        list05.append(i)

if list05[0][0] == '+':
    list05[0] = list05[0][1:]

string01 = ''.join(list05) + ' = 0'
print(f'Сумма многочленов равна: ', string01)

with open('output2.txt', 'w', encoding='utf-8') as f:
    f.write(string01)
