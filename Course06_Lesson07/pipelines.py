# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pprint import pprint


class LmparserPipeline:
    def process_item(self, item, spider):
        print()
        return item


class LmPhotosPipeline(ImagesPipeline):
# чтобы начали корректно видится из файла settings.py настройки приоритезации классов в pipelines.py пришлось в настройки
# File ==> Settings ==> Python Interpreter установить Scrapy и Pillow
# ранее не помогло установка Scrapy и Pillow через pip в окружение проекта
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        pprint(results)
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     return ''
