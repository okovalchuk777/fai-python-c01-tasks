
import re
import requests
from bs4 import BeautifulSoup as bs
import time
import random
from pprint import pprint
import json

url_part01 = 'https://hh.ru'
url_part02 = '/search/vacancy?area=1&area=2019&search_field=name&search_field=company_name&search_field=description&text='
url_part03 = '&page='
url_part04 = '&hhtmFrom=vacancy_search_list'

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 '
               'Safari/537.36 Edg/99.0.1150.55',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 '
               'Safari/537.36']

user_agent = random.choice(user_agents)
headers = {'User-Agent': user_agent}

job_number = int(input(
    "Введите номер профессии (1 (программист), 2 (системный администратор), 3 (строитель), 4 (курьер), 5 (продавец)): "))
job_number_dict = {1: 'программист',
                   2: 'системный+администратор',
                   3: 'строитель',
                   4: 'курьер',
                   5: 'продавец'}

if job_number in range(1, 6):
    list_number = int(input("Введите количество страниц сайта для анализа (от 1 до 50): "))
    if list_number in range(1, 51):
        url_page = url_part01 + url_part02 + job_number_dict.get(job_number) + url_part03 + str(
            list_number - 1) + url_part04
        list_number_response = requests.get(url_page, headers=headers)
        if list_number_response.status_code == 200:
            print(f'Действительно, существует {list_number} страниц сайта для анализа выбранной Вами профессии. '
                  f'Обрабатываем информацию.')
            time.sleep(10)
            vacancies_list = []
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
                                vacancy_compensation_dict['минимальная зарплата'] = vacancy_compensation_list[0]
                            if vacancy_compensation_list[1]:
                                vacancy_compensation_dict['максимальная зарплата'] = vacancy_compensation_list[1]
                        if 'от' in vacancy_compensation_list:
                            index01 = vacancy_compensation_list.index('от')
                            if vacancy_compensation_list[index01 + 1]:
                                vacancy_compensation_dict['минимальная зарплата'] = vacancy_compensation_list[
                                    index01 + 1]
                                vacancy_compensation_list.remove(vacancy_compensation_list[index01 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index01])
                            else:
                                vacancy_compensation_dict['минимальная зарплата'] = 'None'
                        if 'до' in vacancy_compensation_list:
                            index02 = vacancy_compensation_list.index('до')
                            if vacancy_compensation_list[index02 + 1]:
                                vacancy_compensation_dict['максимальная зарплата'] = vacancy_compensation_list[
                                    index02 + 1]
                                vacancy_compensation_list.remove(vacancy_compensation_list[index02 + 1])
                                vacancy_compensation_list.remove(vacancy_compensation_list[index02])
                            else:
                                vacancy_compensation_dict['максимальная зарплата'] = 'None'
                    vacancies_data['Должность'] = vacancy_title
                    vacancies_data['Ссылка на объявление'] = vacancy_title_link
                    vacancies_data['Зарплата'] = vacancy_compensation_dict
                    vacancies_list.append(vacancies_data)
            with open('vacancies_list.json', 'w', encoding='utf-8') as fj:
                json.dump(vacancies_list, fj, ensure_ascii=False, indent=4)
        else:
            print(f'К сожалению, не существует {list_number} страниц сайта для анализа выбранной Вами профессии.')
    else:
        print(f'\nНеобходимо правильно вводить количество страниц сайта для анализа (от 2 до 50).')
else:
    print(f'\nНеобходимо правильно вводить номер профессии. Попробуйте ещё раз.')
