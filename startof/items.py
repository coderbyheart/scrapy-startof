from scrapy.item import Item, Field

class StartofItem(Item):
    name = Field()
    email = Field()
    url = Field()
