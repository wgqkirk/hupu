# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class HupubuxingjietutorialPipeline(object):
    def process_item(self, item, spider):
        return item



class MysqlPipeline(object):
    def __init__(self,url,port,user,pwd,db):
        self.url=url
        self.port=port
        self.user=user
        self.pwd=pwd
        self.db=db
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
        url=crawler.settings.get('MYSQL_URL'),
        port = crawler.settings.get('MYSQL_PORT'),
        user = crawler.settings.get('MYSQL_USER'),
        pwd = crawler.settings.get('MYSQL_PWD'),
        db = crawler.settings.get('MYSQL_DB')
        )
    def insert_mysql(self,sql):
        conn = pymysql.connect(host=self.url, port=self.port, user=self.user, password=self.pwd, db=self.db,charset='utf8')
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    def process_item(self, item, spider):
        title=item['title']
        light_count=item['light_count']
        post_id=item['post_id']
        post_url=item['post_url']
        author=item['author']
        author_url=item['author_url']
        create_date=item['create_date']
        reply_num=item['reply_num']
        page_views=item['page_views']
        last_reply_time=item['last_reply_time']
        last_reply_user=item['last_reply_user']
        sql="insert into street(post_id,title,post_url,author,author_url,create_date,light_count,reply_num,page_views,last_reply_time,last_reply_user) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}') ON DUPLICATE KEY UPDATE last_reply_user=VALUES(last_reply_user),reply_num=VALUES(reply_num),light_count=VALUES(light_count),page_views=VALUES(page_views),last_reply_time=VALUES(last_reply_time)".format(post_id,title.replace("'","\\\'"),post_url,author,author_url,create_date,light_count,reply_num,page_views,last_reply_time,last_reply_user)
        #print(sql)
        self.insert_mysql(sql=sql)
        return item
