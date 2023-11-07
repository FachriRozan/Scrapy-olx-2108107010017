import scrapy
from scrapy import Request
from olx_scrapy.items import MyItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.olx.co.id/motor-bekas_c200?sorting=desc-price']  # Ganti dengan URL awal

    def parse(self, response):
        # Mendapatkan item box dari halaman saat ini
        item_boxes = response.xpath('//li[contains(@class, "_1DNjI")]')
        for item_box in item_boxes:
            item = MyItem()
            item['item_title'] = item_box.xpath('.//span[@class="_2poNJ"]/text()').get().strip()
            item['item_details'] = item_box.xpath('.//span[@class="YBbhy"]/text()').get().strip()
            item['item_location'] = item_box.xpath('.//span[@class="_2VQu4"]/text()').get().strip()
            item['item_price'] = item_box.xpath('.//span[@class="_2Ks63"]/text()').get().strip()
            yield item
