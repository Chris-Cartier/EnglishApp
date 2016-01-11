__author__ = 'chris'
# coding:utf-8

import MySQLdb as mysql
import sys
try:
    # 读取图片文件
    fp = open("/home/chris/Picture/lovely.png")
    img = fp.read()
    fp.close()
except IOError,e:
    print "Error %d %s" % (e.args[0],e.args[1])
    sys.exit(1)
try:
    # mysql连接
    conn = mysql.connect(host='localhost', user='root', passwd='123456', db='apple', port=3306)
    cursor = conn.cursor()
    cursor.execute('create table images(Id INT PRIMARY KEY AUTO_INCREMENT, Data MEDIUMBLOB);')
    # 注意使用Binary()函数来指定存储的是二进制
    cursor.execute("INSERT INTO images SET Data='%s'" % mysql.escape_string(img))
    # 如果数据库没有设置自动提交，这里要提交一下
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()
except mysql.Error, e:
    print "Error %d %s" % (e.args[0],e.args[1])
    sys.exit(1)
