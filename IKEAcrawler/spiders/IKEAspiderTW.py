from IKEAcrawler.items import metaItem

from scrapy.spiders import CrawlSpider
from scrapy import Request

class IKEAspiderTW ( CrawlSpider ) :
	name = "IKEAspiderTW"
	start_urls = ["http://localhost:8050/render.html?url=https://www.ikea.com/tw/zh/catalog/allproducts/&timeout=10&wait=3"]
	splash_l = "http://localhost:8050/render.html?url="
	main_url = "https://www.ikea.com"
	splash_r = "&timeout=10&wait=2"
	
	def parse ( self, response ) :
		
		#product_category_list = response.xpath('//ul[@class="textContainer"]/li/a/@href').extract()
		
		nav_product_list = response.xpath('//li[@class="ct-header-nav-sub-2-item"]/a/@href').extract()
		nav_room_list = response.xpath('//a[@class="ct-nav-sub-link ct-sub-link-space"]/@href').extract()
		for _ in nav_product_list :
			request = Request(self.splash_l+self.main_url+_+self.splash_r, callback=self.parse_meta)
			request.meta["url"] = self.main_url+_
			yield request
		for _ in nav_room_list :
			request = Request(self.splash_l+self.main_url+_+self.splash_r, callback=self.parse_meta)
			request.meta["url"] = self.main_url+_
			yield request
			
		'''
		for _ in product_category_list:
			request = Request(self.splash_l+self.main_url+_+self.splash_r, callback=self.parse_meta)
			request.meta["url"] = self.main_url+_
			yield request
		'''
#		for link in product_category_list :
#			yield scrapy.Request(main_url+link+splash_request,call_back=parse_meta)
		
	def parse_meta ( self, response ) :
		meta_name = response.xpath('//meta/@name').extract()
		tmp_dict = {}
		for _ in meta_name:
			l = "//meta[@name=\""
			r = "\"]/@content"
			_content = response.xpath(l+_+r).extract()[0]
			tmp_dict[_] = _content
		item = metaItem()
		item["url"] = response.meta["url"]
		item["meta_category"] = tmp_dict.get("IRWStats.category")
		item["meta_subCategoryContainer"] = tmp_dict.get("IRWStats.subCategoryContainer")
		item["meta_subCategory"] = tmp_dict.get("IRWStats.subCategory")

		return item
		
		
		