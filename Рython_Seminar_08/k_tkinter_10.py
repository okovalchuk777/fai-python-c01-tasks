from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from csv import DictReader
import json
import os
from pathlib import Path
# Не использовать в именах файлов '-' (import не видит файл)
import a_001_add_record_to_db as a_001
import a_002_search_edit_record_in_db as a_002

id_counter_file = 'id_counter.txt'  # файл для отслеживания занятого идентификатора
dict_enterprise_db_file = 'dict_enterprise_db.json'  # файл постоянного хранения данных предприятия


def func_import_file_to_db():
    try:
        file_path = filedialog.askopenfilename(parent=root, title='Выбор файла',
                                               filetypes=(('CSV документы (*.csv)', '*.csv'), ('Все файлы', '*.*')))
        with open(file_path, 'r', encoding='utf-8') as f:
            dict_reader = DictReader(f)
            list_of_dict = list(dict_reader)
        for i in list_of_dict:
            i['Телефон'] = i['Телефон'].split(';')
            with open(id_counter_file, 'r', encoding='utf-8') as f01:
                data = f01.read().rstrip('\n')
            fle = Path(dict_enterprise_db_file)  # проверка существует ли такой файл (если файла нет - то он будет создан)
            fle.touch(exist_ok=True)  # проверка существует ли такой файл (если файла нет - то он будет создан)
            if os.stat(dict_enterprise_db_file).st_size == 0:  # если файл пустой
                dict_enterprise_db = {int(data): i}  # то формируем новый словарь
                with open(id_counter_file, 'w', encoding='utf-8') as f01:
                    f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
                with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
                    json.dump(dict_enterprise_db, f02, ensure_ascii=False, indent=4)  # перезаписываем файл данных телефонного справочника
            elif os.stat(dict_enterprise_db_file).st_size != 0:  # если файл не пустой
                with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f02:
                    dict_enterprise_db = json.load(f02)  # загружаем весь справочник
                    # Нахождение одинаковых записей
                    # Нахождение hash словаря dict02_func_button_add_record_to_db
                for k, v in dict_enterprise_db.items():
                    if a_001.func_dict_hash(dict_enterprise_db[k]) == a_001.func_dict_hash(i):
                        # messagebox.showerror(title='Дубликат', message='Такая запись уже существует!', parent=root)
                        break
                else:
                    dict_enterprise_db[int(data)] = i  # добавляем новое значение
                    # messagebox.showinfo(title='Успех', message='Данные успешно внесены в БД.', parent=root)
                    with open(id_counter_file, 'w', encoding='utf-8') as f01:
                        f01.write(str(int(data) + 1))  # увеличиваем значение идентификатора на единицу в файле
                    with open(dict_enterprise_db_file, 'w', encoding='utf-8') as f02:
                        json.dump(dict_enterprise_db, f02, ensure_ascii=False,
                                  indent=4)  # перезаписываем файл данных телефонного справочника

        messagebox.showinfo(title='Успех', message='Данные успешно внесены в БД.', parent=root)
    except FileNotFoundError:
        messagebox.showinfo(title='Не выбран файл', message='Вы не указали файл.', parent=root)


def func_export_data_from_db():
    try:
        with open(dict_enterprise_db_file, 'r', encoding='utf-8') as f01:
            dict_enterprise_db = json.load(f01)  # загружаем весь справочник

        file_path = filedialog.asksaveasfilename(parent=root, initialfile='Untitled.json', title='Сохранение файла',
                                                 defaultextension=".json",
                                                 filetypes=(('JSON документы (*.json)', '*.json'), ('Все файлы', '*.*')))

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_enterprise_db, file, ensure_ascii=False, indent=4)
        messagebox.showinfo(title='Успех', message=f'БД сохранена в файл по пути {file_path}', parent=root)

    except FileNotFoundError:
        messagebox.showinfo(title='Не выбран файл', message='Вы не указали файл.', parent=root)


def func_program_quit():
    answer = messagebox.askokcancel(title='Выход из программы', message='Закрыть программу?')  # False, False, True
    if answer:
        root.destroy()


def func_about_program():
    messagebox.showinfo(title='О программе', message='Версия программы 0.0.1')


def main_func():
    global root

    root = Tk()
    root.title('База Данных Предприятия')  # Заголовок окна
    root.iconbitmap('python_icon.ico')  # иконка в заголовке окна
    root.geometry('1000x650+330+180')

    main_menu = Menu(root)
    root.config(menu=main_menu)
    # ===================================================================
    # Выпадающее меню

    # 'Общее' меню ('Импорт файла в БД', 'Экспорт БД', 'Выйти')
    general_menu = Menu(main_menu, tearoff=0)
    general_menu.add_command(label='Импорт файла в БД', command=func_import_file_to_db)
    general_menu.add_command(label='Экспорт БД', command=func_export_data_from_db)
    general_menu.add_separator()
    general_menu.add_command(label='Выйти', command=func_program_quit)
    main_menu.add_cascade(label='Общее', menu=general_menu)

    # 'Добавление' меню ('Добавить запись в БД')
    edit_menu = Menu(main_menu, tearoff=0)
    edit_menu.add_command(label='Добавить запись в БД', command=a_001.func_add_record_to_db)
    main_menu.add_cascade(label='Добавление', menu=edit_menu)

    # 'Поиск и Редактирование' меню ('Найти/редактировать запись в БД')
    search_menu = Menu(main_menu, tearoff=0)
    search_menu.add_command(label='Найти/редактировать запись в БД', command=a_002.func_search_record_in_db)
    main_menu.add_cascade(label='Поиск и Редактирование', menu=search_menu)

    # 'Справка' меню ('О программе')
    search_menu = Menu(main_menu, tearoff=0)
    search_menu.add_command(label='О программе', command=func_about_program)
    main_menu.add_cascade(label='Справка', menu=search_menu)

    frame = Frame(root)
    frame.pack(expand=1, fill=BOTH)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("forest.jpg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    root.mainloop()
