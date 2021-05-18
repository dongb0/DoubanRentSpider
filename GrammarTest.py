class Test:
    dictionary = ['整租', '两室', '三室']

    def __init__(self):
        pass

    def filter(self, list):
        for s in list:
            for word in Test.dictionary:
                if word in s:
                    print(s)


list = ['测试整租1', '测试两室2', '测试三室3', '测试4', '测试5', 'test6', '7']
obj = Test()
obj.filter(list)

