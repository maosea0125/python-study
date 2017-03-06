#coding=utf-8
import sys;
from Mysqlib import Mysqlib;

config = {
    'host': '192.168.18.171',
    'port': '3308',
    'user': 'jmao',
    'passwd': '',
    'db': 'wordpress',
    'charset': 'utf8',
    'timeout': 30
}

db = Mysqlib(config);

#查询数据
posts = db.fetchAll('SELECT * FROM wp_posts');
for post in posts:
    print(post)

post = db.fetchOne('SELECT * FROM wp_posts LIMIT 1');
print(post);

db.query("INSERT INTO `wp_posts` VALUES (NULL, '1', '2017-02-16 22:25:22', '2017-02-16 14:25:22', '', '新生儿', '', 'inherit', 'open', 'closed', '', '%e6%96%b0%e7%94%9f%e5%84%bf', '', '', '2017-02-16 22:25:22', '2017-02-16 14:25:22', '', '194', 'http://doudou0911.com/wp-content/uploads/2017/02/新生儿.jpg', '0', 'attachment', 'image/jpeg', '0');")
insertId = db.getInsertId();
print(insertId);

db.query('DELETE FROM wp_posts WHERE id = ' + str(insertId));

db.close();