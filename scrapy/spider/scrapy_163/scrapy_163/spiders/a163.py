# -*- coding: utf-8 -*-
import scrapy
from scrapy_163.items import Scrapy163Item


class A163Spider(scrapy.Spider):
    name = '163'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']  # 起始url

    def parse(self, response):
        # with open('163.html', 'wb') as f:
        #     f.write(response.body)

        # 获取数据
        node_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        # print(len(node_list))
        for num, node in enumerate(node_list):
            if num % 2 == 0:
                item = Scrapy163Item()  # 创建item对象
                item['position_name'] = node.xpath('./td[1]/a/text()').extract_first()

                # response提供了拼接域名更好的方案：urljoin()
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
                item['department'] = node.xpath('./td[2]/text()').extract_first()
                item['position_type'] = node.xpath('./td[3]/text()').extract_first()
                item['work_type'] = node.xpath('./td[4]/text()').extract_first()
                item['work_addr'] = node.xpath('./td[5]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()
                item['data'] = node.xpath('./td[7]/text()').extract_first()
                # yield item

                # 构建详情页面请求
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_detail,
                    meta={'item': item}
                )

        # 模拟翻页
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()  # 下一页的xpath语法

        if part_url != 'javascript:void(0)':  # url等于href="javascript:void(0)"说明已经到最后一页
            next_url = response.urljoin(part_url)  # 拼接下一页
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )  # 回调处理由谁解析，默认就是parse()方法

    def parse_detail(self, response):
        item = response.meta['item']  # 传递item对象

        item['describe'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract_first()
        item['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract_first()
        yield item