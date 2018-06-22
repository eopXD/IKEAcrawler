# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class metaItem ( Item ) :
# Hierarchy: category > subCategoryContainer > subCategory
	url = Field()
	meta_category = Field()
	meta_subCategoryContainer = Field()
	meta_subCategory = Field()

class LinkItem ( Item ) :
	a_link = Field()
'''
class IkeacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
'''

