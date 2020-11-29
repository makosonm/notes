# MySQL 

## mysql导出数据&导入数据
 

### 导出数据

#### mysqldump常用命令

1.只导出表结构，不导出数据

> mysqldump -uroot -p123456 -d database > database.sql

2.只导出表数据，不导出结构

> mysqldump -uroot -p123456 -t database > database.sql

3.导出整个数据库，表结构&数据

> mysqldump -uroot -p123456 database > database.sql

4.导出整个数据库,忽略table1，table2

> mysqldump -uroot -p123456 database --ignore-table=database.table1 --ignore-table=database.table2 > database.sql

5.dump指定表中的数据

> mysqldump -uroot -p123456 -t database table1 table2 > database.sql

mysqldump常用参数说明
需要导出的主机信息

> --host, -h

连接数据库端口号

> --port, -P

指定连接的用户名。

> --user, -u

连接数据库密码

> --password, -p

指定连接mysql的socket文件位置，默认路径/tmp/mysql.sock

> --socket,-S

覆盖--databases (-B)参数，指定需要导出的表名。

> --tables

不导出任何数据，只导出数据库表结构。

> --no-data, -d

只导出数据，而不添加CREATE TABLE 语句。

> --no-create-info, -t

设置默认字符集，默认值为utf8

> --default-character-set


### 导入数据
mysql
> mysql -uroot -p123456 -d database < database.sql


## MySQL查看库表索引大小

> 通过MySQL的 information_schema 数据库，可查询数据库中每个表占用的空间、表记录的行数；该库中有一个 TABLES 表，这个表主要字段分别是：

- TABLE_SCHEMA : 数据库名
- TABLE_NAME：表名
- ENGINE：所使用的存储引擎
- TABLES_ROWS：记录数
- DATA_LENGTH：数据大小
- INDEX_LENGTH：索引大小


1、查看所有库的大小

```
MySQL [information_schema]> select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from TABLES;
+----------+
| data     |
+----------+
| 276.82MB |
+----------+
1 row in set (0.03 sec)
```

2、查看指定库的大小

```
MySQL [information_schema]> select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from TABLES where table_schema='envops';
+----------+
| data     |
+----------+
| 270.56MB |
+----------+
1 row in set (0.00 sec)
```

3、查看指定库的指定表的大小

```
MySQL [information_schema]> select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from TABLES where table_schema='envops' and table_name='trace';
+----------+
| data     |
+----------+
| 269.83MB |
+----------+
1 row in set (0.00 sec)
```

4、查看指定库的索引大小

```
MySQL [information_schema]> SELECT CONCAT(ROUND(SUM(index_length)/(1024*1024), 2), ' MB') AS 'Total Index Size' FROM TABLES  WHERE table_schema = 'envops'; 
+------------------+
| Total Index Size |
+------------------+
| 314.30 MB        |
+------------------+
1 row in set (0.00 sec)
```

5、查看指定库的指定表的索引大小

```
MySQL [information_schema]> SELECT CONCAT(ROUND(SUM(index_length)/(1024*1024), 2), ' MB') AS 'Total Index Size' FROM TABLES  WHERE table_schema = 'envops' and table_name='srvc_instance'; 
+------------------+
| Total Index Size |
+------------------+
| 0.02 MB          |
+------------------+
1 row in set (0.00 sec)
```

6、查看一个库中的情况

```
MySQL [information_schema]> SELECT CONCAT(table_schema,'.',table_name) AS 'Table Name', CONCAT(ROUND(table_rows/1000000,4),'M') AS 'Number of Rows', CONCAT(ROUND(data_length/(1024*1024*1024),4),'G') AS 'Data Size', CONCAT(ROUND(index_length/(1024*1024*1
024),4),'G') AS 'Index Size', CONCAT(ROUND((data_length+index_length)/(1024*1024*1024),4),'G') AS'Total'FROM information_schema.TABLES WHERE table_schema LIKE 'envops';
+-----------------------+----------------+-----------+------------+---------+
| Table Name            | Number of Rows | Data Size | Index Size | Total   |
+-----------------------+----------------+-----------+------------+---------+
| envops.api            | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.cluster        | 0.0001M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.configmap      | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.data           | 0.0005M        | 0.0001G   | 0.0000G    | 0.0001G |
| envops.doc_env_info   | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.dye            | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.env            | 0.0013M        | 0.0001G   | 0.0000G    | 0.0001G |
| envops.env_srvc       | 0.0004M        | 0.0001G   | 0.0000G    | 0.0001G |
| envops.env_srvc_ins   | 0.0002M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.trace          | 1.2651M        | 0.2635G   | 0.3066G    | 0.5701G |
| envops.user           | 0.0002M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.user_api       | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.user_env       | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
| envops.user_project   | 0.0000M        | 0.0000G   | 0.0000G    | 0.0000G |
+-----------------------+----------------+-----------+------------+---------+
14 rows in set (0.00 sec)
```
