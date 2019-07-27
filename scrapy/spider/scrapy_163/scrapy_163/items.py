# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()  # 职位名称
    link = scrapy.Field()  # 链接
    department = scrapy.Field()  # 部门
    position_type = scrapy.Field()  # 职位类型
    work_type = scrapy.Field()  # 工作类型
    work_addr = scrapy.Field()  # 工作地址
    num = scrapy.Field()  # 招聘人数
    data = scrapy.Field()  # 发布时间
    describe = scrapy.Field()  # 岗位描述
    require = scrapy.Field()  # 岗位要求
