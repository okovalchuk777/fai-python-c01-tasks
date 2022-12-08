from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import csv
import json
import os
import a_001_add_record_to_db as a_001

# Реализованы: разные виды поиска, также поиск по диапазону (от до (дни рождения, зарплаты))
# Изменение/удаление записи
# Импорт/экспорт данных в/из БД
# Сохранение результатов поиска в файл

id_counter_file = 'id_counter.txt'  # файл для отслеживания занятого идентификатора
dict_enterprise_db_file = 'dict_enterprise_db.json'  # файл постоянного хранения данных предприятия


def func_search_record_in_db():
    global win02
    global e_name
    global e_patronymic
    global e_lastname
    global combo_sex
    global combo_dd_birthday_from
    global combo_dd_birthday_to
    global combo_mm_birthday_from
    global combo_mm_birthday_to
    global combo_yy_birthday_from
    global combo_yy_birthday_to
    global combo_departments
    global combo_job_positions
    global e_phone
    global e_salary_from
    global e_salary_to

    win02 = Toplevel()
    win02.title('Поиск записи в БД')
    win02.geometry('950x450+330+180')
    win02.grab_set()

    file_departments = 'departments.csv'
    file_job_positions = 'job_positions.csv'

    l_name = Label(win02, text="Имя:")
    l_name.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e_name = Entry(win02)
    e_name.grid(row=0, column=1, columnspan=2, padx=10, sticky=W + E)

    l_patronymic = Label(win02, text="Отчество:")
    l_patronymic.grid(row=1, column=0, padx=10, sticky=W)
    e_patronymic = Entry(win02)
    e_patronymic.grid(row=1, column=1, columnspan=2, padx=10, sticky=W + E)

    l_lastname = Label(win02, text="Фамилия:")
    l_lastname.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e_lastname = Entry(win02)
    e_lastname.grid(row=2, column=1, columnspan=2, padx=10, sticky=W + E)

    # How can I disable typing in a ttk.Combobox tkinter
    # You can set the state to "readonly"

    l_sex = Label(win02, text="Пол:")
    l_sex.grid(row=3, column=0, padx=10, sticky=W)
    combo_sex = ttk.Combobox(win02, state="readonly", values=['мужской', 'женский'])
    combo_sex.grid(row=3, column=1, columnspan=2, padx=10, sticky=W + E)

    l_dd_birthday_from = Label(win02, text="День рождения (от):")
    l_dd_birthday_from.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    combo_dd_birthday_from = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1, 32)])
    combo_dd_birthday_from.grid(row=4, column=1, columnspan=2, padx=10, sticky=W + E)

    l_dd_birthday_to = Label(win02, text="День рождения (до):")
    l_dd_birthday_to.grid(row=5, column=0, padx=10, sticky=W)
    combo_dd_birthday_to = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1, 32)])
    combo_dd_birthday_to.grid(row=5, column=1, columnspan=2, padx=10, sticky=W + E)

    l_mm_birthday_from = Label(win02, text="Месяц рождения (от):")
    l_mm_birthday_from.grid(row=4, column=3, padx=10, sticky=W)
    combo_mm_birthday_from = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1, 13)])
    combo_mm_birthday_from.grid(row=4, column=4, columnspan=2, padx=10, sticky=W + E)

    l_mm_birthday_to = Label(win02, text="Месяц рождения (до):")
    l_mm_birthday_to.grid(row=5, column=3, padx=10, sticky=W)
    combo_mm_birthday_to = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1, 13)])
    combo_mm_birthday_to.grid(row=5, column=4, columnspan=2, padx=10, sticky=W + E)

    l_yy_birthday_from = Label(win02, text="Год рождения (от):")
    l_yy_birthday_from.grid(row=4, column=6, padx=10, sticky=W)
    combo_yy_birthday_from = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1900, 2023)])
    combo_yy_birthday_from.grid(row=4, column=7, columnspan=2, padx=10, sticky=W + E)

    l_yy_birthday_to = Label(win02, text="Год рождения (до):")
    l_yy_birthday_to.grid(row=5, column=6, padx=10, sticky=W)
    combo_yy_birthday_to = ttk.Combobox(win02, state="readonly", values=[str(x) for x in range(1900, 2023)])
    combo_yy_birthday_to.grid(row=5, column=7, columnspan=2, padx=10, sticky=W + E)

    l_departments = Label(win02, text="Подразделение:")
    l_departments.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    with open(file_departments, 'r', encoding='utf-8') as file_dep:
        data_departments = list(csv.reader(file_dep, delimiter=","))
    combo_departments = ttk.Combobox(win02, state="readonly", values=data_departments[0])
    combo_departments.grid(row=6, column=1, columnspan=4, padx=10, sticky=W + E)

    l_job_positions = Label(win02, text="Должность:")
    l_job_positions.grid(row=7, column=0, padx=10, sticky=W)
    with open(file_job_positions, 'r', encoding='utf-8') as file_job_pos:
        data_job_positions = list(csv.reader(file_job_pos, delimiter=","))
    combo_job_positions = ttk.Combobox(win02, state="readonly", values=data_job_positions[0])
    combo_job_positions.grid(row=7, column=1, columnspan=4, padx=10, sticky=W + E)

    l_phone = Label(win02, text="Телефон:")
    l_phone.grid(row=8, column=0, padx=10, pady=10, sticky=W)
    e_phone = Entry(win02)
    e_phone.grid(row=8, column=1, columnspan=4, padx=10, sticky=W + E)

    l_salary_from = Label(win02, text="ЗАРПЛАТА (от):")
    l_salary_from.grid(row=9, column=0, padx=10, sticky=W)
    e_salary_from = Entry(win02)
    e_salary_from.grid(row=9, column=1, columnspan=2, padx=10, sticky=W + E)

    l_salary_to = Label(win02, text="ЗАРПЛАТА (до):")
    l_salary_to.grid(row=10, column=0, padx=10, pady=10, sticky=W)
    e_salary_to = Entry(win02)
    e_salary_to.grid(row=10, column=1, columnspan=2, padx=10, sticky=W + E)

    btn_search_record_in_db = Button(win02, text="Найти запись в БД", padx=5, command=func_button_search_record_in_db)
    btn_search_record_in_db.grid(row=11, column=1, columnspan=3, padx=10, pady=30, sticky=W)
    btn_clean02 = Button(win02, text="Очистить данные", padx=5, command=func_button_clean02)
    btn_clean02.grid(row=11, column=4)
    btn_close_window02 = Button(win02, text="Закрыть окно", padx=5, command=func_close_window02)
    btn_close_window02.grid(row=11, column=7, padx=10)


