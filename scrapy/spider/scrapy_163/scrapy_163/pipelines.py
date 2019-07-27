# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

class Scrapy163Pipeline(object):
    # def __init__(self):
    #     self.file = open('wang163.json', 'w')
    #
    # def process_item(self, item, spider):
    #     json_dict = json.dumps(dict(item), ensure_ascii=False) + ',\n'
    #     self.file.write(json_dict)
    #
    #     return item
    #
    # def __del__(self):
    #     self.file.close()

    def open_spider(self, spider):  # 使用该方法代替__init__
        self.file = open('wang163.json', 'w')

    def process_item(self, item, spider):
        json_dict = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(json_dict)

        return item

    def close_spider(self, spider):  # 使用该方法代替__del__
        self.file.close()