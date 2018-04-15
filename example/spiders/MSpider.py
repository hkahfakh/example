import scrapy
from example.items import ExampleItem
     #设置name
class MSpider(scrapy.Spider):
    name = "MySpider"
    #设定域名
    allowed_domains = ["bj.ganji.com"]
    #填写爬取地址
    start_urls = ["http://bj.ganji.com/fang1/"]
    #编写爬取方法
    def parse(self, response):
        item = ExampleItem()  
        for box in response.xpath('//div[dl[@class="f-list-item-wrap f-clear"]]'):
            #获取每个div中的课程路径
            item['url'] = box.xpath('.//a[@title]/text()')
            #获取div中的课程标题
            #item['title'] = box.xpath('//a[@class="js-title value title-font"]/text()').extract()[0].strip()
            #获取div中的价格       
            #item['price'] = box.xpath('//div[1]/span[1]/text()')
            yield item

