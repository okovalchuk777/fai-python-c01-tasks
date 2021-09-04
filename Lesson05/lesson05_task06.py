input_file = "text_6.txt"
with open(input_file, mode="r", encoding="utf-8") as f_obj:
    line_count = 0
    init_dict = {}
    for line in f_obj:
        init_list = line.split()
        el_sum = 0
        for el in init_list[1:]:
            el_list = [el[i] for i in range(len(el)) if el[i].isdigit()]
            if el_list:
                el_list = int("".join(el_list))
                el_sum += el_list
        subject = init_list[0]
        subject = subject[:-1]
        init_dict.update({subject: el_sum})
        line_count += 1
print(init_dict)
