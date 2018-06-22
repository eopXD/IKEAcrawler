# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import codecs

class IkeacrawlerPipeline(object):
	def __init__ ( self ) :
		self.current_dir = os.getcwd()

    def process_item(self, item, spider):
        return item
