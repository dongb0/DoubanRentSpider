import pymysql

conn = pymysql.connect(host="119.29.41.246", user="batina", passwd="batina10+10=100", database="spider", charset='utf8mb4')
cursor = conn.cursor()

create_table_sql = '''create table if not exists rent(
                    uid varchar(64) not null,
                    title varchar(256) not null,
                    link varchar(64) primary key,
                    fetch_time timestamp) charset=utf8mb4
                    '''

cursor.execute(create_table_sql)

cursor.close()
conn.close()
