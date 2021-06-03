import schedule
import time
import os


def job():
    # file_name = "data/BinjiangRent-" + time.strftime("%Y%m%d-%H%M", time.localtime()) + ".json"
    # os.system("scrapy crawl BinjiangRent -o" + file_name)
    os.system("scrapy crawl BinjiangRent")


schedule.every().day.at("13:00").do(job)
schedule.every().day.at("22:00").do(job)
# schedule.every(1).minutes.do(job)

job()

while True:
    schedule.run_pending()
    time.sleep(1)
