import scrapy
import pymysql


class BinjiangrentSpider(scrapy.Spider):
    name = 'BinjiangRent'
    allowed_domains = ['douban.com']
    start_urls = ['https://douban.com/']
    filter_words = ['整租', '两房', '两室', '三房', '三室', '华为']
    conn = pymysql.connect(host="119.29.41.246", user="batina", passwd="batina10+10=100", database="test_db1",
                           charset='utf8mb4')
    cursor = conn.cursor()

    def parse(self, response):
        result = []
        for trs in response.xpath("//table[@class='olt']/tr[position()>1]"):
            title = trs.css('a::attr(title)').get()
            for word in BinjiangrentSpider.filter_words:
                if word in title:
                    links = trs.css('a::attr(href)').getall()
                    # result.append({'title': title, 'link': links[0], 'id': links[1]})
                    result.append([title, links[0], links[1]])

        # records = list({v['id']: v for v in result}.values())
        # for record in records:
        #     yield record

        records = list({v[0]: v for v in result}.values())
        insert_sql = "insert ignore into rent(uid, title, link) values(%s, %s, %s)"
        BinjiangrentSpider.cursor.executemany(insert_sql, records)
        BinjiangrentSpider.conn.commit()

    def start_requests(self):
        url_template = "https://www.douban.com/group/554566/discussion?start="
        for i in range(0, 50, 25):
            yield scrapy.Request(url=url_template + str(i), callback=self.parse)
