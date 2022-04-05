import re
import requests
from bs4 import BeautifulSoup as bs
import time
import random
from pprint import pprint
import json
import hashlib
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


# How to hash a dictionary in Python?
# https://www.doc.ic.ac.uk/~nuric/coding/how-to-hash-a-dictionary-in-python.html


def dict_hash(dictionary):
    # """MD5 hash of a dictionary."""
    """SHA256 hash of a dictionary."""
    # dhash = hashlib.md5() # быстрее работает
    dhash = hashlib.sha256()  # типа секьюрнее
    # We need to sort arguments so {'a': 1, 'b': 2} is
    # the same as {'b': 2, 'a': 1}
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


url_part01 = 'https://hh.ru'
# по 20 объявлений на странице + &items_on_page=20
url_part02 = '/search/vacancy?area=1&area=2019&search_field=name&search_field=company_name&search_field=description' \
             '&items_on_page=20&text= '
url_part03 = '&page='
url_part04 = '&hhtmFrom=vacancy_search_list'

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 '
               'Safari/537.36 Edg/99.0.1150.55',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 '
               'Safari/537.36']

user_agent = random.choice(user_agents)
headers = {'User-Agent': user_agent}
print(headers)

job_number = int(input(
    "Введите номер профессии (1 (программист), 2 (системный администратор), 3 (строитель), 4 (курьер), 5 (продавец)): "))
job_number_dict = {1: 'программист',
                   2: 'системный+администратор',
                   3: 'строитель',
                   4: 'курьер',
                   5: 'продавец'}

if job_number in range(1, 6):
    list_number = int(input("Введите количество страниц сайта для анализа (от 1 до 100): "))
    if list_number in range(1, 101):
        url_page = url_part01 + url_part02 + job_number_dict.get(job_number) + url_part03 + str(
            list_number - 1) + url_part04
        list_number_response = requests.get(url_page, headers=headers)
        if list_number_response.status_code == 200:
            print(f'Действительно, существует {list_number} страниц сайта для анализа выбранной Вами профессии. '
                  f'Обрабатываем информацию.')
            # Mongo DB подключение
            client = MongoClient('127.0.0.1', 27017)
            db = client['hh_vacancies']
            vacancy042022 = db.vacancy042022
            # DDOS countermeasure
            time.sleep(10)
            for i in range(1, list_number + 1):
                url_page02 = url_part01 + url_part02 + job_number_dict.get(job_number) + url_part03 + str(
                    i - 1) + url_part04
                response = requests.get(url_page02, headers=headers)
                with open('response.html', 'w', encoding='utf-8') as f:
                    f.write(response.text)
                html_file = ''
                with open('response.html', 'r', encoding='utf-8') as f:
                    html_file = f.read()
                dom = bs(html_file, 'html.parser')
                vacancies = dom.find_all('div', {'class': 'vacancy-serp-item'})
                for vacancy in vacancies:
                    vacancies_data = {}
                    vacancy_title = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
                    if vacancy_title:
                        vacancy_title = vacancy_title.getText()
                    else:
                        vacancy_title = None
                    vacancy_title_link = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href']
                    vacancy_compensation = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
                    vacancy_compensation_dict = {'минимальная зарплата': '', 'максимальная зарплата': '',
                                                 'денежная единица': ''}
                    if vacancy_compensation is None:
                        vacancy_compensation_dict['минимальная зарплата'] = 'None'
                        vacancy_compensation_dict['максимальная зарплата'] = 'None'
                        vacancy_compensation_dict['денежная единица'] = 'None'
                    else:
                        vacancy_compensation_list = vacancy_compensation.text.replace("\u202f", '').split()
                        if '–' in vacancy_compensation_list:
                            vacancy_compensation_list.remove('–')
                        if 'руб.' in vacancy_compensation_list:
                            vacancy_compensation_dict['денежная единица'] = 'руб.'
                            vacancy_compensation_list.remove('руб.')
                        if 'USD' in vacancy_compensation_list:
                            vacancy_compensation_dict['денежная единица'] = 'USD'
                            vacancy_compensation_list.remove('USD')
                        if 'EUR' in vacancy_compensation_list:
                            vacancy_compensation_dict['денежная единица'] = 'EUR'
                            vacancy_compensation_list.remove('EUR')
                        if 'от' not in vacancy_compensation_list and 'до' not in vacancy_compensation_list:
                            if vacancy_compensation_list[0]:
                                vacancy_compensation_dict['минимальная зарплата'] = int(vacancy_compensation_list[0])
                            if vacancy_compensation_list[1]:
                                vacancy_compensation_dict['максимальная зарплата'] = int(vacancy_compensation_list[1])
                        if 'от' in vacancy_compensation_list:
                            index01 = vacancy_compensation_list.index('от')
                            if vacancy_compensation_list[index01 + 1]:
                                vacancy_compensation_dict['минимальная зарплата'] = int(vacancy_compensation_list[
                                    index01 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index01 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index01])
                            else:
                                vacancy_compensation_dict['минимальная зарплата'] = 'None'
                        if 'до' in vacancy_compensation_list:
                            index02 = vacancy_compensation_list.index('до')
                            if vacancy_compensation_list[index02 + 1]:
                                vacancy_compensation_dict['максимальная зарплата'] = int(vacancy_compensation_list[
                                    index02 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index02 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index02])
                            else:
                                vacancy_compensation_dict['максимальная зарплата'] = 'None'
                    vacancies_data['Должность'] = vacancy_title
                    vacancies_data['Ссылка на объявление'] = vacancy_title_link
                    vacancies_data['Зарплата'] = vacancy_compensation_dict
                    # Hash словаря будет ключом '_id' документа
                    vacancies_data['_id'] = dict_hash(vacancies_data)
                    # Вставляем словарь в MongoDB
                    try:
                        vacancy042022.insert_one(vacancies_data)
                    except DuplicateKeyError:
                        print(f"Document with id = {vacancies_data['_id']} already exist")

        else:
            print(f'К сожалению, не существует {list_number} страниц сайта для анализа выбранной Вами профессии.')
    else:
        print(f'\nНеобходимо правильно вводить количество страниц сайта для анализа (от 2 до 50).')
else:
    print(f'\nНеобходимо правильно вводить номер профессии. Попробуйте ещё раз.')
