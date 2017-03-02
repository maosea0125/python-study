#coding=utf-8
import sys;
import mysql.connector;

try:
    conn = mysql.connector.connect(host='192.168.18.171', user='jmao', passwd='uy288a', db='wordpress', port='3308')
    cursor = conn.cursor()
except Exception:
	sys.exit()

#查询数据
cursor.execute('SELECT * FROM wp_posts')
for post in cursor:
    print(post)

cursor.execute('SELECT ID,post_title FROM wp_posts')
for (ID, post_title) in cursor:
    print(ID, post_title)

cursor.close();
conn.close();