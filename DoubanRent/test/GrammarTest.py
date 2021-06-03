class Test:
    dictionary = ['整租', '两室', '三室']

    def __init__(self):
        pass

    def filter(self, list):
        for s in list:
            for word in Test.dictionary:
                if word in s:
                    print(s)


# list = ['测试整租1', '测试两室2', '测试三室3', '测试4', '测试5', 'test6', '7']
# obj = Test()
# obj.filter(list)

# origin = [{"title": "滨江浦沿四号线中医药地铁口整租单身公寓16657040848", "link": "https://www.douban.com/group/topic/228977347/",
#            "id": "https://www.douban.com/people/178358660/"},
#           {"title": "网易，华为首选，冠山小区，整租三室一厅一厨两卫，70方，💰 4300", "link": "https://www.douban.com/group/topic/228976322/",
#            "id": "https://www.douban.com/people/207076398/"},
#           {"title": "网易，华为首选，冠山小区，整租三室一厅一厨两卫，70方，💰 4300", "link": "https://www.douban.com/group/topic/228976322/",
#            "id": "https://www.douban.com/people/207076398/"},
#           ]
#
# remove_duplicate = list({id['id']: id for id in origin}.values())
# print(remove_duplicate)
# print({id['id']: id for id in origin})
# print(len({id['id']: id for id in origin}))


origin = [
    ["https://www.douban.com/people/178358660/", "滨江浦沿四号线中医药地铁口整租单身公寓16657040848",
     "https://www.douban.com/group/topic/228977347/"],
    ["https://www.douban.com/people/178358660/", "滨江浦沿四号线中医药地铁口整租单身公寓16657040848",
     "https://www.douban.com/group/topic/228977347/"],
    ["https://www.douban.com/people/207076398/", "网易，华为首选，冠山小区，整租三室一厅一厨两卫，70方，💰 4300",
     "https://www.douban.com/group/topic/228976322/"]
]
print(list({v[0]: v for v in origin}.values()))
