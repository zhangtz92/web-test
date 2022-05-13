# mysql与python配合

平时在开发系统时，一般情况下数据库和表结构都需要提前创建<br>
在项目开发时，都需要提前通过mysql工具+命令创建，但增、删、改、查相关数据需要通过程序实现

###案例：员工管理
- 使用mysql内置命令创建数据库
- 创建一张表
- 表中列：id、用户名（不允许空）、密码（不允许空）、真实姓名（不允许空）、手机号（不允许空）
- 使用python代码实现添加用户、删除用户、更新用户信息
```sql
create database users_management DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
```sql
use users_management;
```
```sql
create table user_info(
    id int not null auto_increment primary key,
    username varchar(10) not null,
    password varchar(20) not null,
    realname varchar(10) not null,
    mobile varchar(11) not null
)default charset=utf8;
```
向数据表中添加数据：
```sql
insert into user_info(username,password,realname,mobile) values("wanger","123123asd","王二","13888888888");
```
![image](./image/day11-01.png)<br>
<br>

##Python操作Mysql
用python代码连接mysql并发送指令<br>
需要安装：pip install pymysql==0.10.1

- 向mysql写入一条数据：
```python
import pymysql
#1.连接mysql
connect=pymysql.connect(host="localhost",port=3306,user='root',password='985001159',db='users_management')#或者写：host="127.0.0.1"，db="users_management"为连接相应数据库
cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)#连接完成后，通过cursor收发数据

#2.发送指令
# 是向数据表发送
cursor.execute("insert into user_info(username,password,realname,mobile) values('jimmy','456456asd','吉米','15111111111')")
connect.commit()

#3.关闭
cursor.close()
connect.close()
```
写入后：<br>
![image](./image/day11-02.png)<br>

###注意：千万不要用字符串格式化去做sql拼接，因为有安全隐患，一定要用sql内部的拼接符

```python
sql="insert into user_info(username,password,realname,mobile) values(%s,%s,%s,%s)"
list=['anshi','123456ghj','按时','13801000000']
cursor.execute(sql,list)
connect.commit()
```
也可以利用字典查找键值传参：
```python
sql="insert into user_info(username,password,realname,mobile) values(%(n1)s,%(n2)s,%(n3)s,%(n4)s)"
diction={'n1':'sophie','n2':'345aqwe','n3':'索菲','n4':'13301011111'}
cursor.execute(sql,diction)
connect.commit()
```

- 向mysql查询数据：
```python
import pymysql
#1.连接mysql
connect=pymysql.connect(host="localhost",port=3306,user='root',password='985001159',db='users_management')#或者写：host="127.0.0.1"，db="users_management"为连接相应数据库
cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)#连接完成后，通过cursor收发数据

#2.发送指令
# 查询数据：
sql="select * from user_info"
cursor.execute(sql)
datalist=cursor.fetchall()
print(datalist)

#3.关闭
cursor.close()
connect.close()
```
执行完成后，返回列表，列表中每个元素为每一行内容构成的字典，数据库中数据以列表套字典形式返回
![image](./image/day11-03.png)<br>

也可以设置条件查询：
```python
sql="select * from user_info where id>2"
cursor.execute(sql)
datalist=cursor.fetchall()
print(datalist)
```

如果只需要获取第一组数据：
```python
sql="select * from user_info where id>2"
cursor.execute(sql)
res=cursor.fetchone()
print(res)
```

- 删除数据：
```python
cursor.execute("delect from user_info where id=2")
connect.commit()
```

- 修改数据：
```python
cursor.execute("update user_info set mobile='18888888888' where id=2")
connect.commit()
```
采用标准格式化：
```python
cursor.execute("update user_info set mobile=%s where id=%s",['18888888888',2,])
connect.commit()
```

