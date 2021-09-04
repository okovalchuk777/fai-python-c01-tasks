"""
Подсчет количества слов в каждой строке в текстовом файле с помощью Python (используя str.split)
https://coderoad.ru/40573064/%D0%9F%D0%BE%D0%B4%D1%81%D1%87%D0%B5%D1%82-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0
%B5%D1%81%D1%82%D0%B2%D0%B0-%D1%81%D0%BB%D0%BE%D0%B2-%D0%B2-%D0%BA%D0%B0%D0%B6%D0%B4%D0%BE%D0%B9-%D1%81%D
1%82%D1%80%D0%BE%D0%BA%D0%B5-%D0%B2-%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%BC-%D1%84%D0%B0%D
0%B9%D0%BB%D0%B5-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-Python
"""

input_file = "lesson05_01.txt"
with open(input_file, mode="r", encoding="utf-8") as f_obj:
    line_count = 0
    for line in f_obj:
        line_count += 1
        print(f'В {line_count}-й строке содержится {len(line.split())} слова.')
    print(f'В указанном файле содержится всего {line_count} строк.')

