from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import json
import os
from pathlib import Path
import hashlib


# Реализованные проверки:
# - незаполненные поля при внесении данных в БД
# - дубликаты записей в БД


id_counter_file = 'id_counter.txt'  # файл для отслеживания занятого идентификатора
dict_enterprise_db_file = 'dict_enterprise_db.json'  # файл постоянного хранения данных предприятия


def func_dict_hash(dictionary):
    """SHA256 hash of a dictionary."""
    dhash = hashlib.sha256()
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


def func_add_record_to_db():
    global win01
    global e_name
    global e_patronymic
    global e_lastname
    global combo_sex
    global combo_dd_birthday
    global combo_mm_birthday
    global combo_yy_birthday
    global combo_departments
    global combo_job_positions
    global e_phone
    global e_salary

    win01 = Toplevel()
    win01.title('Добавление записи в БД')
    win01.geometry('900x380+380+180')
    win01.grab_set()

    file_departments = 'departments.csv'
    file_job_positions = 'job_positions.csv'

    l_name = Label(win01, text="Имя:")
    l_name.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e_name = Entry(win01)
    e_name.grid(row=0, column=1, columnspan=2, padx=10, sticky=W + E)

    l_patronymic = Label(win01, text="Отчество:")
    l_patronymic.grid(row=1, column=0, padx=10, sticky=W)
    e_patronymic = Entry(win01)
    e_patronymic.grid(row=1, column=1, columnspan=2, padx=10, sticky=W + E)

    l_lastname = Label(win01, text="Фамилия:")
    l_lastname.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e_lastname = Entry(win01)
    e_lastname.grid(row=2, column=1, columnspan=2, padx=10, sticky=W + E)

    # How can I disable typing in a ttk.Combobox tkinter
    # You can set the state to "readonly"

    l_sex = Label(win01, text="Пол:")
    l_sex.grid(row=3, column=0, padx=10, sticky=W)
    combo_sex = ttk.Combobox(win01, state="readonly", values=['мужской', 'женский'])
    combo_sex.grid(row=3, column=1, columnspan=2, padx=10, sticky=W + E)

    l_dd_birthday = Label(win01, text="День рождения:")
    l_dd_birthday.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    combo_dd_birthday = ttk.Combobox(win01, state="readonly", values=[str(x) for x in range(1, 32)])
    combo_dd_birthday.grid(row=4, column=1, columnspan=2, padx=10, sticky=W + E)

    l_mm_birthday = Label(win01, text="Месяц рождения:")
    l_mm_birthday.grid(row=4, column=3, padx=10, sticky=W)
    combo_mm_birthday = ttk.Combobox(win01, state="readonly", values=[str(x) for x in range(1, 13)])
    combo_mm_birthday.grid(row=4, column=4, columnspan=2, padx=10, sticky=W + E)

    l_yy_birthday = Label(win01, text="Год рождения:")
    l_yy_birthday.grid(row=4, column=6, padx=10, pady=10, sticky=W)
    combo_yy_birthday = ttk.Combobox(win01, state="readonly", values=[str(x) for x in range(1900, 2023)])
    combo_yy_birthday.grid(row=4, column=7, columnspan=2, padx=10, sticky=W + E)

    l_departments = Label(win01, text="Подразделение:")
    l_departments.grid(row=5, column=0, padx=10, sticky=W)
    with open(file_departments, 'r', encoding='utf-8') as file_dep:
        data_departments = list(csv.reader(file_dep, delimiter=","))
    combo_departments = ttk.Combobox(win01, state="readonly", values=data_departments[0])
    combo_departments.grid(row=5, column=1, columnspan=4, padx=10, sticky=W + E)

    l_job_positions = Label(win01, text="Должность:")
    l_job_positions.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    with open(file_job_positions, 'r', encoding='utf-8') as file_job_pos:
        data_job_positions = list(csv.reader(file_job_pos, delimiter=","))
    combo_job_positions = ttk.Combobox(win01, state="readonly", values=data_job_positions[0])
    combo_job_positions.grid(row=6, column=1, columnspan=4, padx=10, sticky=W + E)

    l_phone = Label(win01, text="Телефон:")
    l_phone.grid(row=7, column=0, padx=10, sticky=W)
    e_phone = Entry(win01)
    e_phone.grid(row=7, column=1, columnspan=4, padx=10, sticky=W + E)
    l_phone_note = Label(win01, text="Примечание: вводите несколько телефонов через запятую (например, 1234567,2345678)")
    l_phone_note.grid(row=8, column=0, columnspan=5, padx=10, sticky=W)

    l_salary = Label(win01, text="ЗАРПЛАТА:")
    l_salary.grid(row=9, column=0, padx=10, sticky=W)
    e_salary = Entry(win01)
    e_salary.grid(row=9, column=1, columnspan=2, padx=10, sticky=W + E)

    btn_add_record_to_db = Button(win01, text="Добавить запись в БД", padx=5, command=func_button_add_record_to_db)
    btn_add_record_to_db.grid(row=11, column=1, columnspan=3, padx=10, pady=30, sticky=W)
    btn_clean01 = Button(win01, text="Очистить данные", padx=5, command=func_button_clean01)
    btn_clean01.grid(row=11, column=4)
    btn_close_window01 = Button(win01, text="Закрыть окно", padx=5, command=func_close_window01)
    btn_close_window01.grid(row=11, column=7, padx=10)


