# -*- coding: utf-8 -*-

# Scrapy settings for IKEAcrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'IKEAcrawler'

SPIDER_MODULES = ['IKEAcrawler.spiders']
NEWSPIDER_MODULE = 'IKEAcrawler.spiders'

USER_AGENT = 'eopXD'

ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False

#LOG_FILE = "IKEAcrawl.log"

FEED_EXPORT_FIELDS = [
	'url',
	'meta_category',
	'meta_subCategoryContainer',
	'meta_subCategory',
]

#FEED_EXPORT_FIELDS = [
#	'a_link',
#]
CSV_DELIMETER = "\t"
DOWNLOAD_DELAY = 2
