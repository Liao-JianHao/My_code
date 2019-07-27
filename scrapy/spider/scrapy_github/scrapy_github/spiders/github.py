# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/Mr-xiaoweiwei']

    def start_requests(self):  # 重写start_request方法，因该方法没有cookie
        url = self.start_urls[0]

        temp = '_octo=GH1.1.117798273.1559633102; _ga=GA1.2.1258201830.1559633108; _device_id=c787f8042cc2205929a6a198b384047c; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; user_session=wNehP02i8rnwGEZbNoibb9m9Qcjsb5jqJMZ5Pb389L9nlAki; __Host-user_session_same_site=wNehP02i8rnwGEZbNoibb9m9Qcjsb5jqJMZ5Pb389L9nlAki; logged_in=yes; dotcom_user=Mr-xiaoweiwei; _gh_sess=aXdFTDRLWE1qd3FFWVpBTDU1dU4yVkQ5S25STllPTm1WV25VWnFvdE5LNnliT1c4Ti9UcVBCbkhyYzZIS2dTRjFla3gySzR3K1dGajRhT3VpQnQyYlBtOWdrNkNMYWptakFIRHVMTWJPaG5YU044NWJrc2hDSWNCaVkvZGhyUlhCMGw5Y0djb1ZSNTRvaXEvNzdQR044cU5MYkN5K0RPZ1A5UjkwVmUvTlI5N0ZLZHIyK3hZRThDNW5NaDNqQ2x4SUNVMklsVllXWlIzb3g1Qmg0dGFtYldLUXl2ZlI2NjRaTVRPTk50YkJNbXh5NW1RS1RDcWkzZzZ5cmk0S0FYMXd0eGdNUGoxSnlMLzdpblBjNmJOcFE9PS0tZGtraFloZ29PNjdxMnNVRjNFMitRQT09--b155c9e6c843f99cfd879f6c940d2e4e4e7dcdfc'
        cookies = {data.split('=')[0]: data.split('=')[1] for data in temp.split("; ")}
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())


