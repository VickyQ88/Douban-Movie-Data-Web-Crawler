# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class DoubanmovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=Field()#
    year=Field()#上映年份
    score=Field()#豆瓣分数
    director=Field()#导演
    classification=Field()#分类
    actor=Field()#演员