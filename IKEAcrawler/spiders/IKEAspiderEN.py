from IKEAcrawler.items import LinkItem

from scrapy.spiders import CrawlSpider
from scrapy import Request



class IKEAspiderEN ( CrawlSpider ) :
	name = "IKEAspiderEN"
	#start_urls = ["http://localhost:8050/render.html?url=https://www.ikea.com/gb/en/products/&timeout=10&wait=3"]
	start_urls = ["http://localhost:8050/render.html?url=https://www.ikea.com/gb/en/rooms/&timeout=10&wait=3"]
	
	def parse ( self, response ) :
		# parse room page
		'''
		main_links = response.xpath('//li[@class="CategoryNavigation-List--item"]//a').extract()
		for _ in main_links :
			item = LinkItem()
			item["a_link"] = _
			yield item
		'''
		# parse product page
		'''
		main_links = response.xpath('//h5/a').extract()
		for _ in main_links : 
			item = LinkItem()
			item["a_link"] = _
			yield item

		sub_links = response.xpath('//li[@class="LandingPage-PlainList--item"]/a').extract()
		for _ in sub_links :
			item = LinkItem()
			item["a_link"] = _
			yield item
		'''