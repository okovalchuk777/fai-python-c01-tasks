"""
Writing string to a file on a new line every time
https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
"""

output_file = "lesson05_01.txt"
with open(output_file, mode="w+", encoding="utf-8") as f_obj:
    input_string = 'start'
    while bool(str(input_string).split()) is not False:
        input_string = input("Введите данные для записи в файл либо если Вы не хотите вводить данные тогда просто "
                             "ножмите Enter: ")
        if bool(str(input_string).split()) is not False:
            f_obj.write(f'{input_string}\n')

with open(output_file, mode="r", encoding="utf-8") as f_obj:
    data = f_obj.read().rstrip('\n')
    print(data)

with open(output_file, mode="w+", encoding="utf-8") as f_obj:
    f_obj.write(data)
    content = f_obj.read()
    print(content)
