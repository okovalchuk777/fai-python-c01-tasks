input_file = "text_3.txt"
with open(input_file, mode="r", encoding="utf-8") as f_obj:
    line_count = 0
    all_persons_list = []
    all_salary_list = []
    persons_with_low_salary_list = []
    for line in f_obj:
        line_count += 1
        init_string = line.split()
        all_persons_list.append(init_string[0])
        all_salary_list.append(float(init_string[1]))
        if float(init_string[1]) < 20000:
            persons_with_low_salary_list.append(init_string[0])
print(f'Ниже представлен список сотрудников с размером зарплаты ниже 20000\n{", ".join(persons_with_low_salary_list)}')
print(f'Средняя зарплата составляет: {sum(all_salary_list)/len(all_persons_list):.2f}')


