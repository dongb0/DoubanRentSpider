import pymysql

conn = pymysql.connect(host="119.29.41.246", user="batina", passwd="batina10+10=100", database="test_db1", charset='utf8mb4')
cursor = conn.cursor()
cursor.execute("select * from t1")
data = cursor.fetchall()
for row in data:
    print(row)

create_table_sql = '''create table if not exists rent(
                    title varchar(256),
                    link varchar(64) not null ,
                    uid varchar(64) primary key) charset=utf8
                    '''

cursor.execute(create_table_sql)


origin = [
    ["https://www.douban.com/people/178358660/", "滨江浦沿四号线中医药地铁口整租单身公寓16657040848",
     "https://www.douban.com/group/topic/228977347/"],
    ["https://www.douban.com/people/178358660/", "滨江浦沿四号线中医药地铁口整租单身公寓16657040848",
     "https://www.douban.com/group/topic/228977347/"],
    ["https://www.douban.com/people/207076398/", "网易，华为首选，冠山小区，整租三室一厅一厨两卫，70方，💰 4300",
     "https://www.douban.com/group/topic/228976322/"]
]

insert_sql = "insert ignore into rent(uid, title, link) values(%s, %s, %s)"
cursor.executemany(insert_sql, origin)
conn.commit()

cursor.execute("select * from rent limit 10")
data = cursor.fetchall()
for row in data:
    print(row)

conn.close()