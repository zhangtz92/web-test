# 关于MySQL

- MySQL安装与配置
- MySQL启动与关闭
- MySQL指令
- MySQL与任何语言都可以配合，需要安装python第三方模块，通过发送指令获取MySQL返回的结果

##安装Mysql
先安装相关插件
![image](./image/day10-01.png)<br>

下载：
https://downloads.mysql.com/archives/community/
<br>下载mysql-5.7.31-winx64

下载后直接解压到c盘program files文件夹下

##创建配置文件
需要放在mysql的安装目录下<br>
创建my.ini
![image](./image/day10-02.png)<br>
```
[mysqld]

port=3306

basedir=C:\\Program Files\\mysql-5.7.31-winx64

datadir=C:\\Program Files\\mysql-5.7.31-winx64\\data
```
![image](./image/day10-03.png)<br>

##初始化
- 打开终端，以管理员权限运行
- 输入初始化命令
```
"C:\Program Files\mysql-5.7.31-winx64\bin\mysqld.exe" --initialize-insecure
```

##启动mysql
制作成windows服务，用来启动与关闭
- 制作服务
```
"C:\Program Files\mysql-5.7.31-winx64\bin\mysqld.exe" --install mysql57
```
终端会显示service successfully installed，表示制作成功

在终端中输入net start mysql57与net stop mysql57来启动和关闭服务

也可以在windows服务中启动mysql
![image](./image/day10-04.png)<br>

##链接mysql
```
"C:\Program Files\mysql-5.7.31-winx64\bin\mysql.exe" -h 127.0.0.1 -P 3306 -u root -p
```
如果在自己电脑上，可简化：
```
"C:\Program Files\mysql-5.7.31-winx64\bin\mysql.exe" -u root -p
```

将"C:\Program Files\mysql-5.7.31-winx64\bin\"可添加到系统环境变量中，可以直接：
```
"mysql -u root -p
```
![image](./image/day10-05.png)<br>

####设置密码：
仅限首次设置！
```mysql
set password =password("自己的密码");
```

##数据库相关操作
- 查看已有数据库
```mysql
show databases;
```

- 退出
```mysql
exit;
```
```mysql
quit
```

- 清屏
```sql
system clear
```

其他一些基础操作：
https://blog.csdn.net/weixin_37887248/article/details/80897230

##mysql指令
mysql中，数据库类似文件夹，数据表类似文件
###1.数据库管理
- 创建数据库
```mysql
create database 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
注意：不要用中文

- 删除数据库
```mysql
drop database 数据库名称;
```

- 进入数据库
```mysql
use database 数据库名称;
```

- 查看数据库下全部数据表
```mysql
show tables;
```

###2.数据表管理
- 创建数据表
```mysql
create table 表名称(
    列名称 类型,
    列名称 类型,
    列名称 类型,
    ...
)default charset=utf8;
```
例如：
```mysql
create table tb1(
    id int,
    name varchar(16),
    age int
)default charset=utf8;
```
补充：可在列名称 类型后加入not null，表示不允许为空<br>

设置默认值：default
```sql
create table tb1(
    id int,
    name varchar(16),
    age int default 18
)default charset=utf8;
```
设置主键：primary key，表示不允许为空，不允许重复（类似于人的身份证）
```sql
create table tb1(
    id int auto_increament primary key, --auto_increament表示自增
    name varchar(16),
    age int default 18
)default charset=utf8;
```

- 删除数据表
```sql
drop table 表名称;
```

- 常用的数据类型
    - tinyint
    <br>8bit
    ```
    有符号：取值范围-128~127
    无符号：取值范围0~255
    ```
    ```sql
    create table tb1(
      id int not null auto_increment primary key, --auto_increament表示自增
      age tinyint, --有符号
      num tinyint unsigned --无符号
    )default charset=utf8;
    ```
    - int
    <br>32bit
    - bigint
    <br>64bit
    
    - decimal
    <br>表示精准小数
    ```sql
    create table tb1(
      id int not null auto_increment primary key, --auto_increament表示自增
      salary decimal(8,2) --8位有效数，2位小数
    )default charset=utf8;
    ```
    
- 向数据表插入数据
```sql
create table tb1(
    id int not null auto_increment primary key, --auto_increament表示自增
    salary int,
    age int default 18
)default charset=utf8;
```
```sql
insert into tb1(salary,age) values(10000,18);
insert into tb1(salary,age) values(20000,28);
insert into tb1(salary,age) values(30000,38),(40000,48),(50000,58); --批量插入
```

- 查看表中数据
```sql
select * from tb1;
```
- 字符串的存储
    - char
    ```sql
    --定长字符串
    create table tb4(
      id int not null auto_increment primary key,
      mobile char(11) -- 固定用11个字符进行存储，哪怕没有11个字符，也会存11个字符
    )default charset=utf8;
    ```
    - varchar
    ```sql
    --变长字符串
    create table tb4(
      id int not null auto_increment primary key,
      mobile varchar(11) -- 真实又多长，就存储多长，仅限制范围为11
    )default charset=utf8;
    ```
    - text
        - 最多可存65535个字符，用于长文本
    - mediumtext
        - 用于长文本，存储多
    - longtext
        - 用于长文本，存储多
        
    - datatime
        - 时间存储
    - data
        - 日期
    