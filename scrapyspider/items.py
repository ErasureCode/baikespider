# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import scrapy


class DouBanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()

    movie_name = scrapy.Field()

    score = scrapy.Field()

    score_num = scrapy.Field()


class BaiKeItem(scrapy.Item):
    name = scrapy.Field()

    descrip = scrapy.Field()

    infobox = scrapy.Field()

    tag = scrapy.Field()

    oid = scrapy.Field()

    infolink = scrapy.Field()

    polysemy = scrapy.Field()

    # polysemy_href = scrapy.Field()
    # #多义词表

class PicturesItem(scrapy.Item):
    image_urls = scrapy.Field()  # 保存图片地址

    images = scrapy.Field()  # 保存图片的信息

    images_paths = scrapy.Field()  # 保存文件的路径

    image_name = scrapy.Field()  # 图片的名字

    count=scrapy.Field()#记录当前图片是第几个

    oid=scrapy.Field()#记录当期那图片所属网页的oid
