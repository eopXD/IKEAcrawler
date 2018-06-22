# IKEA webpage compare between GB_EN  and TW 

Done by [eopXD](https://github.com/eopXD)@2018.06.21

## Taiwan (TW)

1. Pages to Crawl

	- Navigation bar
		- 找產品
		- 找空間
				
		```
		nav_product_list = response.xpath('//li[@class="ct-header-nav-sub-2-item"]/a/@href').extract()
		nav_room_list = response.xpath('//a[@class="ct-nav-sub-link ct-sub-link-space"]/@href').extract()
		
		```
	- [List-of-Product](https://www.ikea.com/tw/zh/catalog/allproducts/)
		
		```
		product_category_list = response.xpath('//ul[@class="textContainer"]/li/a/@href').extract()
		
		```

2. Crawl meta tags in the pages above $\uparrow$$\uparrow$$\uparrow$

	- Category
	- subCategoryContainer
	- subCategory

### Require field: URL, meta tags


## Great Britain (GB)

1. Pages to crawl
	- [List-of-Product](https://www.ikea.com/gb/en/products/)
	- [List-of-Rooms](https://www.ikea.com/gb/en/rooms/)

2. Category  level
	- Category

		
		```
		main_links = response.xpath('//h5/a').extract()
		
		```
	
	- subCategory
		
		```
		main_links = response.xpath('//li[@class="CategoryNavigation-List--item"]//a').extract()
			
		```

Crawl link by Scrapy then parse with BeautifulSoup

### Require field: URL, Category

## Result

### TW

- `tw_nav.csv`: scratched from links inside navigation bar
- `tw_product.csv`: scratched from links in product list

### GB

- `en_product.csv`: category scratched from product list
list
- `en_room_.csv`: category scratched from room list

### Compare

- `result.txt`: result of comparing. Output the categories that both appeared in TW and GB.