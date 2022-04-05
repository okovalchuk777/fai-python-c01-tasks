from pymongo import MongoClient
from pprint import pprint

#Query on Embedded/Nested Documents
#https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/

def wage_level(currency, salary):
    client = MongoClient('127.0.0.1', 27017)
    db = client['hh_vacancies']
    vacancy042022 = db.vacancy042022
    for doc in vacancy042022.find({'$or':
        [
            {'Зарплата.денежная единица': currency, 'Зарплата.минимальная зарплата': {'$gt': salary}},
            {'Зарплата.денежная единица': currency, 'Зарплата.максимальная зарплата': {'$gt': salary}}
        ]
    }):
        yield doc


currency_number = int(input("Введите денежную единицу (1 (руб.), 2 (USD), 3 (EUR)): "))

currency_number_dict = {1: 'руб.',
                        2: 'USD',
                        3: 'EUR'}

if currency_number in range(1, 4):
    salary_level = int(input("Введите желаемую зарплату (от 100 до 10000000): "))
    if salary_level in range(100, 10000001):
        for i in wage_level(currency_number_dict.get(currency_number), salary_level):
            pprint(i)
    else:
        print(f'\nНеобходимо правильно вводить желаемую зарплату (от 100 до 10000000).')
else:
    print(f'\nНеобходимо правильно вводить денежную единицу. Попробуйте ещё раз.')
