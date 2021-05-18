import schedule
import time
import os


def job():
    file_name = "data/BinjiangRent-" + time.strftime("%Y%m%d-%H%M", time.localtime()) + ".json"
    os.system("scrapy crawl BinjiangRent -o" + file_name)


schedule.every().day.at("22:00").do(job)
# schedule.every(1).minutes.do(job)

job()
# while True:
#     schedule.run_pending()
#     time.sleep(1)
