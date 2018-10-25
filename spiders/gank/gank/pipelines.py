# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

imags="./images"

class GankPipeline(object):
    def process_item(self, item, spider):
        if item.canParse():
            item.downLoad(imags)

        pass



