from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select
import time
from datetime import date, datetime, timedelta
import arrow
import json
import hashlib
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def dict_hash(dictionary):
    """SHA256 hash of a dictionary."""
    dhash = hashlib.sha256()
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()

# Mongo DB подключение
client = MongoClient('127.0.0.1', 27017)
db = client['emails']
mailru = db.mailru

options = Options()
options.add_argument("start-maximized")

s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://e.mail.ru/templates/')

wait = WebDriverWait(driver, 15)

# Теперь нам надо авторизоваться
# заполняем поле логин
try:
    wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    emailElem = driver.find_element(By.NAME, 'username')
    emailElem.send_keys('study.ai_172@mail.ru')
    emailElem.submit()
    time.sleep(1)
except exceptions.TimeoutException:
    print("Отсутствует поле для ввода логина пользователя")

# заполняем поле пароль
try:
    wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    passwordElem = driver.find_element(By.NAME, 'password')
    passwordElem.send_keys('NextPassword172#')
    passwordElem.submit()
except exceptions.TimeoutException:
    print("Отсутствует поле для ввода пароля пользователя")

# Мы авторизовались
# Собираем ссылки на письма
email_links = []
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'/inbox/')]")))
    elems = driver.find_elements(By.XPATH, "//a[contains(@class,'direction_letter-bottom')]")
    for elem in elems:
        link = elem.get_attribute('href')
        link = link[:-1]
        if link not in email_links:
            email_links.append(link)
except exceptions.TimeoutException:
    print("Страница на смогла загрузиться")

pages_list_last_value = ''

# Прокрутка до конца страницы
while True:
    pages = driver.find_elements(By.XPATH, "//a[contains(@class,'direction_letter-bottom')]")
    if pages[-1] == pages_list_last_value:
        print("Прокрутка страницы окончена")
        break
    pages_list_last_value = pages[-1]
    actions = ActionChains(driver)
    actions.move_to_element(pages_list_last_value)
    actions.perform()
    time.sleep(4)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'/inbox/')]")))
        elems = driver.find_elements(By.XPATH, "//a[contains(@class,'direction_letter-bottom')]")
        for elem in elems:
            link = elem.get_attribute('href')
            link = link[:-1]
            if link not in email_links:
                email_links.append(link)
    except exceptions.TimeoutException:
        print("Страница на смогла загрузиться")

today = date.today()

# Перебираем каждое письмо
for email_link in email_links:
    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get(email_link)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'letter-contact')]")))
        elem1 = driver.find_element(By.XPATH, "//span[contains(@class,'letter-contact')]")
        elem2 = driver.find_element(By.XPATH, "//div[contains(@class,'letter__date')]")
        elem3 = driver.find_element(By.XPATH, "//div[contains(@class,'letter-body')]")
        elem4 = driver.find_element(By.XPATH, "//h2[contains(@class,'thread-subject')]")
        from_email = elem1.get_attribute('title')
        from_title = elem1.text
        date_list = elem2.text.split(sep=',')
        if 'Сегодня' in date_list:
            date_list[0] = today.strftime("%Y-%m-%d")
        elif 'Вчера' in date_list:
            date_list[0] = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        else:
            year = today.strftime("%Y")
            date_list[0] = date_list[0] + ' ' + year
            print(date_list[0])
            date_list[0] = arrow.get(date_list[0], 'D MMMM YYYY', locale='ru').format('YYYY-MM-DD')
        date_email = date_list[0]
        time_email = date_list[-1].replace(' ', '')
        subject = elem4.text
        text_info = elem3.text
        # Отправка данных в БД
        emails_mailru_dict = {}
        source = "mail.ru"
        emails_mailru_dict['Источник'] = source
        emails_mailru_dict['Почта отправителя'] = from_email
        emails_mailru_dict['Короткое описание отправителя'] = from_title
        emails_mailru_dict['Дата письма'] = date_email
        emails_mailru_dict['Время письма'] = time_email
        emails_mailru_dict['Тема письма'] = subject
        emails_mailru_dict['Текст письма'] = text_info
        # Hash словаря будет ключом '_id' документа
        emails_mailru_dict['_id'] = dict_hash(emails_mailru_dict)
        # Вставляем словарь в MongoDB
        try:
            mailru.insert_one(emails_mailru_dict)
        except DuplicateKeyError:
            print(f"Email with id = {emails_mailru_dict['_id']} already exist")
    except exceptions.TimeoutException:
        print("Страница на смогла загрузиться")
    # Close the tab with URL B
    driver.close()
    # Switch back to the first tab with URL A
    driver.switch_to.window(driver.window_handles[0])
