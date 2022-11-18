# 5) поиск данных

import json
import os
from pathlib import Path
import c_03_keep_data as c
import d_04_export_data as d
import g_07_view_data as g


# Функция нахождения данных в словарях словарей :)
def get_key(val, dict_value):
    new_dict = {}
    for key01, value01 in dict_value.items():
        for key02, value02 in value01.items():
            if isinstance(value02, list):  # у нас может храниться несколько телефонных номеров пользователя (список)
                for i in value02:
                    if val == i:
                        new_dict[key01] = value01
            else:
                if val == value02:
                    new_dict[key01] = value01
    if new_dict != {}:
        g.view_data(new_dict)  # вывод пользователю найденной информации
        return new_dict
    else:
        g.view_data("key doesn't exist")  # вывод пользователю найденной информации
        return "key doesn't exist"


# Функция взаимодействия с пользователем по поиску информации в телефонном справочнике
def search_data():
    fle = Path(c.dict_phone_file) # проверка существует ли такой файл (если файла нет - то он будет создан)
    fle.touch(exist_ok=True) # проверка существует ли такой файл (если файла нет - то он будет создан)
    if os.stat(c.dict_phone_file).st_size == 0: # если файл пустой
        g.view_data('Файл телефонного справочника пустой')
    elif os.stat(c.dict_phone_file).st_size != 0:
        with open(c.dict_phone_file, 'r', encoding='utf-8') as f02:
            dict_phone = json.load(f02)
        d.export_data(get_key(input("Введите поисковый запрос: "), dict_phone)) # поиск информации
        print(f'Запрос выполнен. При наличии данных они будут сохранены в файл export_data.txt')


if __name__ == "__main__":
    pass
