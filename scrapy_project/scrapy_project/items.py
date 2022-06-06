# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from turtle import title
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Profile(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    data = scrapy.Field(output_processor=TakeFirst())
    
# class Profile(scrapy.Item):
#     data = scrapy.Field()