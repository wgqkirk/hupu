# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupubuxingjietutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    light_count=scrapy.Field()
    post_url=scrapy.Field()
    author=scrapy.Field()
    author_url=scrapy.Field()
    create_date=scrapy.Field()
    reply_num=scrapy.Field()
    page_views=scrapy.Field()
    post_id=scrapy.Field()
    last_reply_time=scrapy.Field()
    last_reply_user=scrapy.Field()