def func_button_search_record_in_db():
    global dict02_func_search_record_in_db

    dict01_func_search_record_in_db = {
        "Имя": e_name.get(),
        "Отчество": e_patronymic.get(),
        "Фамилия": e_lastname.get(),
        "Пол": combo_sex.get(),
        "День рождения (от)": combo_dd_birthday_from.get(),
        "День рождения (до)": combo_dd_birthday_to.get(),
        "Месяц рождения (от)": combo_mm_birthday_from.get(),
        "Месяц рождения (до)": combo_mm_birthday_to.get(),
        "Год рождения (от)": combo_yy_birthday_from.get(),
        "Год рождения (до)": combo_yy_birthday_to.get(),
        "Подразделение": combo_departments.get(),
        "Должность": combo_job_positions.get(),
        "Телефон": e_phone.get().split(','),
        "ЗАРПЛАТА (от)": e_salary_from.get(),
        "ЗАРПЛАТА (до)": e_salary_to.get()
    }

    list01_func_search_record_in_db = []

    for init_key, init_values in dict01_func_search_record_in_db.items():
        if init_values == '':
            list01_func_search_record_in_db.append(init_key)

    for i in list01_func_search_record_in_db:
        del dict01_func_search_record_in_db[i]

    # ===================================================================
    # "День рождения"
    # ===================================================================
    # 1 variant
    if ("День рождения (от)" in dict01_func_search_record_in_db) and ("День рождения (до)" in dict01_func_search_record_in_db):
        if int(dict01_func_search_record_in_db["День рождения (от)"]) > int(dict01_func_search_record_in_db["День рождения (до)"]):
            messagebox.showerror(title='Неверное значение',
                                 message='Поле "День рождения (от)" не может быть больше поля "День рождения (до)" или наоборот. Введите корректные значения.',
                                 parent=win02)
            return func_button_search_record_in_db
        else:
            dict01_func_search_record_in_db["День рождения"] = tuple(
                (dict01_func_search_record_in_db["День рождения (от)"], dict01_func_search_record_in_db["День рождения (до)"]))
            del dict01_func_search_record_in_db["День рождения (от)"]
            del dict01_func_search_record_in_db["День рождения (до)"]

    # 2 variant
    if ("День рождения (от)" in dict01_func_search_record_in_db) and ("День рождения (до)" not in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "День рождения (до)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db

    # 3 variant
    if ("День рождения (от)" not in dict01_func_search_record_in_db) and ("День рождения (до)" in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "День рождения (от)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db
    # ===================================================================
    # Месяц рождения
    # ===================================================================
    # 1 variant
    if ("Месяц рождения (от)" in dict01_func_search_record_in_db) and ("Месяц рождения (до)" in dict01_func_search_record_in_db):
        if int(dict01_func_search_record_in_db["Месяц рождения (от)"]) > int(dict01_func_search_record_in_db["Месяц рождения (до)"]):
            messagebox.showerror(title='Неверное значение',
                                 message='Поле "Месяц рождения (от)" не может быть больше поля "Месяц рождения (до)" или наоборот. Введите корректные значения.',
                                 parent=win02)
            return func_button_search_record_in_db
        else:
            dict01_func_search_record_in_db["Месяц рождения"] = tuple(
                (dict01_func_search_record_in_db["Месяц рождения (от)"], dict01_func_search_record_in_db["Месяц рождения (до)"]))
            del dict01_func_search_record_in_db["Месяц рождения (от)"]
            del dict01_func_search_record_in_db["Месяц рождения (до)"]

    # 2 variant
    if ("Месяц рождения (от)" in dict01_func_search_record_in_db) and ("Месяц рождения (до)" not in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "Месяц рождения (до)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db

    # 3 variant
    if ("Месяц рождения (от)" not in dict01_func_search_record_in_db) and ("Месяц рождения (до)" in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "Месяц рождения (от)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db
    # ===================================================================
    # Год рождения
    # ===================================================================
    # 1 variant
    if ("Год рождения (от)" in dict01_func_search_record_in_db) and ("Год рождения (до)" in dict01_func_search_record_in_db):
        if int(dict01_func_search_record_in_db["Год рождения (от)"]) > int(dict01_func_search_record_in_db["Год рождения (до)"]):
            messagebox.showerror(title='Неверное значение',
                                 message='Поле "Год рождения (от)" не может быть больше поля "Год рождения (до)" или наоборот. Введите корректные значения.',
                                 parent=win02)
            return func_button_search_record_in_db
        else:
            dict01_func_search_record_in_db["Год рождения"] = tuple(
                (dict01_func_search_record_in_db["Год рождения (от)"], dict01_func_search_record_in_db["Год рождения (до)"]))
            del dict01_func_search_record_in_db["Год рождения (от)"]
            del dict01_func_search_record_in_db["Год рождения (до)"]

    # 2 variant
    if ("Год рождения (от)" in dict01_func_search_record_in_db) and ("Год рождения (до)" not in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "Год рождения (до)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db

    # 3 variant
    if ("Год рождения (от)" not in dict01_func_search_record_in_db) and ("Год рождения (до)" in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "Год рождения (от)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db
    # ===================================================================
    # ЗАРПЛАТА
    # ===================================================================
    # 1 variant
    if ("ЗАРПЛАТА (от)" in dict01_func_search_record_in_db) and ("ЗАРПЛАТА (до)" in dict01_func_search_record_in_db):
        if int(dict01_func_search_record_in_db["ЗАРПЛАТА (от)"]) > int(dict01_func_search_record_in_db["ЗАРПЛАТА (до)"]):
            messagebox.showerror(title='Неверное значение',
                                 message='Поле "ЗАРПЛАТА (от)" не может быть больше поля "ЗАРПЛАТА (до)" или наоборот. Введите корректные значения.',
                                 parent=win02)
            return func_button_search_record_in_db
        else:
            dict01_func_search_record_in_db["ЗАРПЛАТА"] = tuple(
                (dict01_func_search_record_in_db["ЗАРПЛАТА (от)"], dict01_func_search_record_in_db["ЗАРПЛАТА (до)"]))
            del dict01_func_search_record_in_db["ЗАРПЛАТА (от)"]
            del dict01_func_search_record_in_db["ЗАРПЛАТА (до)"]

    # 2 variant
    if ("ЗАРПЛАТА (от)" in dict01_func_search_record_in_db) and ("ЗАРПЛАТА (до)" not in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "ЗАРПЛАТА (до)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db

    # 3 variant
    if ("ЗАРПЛАТА (от)" not in dict01_func_search_record_in_db) and ("ЗАРПЛАТА (до)" in dict01_func_search_record_in_db):
        messagebox.showerror(title='Пустое поле', message='Поле "ЗАРПЛАТА (от)" пустое. Введите значение.', parent=win02)
        return func_button_search_record_in_db
    # ===================================================================

    dict02_func_search_record_in_db = {}

    if os.stat(dict_enterprise_db_file).st_size == 0:  # если файл пустой
        messagebox.showerror(title='Пустая БД', message='Отсутствуют данные в БД', parent=win02)
    elif os.stat(dict_enterprise_db_file).st_size != 0:  # если файл не пустой
        with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
            dict_enterprise_db = json.load(f02)  # загружаем весь справочник
        # Реализуем поиск по запросам в БД
        for key, values in dict_enterprise_db.items():
            # 0 и {}
            for k01, v01 in dict01_func_search_record_in_db.items():
                if isinstance(values[k01], list):
                    count = len(values[k01])
                    for i in values[k01]:
                        if i.count(str(v01[0])) == 0:
                            count -= 1
                    if count == 0:
                        break
                elif isinstance(v01, tuple):
                    if int(values[k01]) not in range(int(v01[0]), int(v01[1]) + 1):
                        break
                elif values[k01].count(str(v01)) == 0:
                    break
            else:
                dict02_func_search_record_in_db[key] = values
        if dict02_func_search_record_in_db == {}:
            messagebox.showwarning(title='Запись отсутствует в БД', message='Подходящие записи не найдены в БД', parent=win02)
        else:
            func_show_search_result(dict02_func_search_record_in_db)
            return dict02_func_search_record_in_db


def func_show_search_result(show_search_result_value):
    global win03
    global combo_search_result
    global dict_show_search_result_value

    dict_show_search_result_value = show_search_result_value.copy()

    win03 = Toplevel()
    win03.title('Результаты поиска в БД')
    win03.geometry('950x450+330+180')
    win03.grab_set()

    list_func_show_search_result01 = [(key, value) for key, value in show_search_result_value.items()]

    l_search_result01 = Label(win03, text=f"Найдено {len(show_search_result_value)} совпадений")
    l_search_result01.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    l_search_result02 = Label(win03, text="Результаты поиска:")
    l_search_result02.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    combo_search_result = ttk.Combobox(win03, state="readonly", values=list_func_show_search_result01)
    combo_search_result.place(x=150, y=50, width=700, height=25)
    combo_search_result.current(0)
    combo_search_result.bind('<<ComboboxSelected>>', func_choose_combo_search_result)
    l_search_result03 = Label(win03, text="Выберите из выпадающего меню значение и откроется окно с подробной информацией")
    l_search_result03.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    btn_save_record_to_file = Button(win03, text="Сохранить все результаты поиска в файл", padx=5, command=func_btn_save_record_to_file)
    btn_save_record_to_file.place(x=350, y=170, width=250, height=25)


def func_choose_combo_search_result(show_search_result_value):
    global win04
    global key_result
    global e_name02
    global e_patronymic02
    global e_lastname02
    global combo_sex02
    global combo_dd_birthday02
    global combo_mm_birthday02
    global combo_yy_birthday02
    global combo_departments02
    global combo_job_positions02
    global e_phone02
    global e_salary02

    file_departments = 'departments.csv'
    file_job_positions = 'job_positions.csv'

    win04 = Toplevel()
    win04.title('Результаты поиска в БД')
    win04.geometry('950x450+330+180')
    win04.grab_set()

    # Получение ключа (идентификатора)
    key_result = (combo_search_result.get().split(' '))[0]

    l_name02 = Label(win04, text="Имя:")
    l_name02.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e_name02 = Entry(win04)
    e_name02.grid(row=0, column=1, columnspan=2, padx=10, sticky=W + E)

    l_patronymic02 = Label(win04, text="Отчество:")
    l_patronymic02.grid(row=1, column=0, padx=10, sticky=W)
    e_patronymic02 = Entry(win04)
    e_patronymic02.grid(row=1, column=1, columnspan=2, padx=10, sticky=W + E)

    l_lastname02 = Label(win04, text="Фамилия:")
    l_lastname02.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e_lastname02 = Entry(win04)
    e_lastname02.grid(row=2, column=1, columnspan=2, padx=10, sticky=W + E)

    # How can I disable typing in a ttk.Combobox tkinter
    # You can set the state to "readonly"

    l_sex02 = Label(win04, text="Пол:")
    l_sex02.grid(row=3, column=0, padx=10, sticky=W)
    combo_sex02 = ttk.Combobox(win04, state="readonly", values=['мужской', 'женский'])
    combo_sex02.grid(row=3, column=1, columnspan=2, padx=10, sticky=W + E)

    l_dd_birthday02 = Label(win04, text="День рождения:")
    l_dd_birthday02.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    combo_dd_birthday02 = ttk.Combobox(win04, state="readonly", values=[str(x) for x in range(1, 32)])
    combo_dd_birthday02.grid(row=4, column=1, columnspan=2, padx=10, sticky=W + E)

    l_mm_birthday02 = Label(win04, text="Месяц рождения:")
    l_mm_birthday02.grid(row=4, column=3, padx=10, sticky=W)
    combo_mm_birthday02 = ttk.Combobox(win04, state="readonly", values=[str(x) for x in range(1, 13)])
    combo_mm_birthday02.grid(row=4, column=4, columnspan=2, padx=10, sticky=W + E)

    l_yy_birthday02 = Label(win04, text="Год рождения:")
    l_yy_birthday02.grid(row=4, column=6, padx=10, pady=10, sticky=W)
    combo_yy_birthday02 = ttk.Combobox(win04, state="readonly", values=[str(x) for x in range(1900, 2023)])
    combo_yy_birthday02.grid(row=4, column=7, columnspan=2, padx=10, sticky=W + E)

    l_departments02 = Label(win04, text="Подразделение:")
    l_departments02.grid(row=5, column=0, padx=10, sticky=W)
    with open(file_departments, 'r', encoding='utf-8') as file_dep:
        data_departments = list(csv.reader(file_dep, delimiter=","))
    combo_departments02 = ttk.Combobox(win04, state="readonly", values=data_departments[0])
    combo_departments02.grid(row=5, column=1, columnspan=4, padx=10, sticky=W + E)

    l_job_positions02 = Label(win04, text="Должность:")
    l_job_positions02.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    with open(file_job_positions, 'r', encoding='utf-8') as file_job_pos:
        data_job_positions = list(csv.reader(file_job_pos, delimiter=","))
    combo_job_positions02 = ttk.Combobox(win04, state="readonly", values=data_job_positions[0])
    combo_job_positions02.grid(row=6, column=1, columnspan=4, padx=10, sticky=W + E)

    l_phone02 = Label(win04, text="Телефон:")
    l_phone02.grid(row=7, column=0, padx=10, sticky=W)
    e_phone02 = Entry(win04)
    e_phone02.grid(row=7, column=1, columnspan=4, padx=10, sticky=W + E)

    l_salary02 = Label(win04, text="ЗАРПЛАТА:")
    l_salary02.grid(row=8, column=0, padx=10, pady=10, sticky=W)
    e_salary02 = Entry(win04)
    e_salary02.grid(row=8, column=1, columnspan=2, padx=10, sticky=W + E)

    with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
        dict_enterprise_db = json.load(f02)  # загружаем весь справочник

    e_name02.insert(0, dict_enterprise_db[key_result].get('Имя'))
    e_patronymic02.insert(0, dict_enterprise_db[key_result].get('Отчество'))
    e_lastname02.insert(0, dict_enterprise_db[key_result].get('Фамилия'))
    combo_sex02.set(dict_enterprise_db[key_result].get('Пол'))
    combo_dd_birthday02.set(dict_enterprise_db[key_result].get('День рождения'))
    combo_mm_birthday02.set(dict_enterprise_db[key_result].get('Месяц рождения'))
    combo_yy_birthday02.set(dict_enterprise_db[key_result].get('Год рождения'))
    combo_departments02.set(dict_enterprise_db[key_result].get('Подразделение'))
    combo_job_positions02.set(dict_enterprise_db[key_result].get('Должность'))
    e_phone02.insert(0, ','.join(dict_enterprise_db[key_result].get('Телефон')))
    e_salary02.insert(0, dict_enterprise_db[key_result].get('ЗАРПЛАТА'))

    btn_edit_record_in_db = Button(win04, text="Сохранить изменения", padx=5, command=func_button_edit_record_in_db)
    btn_edit_record_in_db.grid(row=11, column=1, columnspan=3, padx=10, pady=30, sticky=W)
    btn_delete_record_in_db = Button(win04, text="Удалить запись", padx=5, command=func_delete_record_in_db)
    btn_delete_record_in_db.grid(row=11, column=3)
    btn_save_record_to_file02 = Button(win04, text="Сохранить запись в файл", padx=5, command=func_btn_save_record_to_file02)
    btn_save_record_to_file02.grid(row=11, column=5)
    btn_close_window04 = Button(win04, text="Закрыть окно", padx=5, command=func_close_window04)
    btn_close_window04.grid(row=11, column=7, padx=10)


def func_button_clean02():
    e_name.delete(0, END)
    e_patronymic.delete(0, END)
    e_lastname.delete(0, END)
    combo_sex.set('')
    combo_dd_birthday_from.set('')
    combo_dd_birthday_to.set('')
    combo_mm_birthday_from.set('')
    combo_mm_birthday_to.set('')
    combo_yy_birthday_from.set('')
    combo_yy_birthday_to.set('')
    combo_departments.set('')
    combo_job_positions.set('')
    e_phone.delete(0, END)
    e_salary_from.delete(0, END)
    e_salary_to.delete(0, END)


def func_close_window02():
    answer = messagebox.askokcancel(title='Закрыть окно', message='Вы действительно хотите закрыть окно?', parent=win02)
    if answer:
        win02.destroy()


def func_button_edit_record_in_db():
    dict01_func_button_edit_record_in_db = {
        # не нужно ставить кавычки для ключа иначе будет ошибка
        # if key.get() == '':
        # AttributeError: 'str' object has no attribute 'get'
        e_name02: '"Имя"',
        e_patronymic02: '"Отчество"',
        e_lastname02: '"Фамилия"',
        combo_sex02: '"Пол"',
        combo_dd_birthday02: '"День рождения"',
        combo_mm_birthday02: '"Месяц рождения"',
        combo_yy_birthday02: '"Год рождения"',
        combo_departments02: '"Подразделение"',
        combo_job_positions02: '"Должность"',
        e_phone02: '"Телефон"',
        e_salary02: '"ЗАРПЛАТА"'
    }

    # for / else В цикле for: блок else выполняется в том случае, если цикл завершил итерацию списка но else не выполняется, если в цикле был выполнен break
    for key, values in dict01_func_button_edit_record_in_db.items():
        if key.get() == '':
            # [Tkinter] How to make message box error stay on top of window - use parent
            messagebox.showerror(title='Пустое поле', message=f'Поле {values} пустое. Введите значение.', parent=win04)
            break
    else:
        answer = messagebox.askokcancel(title='Изменение записи', message='Вы действительно хотите изменить запись?', parent=win04)
        if answer:
            dict02_func_button_edit_record_in_db = {
                "Имя": e_name02.get(),
                "Отчество": e_patronymic02.get(),
                "Фамилия": e_lastname02.get(),
                "Пол": combo_sex02.get(),
                "День рождения": combo_dd_birthday02.get(),
                "Месяц рождения": combo_mm_birthday02.get(),
                "Год рождения": combo_yy_birthday02.get(),
                "Подразделение": combo_departments02.get(),
                "Должность": combo_job_positions02.get(),
                "Телефон": e_phone02.get().split(','),
                "ЗАРПЛАТА": e_salary02.get()
            }
            with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
                dict_enterprise_db = json.load(f02)  # загружаем весь справочник
            # Нахождение одинаковых записей
            # Нахождение hash словаря dict02_func_button_add_record_to_db
            for k, v in dict_enterprise_db.items():
                if a_001.func_dict_hash(dict_enterprise_db[k]) == a_001.func_dict_hash(dict02_func_button_edit_record_in_db):
                    messagebox.showerror(title='Дубликат', message='Такая запись уже существует!', parent=win04)
                    break
            else:
                # Удаляем редактируемую запись
                del dict_enterprise_db[key_result]
                dict_enterprise_db[key_result] = dict02_func_button_edit_record_in_db  # добавляем новое значение
                with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
                    json.dump(dict_enterprise_db, f02, ensure_ascii=False, indent=4)  # перезаписываем файл данных телефонного справочника
                messagebox.showinfo(title='Успех', message='Данные успешно внесены в БД.', parent=win04)
                # используем конструкцию try/finally, если нужно что-то сделать после return
                # try:
                #     return func_button_search_record_in_db()
                # finally:
                #     win04.destroy()
                #     win03.destroy()
                win04.destroy()
                win03.destroy()
                return func_button_search_record_in_db()


def func_delete_record_in_db():
    answer = messagebox.askokcancel(title='Удаление записи', message='Вы действительно хотите удалить запись?', parent=win04)
    if answer:
        with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
            dict_enterprise_db = json.load(f02)  # загружаем весь справочник
        del dict_enterprise_db[key_result]
        with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
            json.dump(dict_enterprise_db, f02, ensure_ascii=False, indent=4)  # перезаписываем файл данных телефонного справочника
        messagebox.showinfo(title='Успех', message='Запись удалена в БД.', parent=win04)
        # используем конструкцию try/finally, если нужно что-то сделать после return
        # try:
        #     return func_button_search_record_in_db()
        # finally:
        #     win03.destroy()
        win04.destroy()
        win03.destroy()
        return func_button_search_record_in_db()


def func_close_window04():
    answer = messagebox.askokcancel(title='Закрыть окно', message='Вы действительно хотите закрыть окно?', parent=win04)
    if answer:
        win04.destroy()


def func_btn_save_record_to_file():
    try:
        file_path = filedialog.asksaveasfilename(parent=win03, initialfile='Untitled.json', title='Сохранение файла',
                                                 defaultextension=".json",
                                                 filetypes=(('JSON документы (*.json)', '*.json'), ('Все файлы', '*.*')))
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_show_search_result_value, file, ensure_ascii=False, indent=4)
        messagebox.showinfo(title='Успех', message=f'Все результаты поиска добавлены в файл по пути {file_path}', parent=win03)
    except FileNotFoundError:
        messagebox.showinfo(title='Не выбран файл', message='Вы не указали файл.', parent=win03)


def func_btn_save_record_to_file02():
    try:
        with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f01:
            dict_enterprise_db = json.load(f01)  # загружаем весь справочник
        dict01_func_btn_save_record_to_file02 = {key_result: dict_enterprise_db[key_result]}

        file_path = filedialog.asksaveasfilename(parent=win04, initialfile='Untitled.json', title='Сохранение файла',
                                                 defaultextension=".json",
                                                 filetypes=(('JSON документы (*.json)', '*.json'), ('Все файлы', '*.*')))
        with open(file_path, 'a', encoding='utf-8') as file:
            json.dump(dict01_func_btn_save_record_to_file02, file, ensure_ascii=False, indent=4)
        messagebox.showinfo(title='Успех', message=f'Запись добавлена в файл по пути {file_path}', parent=win04)
    except FileNotFoundError:
        messagebox.showinfo(title='Не выбран файл', message='Вы не указали файл.', parent=win04)
