import requests
import time
import random
from pprint import pprint
import json
import hashlib
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from lxml import html
from datetime import datetime


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


# Python code to convert string to list character-wise
# https://www.geeksforgeeks.org/python-program-convert-string-list/
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


url_lentaru = 'https://lenta.ru/'
url_newsmailru = 'https://news.mail.ru/'

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 '
               'Safari/537.36 Edg/99.0.1150.55',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 '
               'Safari/537.36']

user_agent = random.choice(user_agents)
headers = {'User-Agent': user_agent}

# Mongo DB подключение
client = MongoClient('127.0.0.1', 27017)
db = client['news']
lentaru = db.lentaru
newsmailru = db.newsmailru

# DDOS countermeasure
# time.sleep(10)
response_lentaru = requests.get(url_lentaru, headers=headers)
with open('response_lentaru.html', 'w', encoding='utf-8') as f:
    f.write(response_lentaru.text)
html_lentaru_file = ''
with open('response_lentaru.html', 'r', encoding='utf-8') as f:
    html_lentaru_file = f.read()

response_newsmailru = requests.get(url_newsmailru, headers=headers)
with open('response_newsmailru.html', 'w', encoding='utf-8') as f:
    f.write(response_newsmailru.text)
html_newsmailru_file = ''
with open('response_newsmailru.html', 'r', encoding='utf-8') as f:
    html_newsmailru_file = f.read()

# dom = html.fromstring(response_lentaru.text)
dom_lentaru = html.fromstring(html_lentaru_file)
dom_newsmailru = html.fromstring(html_newsmailru_file)

# Обработка lenta.ru
news_lentaru_list = dom_lentaru.xpath("//div[@class='last24']/a[contains(@class,'card-mini _compact')]")

for news in news_lentaru_list:
    news_lentaru_dict = {}
    source = "lenta.ru"
    name = ''.join(news.xpath(".//text()"))
    link = ''.join(news.xpath("./@href"))
    link_list = link.split(sep="/")
    my_index = [2, 3, 4]
    date_list = [link_list[i] for i in my_index]
    date_time_str = '-'.join(date_list)
    # date_time_obj = datetime.strptime(date_time_str, '%Y/%m/%d').date()
    news_lentaru_dict['Источник'] = source
    news_lentaru_dict['Новость'] = name
    news_lentaru_dict['Ссылка'] = link
    news_lentaru_dict['Дата'] = date_time_str
    # Hash словаря будет ключом '_id' документа
    news_lentaru_dict['_id'] = dict_hash(news_lentaru_dict)
    # Вставляем словарь в MongoDB
    try:
        lentaru.insert_one(news_lentaru_dict)
    except DuplicateKeyError:
        print(f"News with id = {news_lentaru_dict['_id']} already exist")

# Обработка news.mail.ru
news_newsmailru_list01 = dom_newsmailru.xpath("//div[contains(@class,'daynews__item')]")
news_newsmailru_list02 = dom_newsmailru.xpath("//div[@data-logger='news__MainTopNews']//li[@class='list__item']")

news_newsmailru_list = []

for news in news_newsmailru_list01:
    link = ''.join(news.xpath(".//@href"))
    news_newsmailru_list.append(link)

for news in news_newsmailru_list02:
    link = ''.join(news.xpath(".//@href"))
    news_newsmailru_list.append(link)

for news in news_newsmailru_list:
    response_newsmailru_addon = requests.get(news, headers=headers)
    with open('response_newsmailru_addon.html', 'w', encoding='utf-8') as f:
        f.write(response_newsmailru_addon.text)
    html_newsmailru_addon_file = ''
    with open('response_newsmailru_addon.html', 'r', encoding='utf-8') as f:
        html_newsmailru_addon_file = f.read()
    dom_newsmailru_addon = html.fromstring(html_newsmailru_addon_file)
    news_newsmailru_addon_dict = {}
    source = "news.mail.ru"
    name = ''.join(dom_newsmailru_addon.xpath("//h1/text()"))
    link = news
    date_time = Convert(''.join(dom_newsmailru_addon.xpath("//span[@class='note']//@datetime")))
    date_time = ''.join(date_time[0:10])
    news_newsmailru_addon_dict['Источник'] = source
    news_newsmailru_addon_dict['Новость'] = name
    news_newsmailru_addon_dict['Ссылка'] = link
    news_newsmailru_addon_dict['Дата'] = date_time
    # Hash словаря будет ключом '_id' документа
    news_newsmailru_addon_dict['_id'] = dict_hash(news_newsmailru_addon_dict)
    # Вставляем словарь в MongoDB
    try:
        newsmailru.insert_one(news_newsmailru_addon_dict)
    except DuplicateKeyError:
        print(f"News with id = {news_newsmailru_addon_dict['_id']} already exist")
