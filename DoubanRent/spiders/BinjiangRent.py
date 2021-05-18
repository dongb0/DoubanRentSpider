import scrapy


class BinjiangrentSpider(scrapy.Spider):
    name = 'BinjiangRent'
    allowed_domains = ['douban.com']
    start_urls = ['https://douban.com/']
    filter_words = ['整租', '两房', '两室', '三房', '华为']

    def parse(self, response):
        print(response)
        # response.css return value?
        raw_result = []
        for titles in response.css('.olt .title'):
            target_title = titles.css('a::attr(title)').get()
            for word in BinjiangrentSpider.filter_words:
                if word in target_title:
                    # raw_result.append({'title': target_title, 'link': titles.css('a::attr(href)').get()})
                    yield {'title': target_title, 'link': titles.css('a::attr(href)').get()}

        # result = [dict(t) for t in set([tuple(d.items()) for d in raw_result])]
        # for r in result:
        #     yield r

    def start_requests(self):
        url_template = "https://www.douban.com/group/554566/discussion?start="
        for i in range(0, 200, 25):
            yield scrapy.Request(url=url_template + str(i), callback=self.parse)
