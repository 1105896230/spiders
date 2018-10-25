# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os
import requests


class GankItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    imageurl = scrapy.Field()
    url = scrapy.Field()
    pass

    def canParse(self):
        return self['name'] != '' and self['imageurl'] != ''

    def downLoad(self, imagepath):
        filename = 'file'
        files = self['url'].split("/")
        if len(files) > 3:
            filename = files[len(files) - 3] + "-" + files[len(files) - 2] + "-" + files[len(files) - 1]
        suffix = "jpg"
        data = self['imageurl'].split(".")

        if len(data) >= 2:
            suffix = data[len(data) - 1]

        path = imagepath + "/" + filename + "." + suffix
        if not os.path.exists(path):
            print('下载文件')
            with open(path, 'wb') as fp:
                r = requests.get(self['imageurl'])
                fp.write(r.content)
