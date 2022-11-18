# 8) связка

import b_02_import_data as b
import c_03_keep_data as c
import e_05_search_data as e


# Общая функция взаимодействия с пользователем
def click_button():
    answer = 'yes'
    # предоставляем возможность ввести данные в телефонный справочник
    while answer != 'no':
        answer = input('Вы желаете добавить информацию в телефонную книгу? yes/no: ')
        if answer == 'yes':
            c.keep_data(b.import_data())
    # предоставляем возможность поиска данных в телефонном справочнике
    answer = 'yes'
    while answer != 'no':
        answer = input('Вы желаете поискать информацию в телефонной книге? yes/no: ')
        if answer == 'yes':
            e.search_data()



if __name__ == "__main__":
    pass
