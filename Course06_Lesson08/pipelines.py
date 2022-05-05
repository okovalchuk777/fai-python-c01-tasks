# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from hashlib import sha256
from pymongo.errors import DuplicateKeyError
from scrapy import item
from instaparser.items import InstaparserItem


class InstaparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.instagram

    def process_item(self, item: InstaparserItem, spider):
        item_dict = dict(item)
        hash_id = sha256(str(item_dict).encode('utf-8'))
        item['_id'] = hash_id.hexdigest()
        collection = self.db[item['profile_username']]
        try:
            collection.insert_one(item)
        except DuplicateKeyError:
            print(f"Vacancy with id = {item['_id']} already exist")
        return item
