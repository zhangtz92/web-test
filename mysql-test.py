import pymysql
#1.连接mysql
connect=pymysql.connect(host="localhost",port=3306,user='root',password='985001159',db='users_management')#或者写：host="127.0.0.1"，db="users_management"为连接相应数据库
cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)#连接完成后，通过cursor收发数据

#2.发送指令
# 是向数据表发送：
#sql="insert into user_info(username,password,realname,mobile) values(%s,%s,%s,%s)"
#list=['anshi','123456ghj','按时','13801000000']
#sql="insert into user_info(username,password,realname,mobile) values(%(n1)s,%(n2)s,%(n3)s,%(n4)s)"
#diction={'n1':'sophie','n2':'345aqwe','n3':'索菲','n4':'13301011111'}
#cursor.execute(sql,diction)
#connect.commit()

# 查询数据：
sql="select * from user_info"
cursor.execute(sql)
datalist=cursor.fetchall()
print(datalist)

#3.关闭
cursor.close()
connect.close()

