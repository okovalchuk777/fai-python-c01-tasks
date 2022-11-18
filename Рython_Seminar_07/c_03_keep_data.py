# 3) хранение данных
# хранение - словарь
# ключ - id
# value {'name': 'firstname', 'surname': 'lastname' etc}
# Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона (может быть несколько).

import json
import os
from pathlib import Path
import g_07_view_data as g

id_counter_file = 'id_counter.txt'  # файл для отслеживания занятого идентификатора
dict_phone_file = 'dict_phone.json'  # файл постоянного хранения данных телефонного спавочника


# функция для внесения новых данных в файл постоянного хранения данных телефонного справочника
def keep_data(list_value):
    with open(id_counter_file, 'r', encoding='utf-8') as f01:
        data = f01.read().rstrip('\n')
    fle = Path(dict_phone_file)  # проверка существует ли такой файл (если файла нет - то он будет создан)
    fle.touch(exist_ok=True)  # проверка существует ли такой файл (если файла нет - то он будет создан)
    if os.stat(dict_phone_file).st_size == 0:  # если файл пустой
        dict_phone = {int(data): list_value}  # то формируем новый словарь
        g.view_data({int(data): list_value})  # пользователь проверяет что же он внес в ТС
        g.view_data('Данные успешно внесены в телефонный справочник')
        with open(id_counter_file, 'w', encoding='utf-8') as f01:
            f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
        with open(dict_phone_file, 'w', encoding='utf-8') as f02:
            json.dump(dict_phone, f02, indent=4)  # перезаписываем файл данных телефонного справочника
            return dict_phone
    elif os.stat(dict_phone_file).st_size != 0:  # если файл не пустой
        with open(dict_phone_file, 'r', encoding='utf-8') as f02:
            dict_phone = json.load(f02)  # загружаем весь справочник
        dict_phone[int(data)] = list_value  # добавляем новое значение
        g.view_data({int(data): list_value})  # пользователь проверяет что же он внес в ТС
        g.view_data('Данные успешно внесены в телефонный справочник')
        with open(id_counter_file, 'w', encoding='utf-8') as f01:
            f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
        with open(dict_phone_file, 'w', encoding='utf-8') as f02:
            json.dump(dict_phone, f02, indent=4)  # перезаписываем файл данных телефонного справочника
            return dict_phone


if __name__ == "__main__":
    pass
