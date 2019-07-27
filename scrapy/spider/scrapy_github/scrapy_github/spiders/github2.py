# -*- coding: utf-8 -*-
import scrapy
from scrapy_github.items import ScrapyGithubItem


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()

        post_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": token,
            "login": "529786580@qq.com",
            "password": "python1216",
            "webauthn-support": "supported"
        }

        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.parse_login,
            formdata=post_data,
        )


    def parse_login(self, response):
        yield scrapy.Request('https://github.com/Mr-xiaoweiwei', callback=self.parse_profile)

    def parse_profile(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())


