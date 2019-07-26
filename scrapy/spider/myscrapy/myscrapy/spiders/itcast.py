# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'

    # 2.检查域名
    allowed_domains = ['itcast.cn']

    # 1.修改起始域名
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']  # 起始url

    # 3.在parse中实现爬取逻辑
    def parse(self, response):
    #     with open('itcast.html', 'wb') as f:
    #         f.write(response.body)

        node_teacher = response.xpath('//div[@class="li_txt"]')
        for i in node_teacher:
            item = MyscrapyItem()

            item['name'] = i.xpath('./h3/text()')[0].extract()  # extract() 数据进行提取
            item['title'] = i.xpath('./h4/text()')[0].extract()
            item['desc'] = i.xpath('./p/text()')[0].extract()
            yield item