from scrapy.selector import Selector
from scrapy.http import TextResponse


with open(r'../../data/response.txt', 'r', encoding='utf-8') as f:
    data_str = f.read()
    # "."
    data = Selector(text=data_str).xpath("//table[@class='olt']").getall()
    print(data)
    print(len(data))

    data = Selector(text=data[0]).xpath("//table/tr/td[@nowrap]/a").getall()
    print(data)
    print(len(data))
    print(data[2], data[3])
    print(Selector(text=data[2]).css('a::attr(href)').get())

# data = TextResponse('https://www.douban.com/group/554566/discussion')
# data.replace()
# print(data.body)



