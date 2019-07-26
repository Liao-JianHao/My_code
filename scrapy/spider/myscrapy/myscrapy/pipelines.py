# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class MyscrapyPipeline(object):

    def __init__(self):
        self.file = open('itcast_teacher.txt', 'w')

    def process_item(self, item, spider):
        # 将数据序列化;json.dumps只接收字典
        json_dict = json.dumps(dict(item), ensure_ascii=False) + ',\n'  # ensure_ascii=False 关闭ascii码，显示中文

        # 写入数据
        self.file.write(json_dict)

        return item  # 默认使用完管道之后返回给引擎

    def __del__(self):
        self.file.close()