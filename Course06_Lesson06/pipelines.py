# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from jobparser.items import JobparserItem
import json
from hashlib import sha256
from pymongo.errors import DuplicateKeyError
from scrapy import item


class JobparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.vacancy20220417


    def process_item(self, item: JobparserItem, spider):
        if spider.name == 'hhru':
            final_item = self.process_hhru(item)
            del item['salary']
        elif spider.name == 'sjru':
            final_item = self.process_sjru(item)
            del item['salary']
        # final_item_dict = dict(final_item)
        # final_item['_id'] = self.dict_hash(final_item)
        collection = self.db[spider.name]
        try:
            collection.insert_one(final_item)
        except DuplicateKeyError:
            print(f"Vacancy with id = {item['_id']} already exist")
        return item

    def process_hhru(self, item: JobparserItem):
        print(item['salary'])
        if item['salary'] is None:
            item['min_salary'] = None
            item['max_salary'] = None
            item['currency'] = None
            item['type_salary'] = None
        else:
            item['salary'] = [i.replace('\xa0', '').replace(" ", '') for i in item['salary']]
            print(item['salary'])
            if 'з/п не указана' in item['salary']:
                item['min_salary'] = None
                item['max_salary'] = None
                item['currency'] = None
                item['type_salary'] = None
            else:
                if 'наруки' in item['salary']:
                    item['type_salary'] = '"чистая" зарплата (на руки)'
                    item['salary'].remove('наруки')
                if 'довычетаналогов' in item['salary']:
                    item['type_salary'] = '"грязная" зарплата (до вычета налогов)'
                    item['salary'].remove('довычетаналогов')
                if '–' in item['salary']:
                    item['salary'].remove('–')
                if '' in item['salary']:
                    item['salary'].remove('')
                if 'руб.' in item['salary']:
                    item['currency'] = 'руб.'
                    item['salary'].remove('руб.')
                if 'руб./месяц' in item['salary']:
                    item['currency'] = 'руб.'
                    item['salary'].remove('руб./месяц')
                if 'USD' in item['salary']:
                    item['currency'] = 'USD'
                    item['salary'].remove('USD')
                if 'EUR' in item['salary']:
                    item['currency'] = 'EUR'
                    item['salary'].remove('EUR')
                if 'от' not in item['salary'] and 'до' not in item['salary']:
                    if item['salary'][0]:
                        item['min_salary'] = item['salary'][0]
                    if item['salary'][1]:
                        item['max_salary'] = item['salary'][1]
                if 'от' in item['salary']:
                    index01 = item['salary'].index('от')
                    if item['salary'][index01 + 1]:
                        item['min_salary'] = item['salary'][index01 + 1]
                        item['salary'].remove(item['salary'][index01 + 1])
                        item['salary'].remove(item['salary'][index01])
                    else:
                        item['min_salary'] = 'None'
                if 'до' in item['salary']:
                    index02 = item['salary'].index('до')
                    if item['salary'][index02 + 1]:
                        item['max_salary'] = item['salary'][index02 + 1]
                        item['salary'].remove(item['salary'][index02 + 1])
                        item['salary'].remove(item['salary'][index02])
                    else:
                        item['max_salary'] = 'None'
        item_dict = dict(item)
        hash_id = sha256(str(item_dict).encode('utf-8'))
        item['_id'] = hash_id.hexdigest()
        print(item['_id'])

        return item

    def process_sjru(self, item: JobparserItem):
        print(item['salary'])
        if item['salary'] is None:
            item['min_salary'] = None
            item['max_salary'] = None
            item['currency'] = None
            item['type_salary'] = None
        else:
            item['salary'] = [i.replace('\xa0', '').replace(" ", '') for i in item['salary']]
            print(item['salary'])
            if 'з/п не указана' in item['salary']:
                item['min_salary'] = None
                item['max_salary'] = None
                item['currency'] = None
                item['type_salary'] = None
            else:
                if 'Подоговоренности' in item['salary']:
                    item['type_salary'] = 'договорная'
                    item['salary'].remove('Подоговоренности')
                if 'довычетаналогов' in item['salary']:
                    item['type_salary'] = '"грязная" зарплата (до вычета налогов)'
                    item['salary'].remove('довычетаналогов')
                if '–' in item['salary']:
                    item['salary'].remove('–')
                if '' in item['salary']:
                    item['salary'].remove('')
                if 'руб.' in item['salary']:
                    item['currency'] = 'руб.'
                    item['salary'].remove('руб.')
                if 'руб./месяц' in item['salary']:
                    item['currency'] = 'руб.'
                    item['salary'].remove('руб./месяц')
                if 'USD' in item['salary']:
                    item['currency'] = 'USD'
                    item['salary'].remove('USD')
                if 'EUR' in item['salary']:
                    item['currency'] = 'EUR'
                    item['salary'].remove('EUR')
                if 'от' not in item['salary'] and 'до' not in item['salary']:
                    if item['salary'][0]:
                        item['min_salary'] = item['salary'][0]
                    if item['salary'][1]:
                        item['max_salary'] = item['salary'][1]
                if 'от' in item['salary']:
                    index01 = item['salary'].index('от')
                    if item['salary'][index01 + 1]:
                        item['min_salary'] = item['salary'][index01 + 1]
                        item['salary'].remove(item['salary'][index01 + 1])
                        item['salary'].remove(item['salary'][index01])
                    else:
                        item['min_salary'] = 'None'
                if 'до' in item['salary']:
                    index02 = item['salary'].index('до')
                    if item['salary'][index02 + 1]:
                        item['max_salary'] = item['salary'][index02 + 1]
                        item['salary'].remove(item['salary'][index02 + 1])
                        item['salary'].remove(item['salary'][index02])
                    else:
                        item['max_salary'] = 'None'
        item_dict = dict(item)
        hash_id = sha256(str(item_dict).encode('utf-8'))
        item['_id'] = hash_id.hexdigest()
        print(item['_id'])

        return item



