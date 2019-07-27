import csv

class ScrapyMoviePipeline(object):

    def open_spider(self,spider):
        self.csv_file = open("movies.csv",'w',encoding='utf-8')
        # 定义一个列表，用于整合所有的信息
        self.csv_items = []


    def process_item(self, item, spider):
        # 定义一个item用于整合每一个item的信息
        item_csv = []
        item_csv.append(item['name'])
        item_csv.append(item["date"])
        item_csv.append(item["haibao"])
        item_csv.append(item["info"])
        item_csv.append(item['zhongzi'])

        self.csv_items.append(item_csv) + ',\n'
        return item

    def close_spider(self,spider):
        writer = csv.writer(self.csv_file)
        writer.writerow(["name","date","haibao","info","zhongzi"])
        writer.writerows(self.csv_items)

        self.csv_file.close()