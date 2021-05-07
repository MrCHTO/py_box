import pymysql
db = pymysql.connect(host='rm-2ze2pr85o2ozj8479po.mysql.rds.aliyuncs.com', port=3306, user='rds_user',
                     passwd='CTuser1928', charset='utf8')
cursor = db.cursor()
sql = 'show databases'
cursor.execute(sql)
results = cursor.fetchall()
length = len(results)
print(length)
for row in results:
    i = 1
    a = row[0]
    print(str(i)+str(".")+str(a))
    i = i+1

'''
db = connect(host='rm-2ze2pr85o2ozj8479po.mysql.rds.aliyuncs.com', port=3306, user='rds_user',
                     passwd='CTuser1928', db='mysql', charset='utf8')
cursor = db.cursor()
sql = 'show tables'
cursor.execute(sql)
results = cursor.fetchall()

list0  = Listbox(top)
for item in results:                 # 第一个小部件插入数据
    list0.insert(0,item)
list0.pack()  

'''
