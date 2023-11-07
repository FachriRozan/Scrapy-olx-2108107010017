# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    item_title = scrapy.Field()
    item_details = scrapy.Field()
    item_location = scrapy.Field()
    item_price = scrapy.Field()

