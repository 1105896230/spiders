
import scrapy

from demo.spiders.gank import GankItem

class GankSpider(scrapy.Spider,count=1):
    name="gank"

    allowed_domains = ["gank.io"]
    start_urls=["https://gank.io/2018/10/22"]
    def parse(self, response):
        item=GankItem()
        item['url'] = response.url
        item['name']=response.xpath('//div[@class="container content"]/h1/text()').extract()[0]
        item['imageurl']=response.xpath('//div[@class="container content"]/div[@class="outlink"]//p/img/@src').extract()[0]

        return item
        newcontent =response.xpath('//div[@class="container content"]/div[@class="row"]/div[@class="six columns"]/p[@style="text-align: right"]/a/@href').extract_first()
        if newcontent:
            newurl="https://gank.io"+newcontent
            print(newurl)
            yield scrapy.Request(newurl, callback=self.parse)


