"""
Запись кириллицы и других не ASCII символов в формате JSON
https://pyneng.github.io/pyneng-3/json-module/
"""
import json

input_file = "text_7.txt"
output_file = "lesson05_07.json"
with open(input_file, mode="r", encoding="utf-8") as f_obj:
    line_count = 0
    profit_firm_count = 0
    el_sum = 0
    init_dict = {}
    for line in f_obj:
        init_list = line.split()
        if int(init_list[2]) > int(init_list[3]):
            profit = int(init_list[2]) - int(init_list[3])
            init_dict.update({init_list[0]: profit})
            el_sum += profit
            profit_firm_count += 1
        elif int(init_list[2]) <= int(init_list[3]):
            profit = int(init_list[2]) - int(init_list[3])
            init_dict.update({init_list[0]: profit})
        line_count += 1
final_list = []
average_dict = {"average_profit": el_sum/profit_firm_count}
final_list.append(init_dict)
final_list.append(average_dict)
print(final_list)

with open(output_file, mode="w+", encoding="utf-8") as output_f_obj:
    json.dump(final_list, output_f_obj, indent=4, ensure_ascii=False)

json_str = json.dumps(final_list, indent=4, ensure_ascii=False)
print(json_str)