def func_button_add_record_to_db():

    dict01_func_button_add_record_to_db = {
        # не нужно ставить кавычки для ключа иначе будет ошибка
        # if key.get() == '':
        # AttributeError: 'str' object has no attribute 'get'
        e_name: '"Имя"',
        e_patronymic: '"Отчество"',
        e_lastname: '"Фамилия"',
        combo_sex: '"Пол"',
        combo_dd_birthday: '"День рождения"',
        combo_mm_birthday: '"Месяц рождения"',
        combo_yy_birthday: '"Год рождения"',
        combo_departments: '"Подразделение"',
        combo_job_positions: '"Должность"',
        e_phone: '"Телефон"',
        e_salary: '"ЗАРПЛАТА"'
    }

    # for / else В цикле for: блок else выполняется в том случае, если цикл завершил итерацию списка но else не выполняется, если в цикле был выполнен break
    for key, values in dict01_func_button_add_record_to_db.items():
        if key.get() == '':
            # [Tkinter] How to make message box error stay on top of window - use parent
            messagebox.showerror(title='Пустое поле', message=f'Поле {values} пустое. Введите значение.', parent=win01)
            break
    else:
        answer = messagebox.askokcancel(title='Внесение данных в БД',
                                        message='Вы хотите внести эти данные в БД? Вы уверены в правильности данных?', parent=win01)
        if answer:
            dict02_func_button_add_record_to_db = {
                "Имя": e_name.get(),
                "Отчество": e_patronymic.get(),
                "Фамилия": e_lastname.get(),
                "Пол": combo_sex.get(),
                "День рождения": combo_dd_birthday.get(),
                "Месяц рождения": combo_mm_birthday.get(),
                "Год рождения": combo_yy_birthday.get(),
                "Подразделение": combo_departments.get(),
                "Должность": combo_job_positions.get(),
                "Телефон": e_phone.get().split(','),
                "ЗАРПЛАТА": e_salary.get()
            }

            with open(id_counter_file, 'r', encoding='utf-8') as f01:
                data = f01.read().rstrip('\n')
            fle = Path(dict_enterprise_db_file)  # проверка существует ли такой файл (если файла нет - то он будет создан)
            fle.touch(exist_ok=True)  # проверка существует ли такой файл (если файла нет - то он будет создан)
            if os.stat(dict_enterprise_db_file).st_size == 0:  # если файл пустой
                dict_enterprise_db = {int(data): dict02_func_button_add_record_to_db}  # то формируем новый словарь
                messagebox.showinfo(title='Успех', message='Данные успешно внесены в БД.', parent=win01)
                with open(id_counter_file, 'w', encoding='utf-8') as f01:
                    f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
                with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
                    json.dump(dict_enterprise_db, f02, ensure_ascii=False, indent=4)  # перезаписываем файл данных телефонного справочника
                    return dict_enterprise_db
            elif os.stat(dict_enterprise_db_file).st_size != 0:  # если файл не пустой
                with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
                    dict_enterprise_db = json.load(f02)  # загружаем весь справочник
                    # print(dict_enterprise_db)
                # Нахождение одинаковых записей
                # Нахождение hash словаря dict02_func_button_add_record_to_db
                for k, v in dict_enterprise_db.items():
                    if func_dict_hash(dict_enterprise_db[k]) == func_dict_hash(dict02_func_button_add_record_to_db):
                        messagebox.showerror(title='Дубликат', message='Такая запись уже существует!', parent=win01)
                        break
                else:
                    dict_enterprise_db[int(data)] = dict02_func_button_add_record_to_db  # добавляем новое значение
                    messagebox.showinfo(title='Успех', message='Данные успешно внесены в БД.', parent=win01)
                    with open(id_counter_file, 'w', encoding='utf-8') as f01:
                        f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
                    with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
                        json.dump(dict_enterprise_db, f02, ensure_ascii=False, indent=4)  # перезаписываем файл данных телефонного справочника
                        return dict_enterprise_db


def func_button_clean01():
    # # # Проверка что есть в глобальных переменных (не вижу словаря)
    # # pprint(globals())
    # # # <class 'tkinter.Entry'>, <class 'tkinter.Label', <class 'tkinter.ttk.Combobox'>>
    # # Из предыдущей функции func_button_add_record_to_db мы не можем использовать этот словарь так как сейчас эта функция не вызывается и словаря dict01_func_button_clean01 на данный момент вообще не существует

    e_name.delete(0, END)
    e_patronymic.delete(0, END)
    e_lastname.delete(0, END)
    combo_sex.set('')
    combo_dd_birthday.set('')
    combo_mm_birthday.set('')
    combo_yy_birthday.set('')
    combo_departments.set('')
    combo_job_positions.set('')
    e_phone.delete(0, END)
    e_salary.delete(0, END)


def func_close_window01():
    answer = messagebox.askokcancel(title='Закрыть окно', message='Вы действительно хотите закрыть окно?', parent=win01)  # False, False, True
    if answer:
        win01.destroy()
