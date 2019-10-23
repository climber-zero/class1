"""
    通过终端输入一个名字
    获得其所有信息
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8'
                     )
# 生成游标对象(操作数据库,执行SQl语句)
cur = db.cursor()
name = input('输入姓名:')

# 执行各种数据的读写操作
sql = "select * from interest where name='%s';" % name
print(sql)
cur.execute(sql)
# 迭代sql获取查询结果
# for item in cur:
#     print(item)

# 获取查询结果
one_row = cur.fetchone()
print(one_row)
# all_row = cur.fetchall()
# print(all_row)

# 关闭游标和数据库连接
cur.close()
db.close()
