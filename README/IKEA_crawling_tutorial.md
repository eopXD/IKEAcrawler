# IKEA crawling Record

## Problem

```html
< meta name="IRWStats.category" content="" >
< meta name="IRWStats.subCategoryContainer" content="" >
< meta name="IRWStats.subCategory" content="" >
```

Crawl and evaluate .... [TBD]

## Approach

Crawl with Python via **Scrapy**

Crawl all category page listed [here](https://www.ikea.com/tw/zh/catalog/allproducts/) (list of all product).

Crawl all category page on navigation bar.

### Field

```python
FEED_EXPORT_FIELDS = [
	'url',
	'meta_category',
	'meta_subCategoryContainer',
	'meta_subCategory',
]
```

### Scrapy shell

Poking list of all product page with `scrapy shell`. Rendered the file via Splash (see [Problem encountered](#problem-encountered) )

```bash
scrapy shell 'http://localhost:8050/render.html?url=https://www.ikea.com/tw/zh/catalog/allproducts/&timeout=10&wait=0.5'
```

List name inside all meta tag

```bash
response.xpath('//meta/@name').extract()
```

Select certain meta tag

```bash
response.xpath('//meta[@name="IRWStats.category"]/@content').extract()
```

### Go deeper into a link

Scrapy goes through websites with Request and response.

```txt
Scrapy -> Create Request -> Request GETs to Response -> Response returns data to Scrapy
```

So to call 

So as we get list of link, send request with call_back as the function you wish to call and back.

```python
request = Request(self.splash_l+self.main_url+_+self.splash_r, callback=self.parse_meta)
yield request

```

### Passing data into request

Also we may want to pass data into the request. So add into the `meta` inside the request. `meta` is in dictionary format to send data into request.

```python
request.meta["url"] = self.main_url+_
```

### Output in CSV format

Compile crawler with output directed to CSV.

```
scrapy crawl IKEAspider -o output.csv
```

## Problems encoutered

1. Categories in [list of all products](https://www.ikea.com/tw/zh/catalog/allproducts/) is not organized the same way when dig deeper into category, for example...[secondary_storage](https://www.ikea.com/tw/zh/catalog/categories/departments/secondary_storage/)

	Found that there are different organization. Categories inside Navigation bar has "subCategoryContainer" but inside the list of all product, there are no such meta content.

	**UPDATE : Seperate into two outputs. Crawl links on [list of all product](https://www.ikea.com/tw/zh/catalog/allproducts/) and navigation bar** 

2. Javascipt is not loaded with simply scrapy trying to reach

	Solution : Render the page through [Splash](http://splash.readthedocs.io/en/stable/install.html) (run on Mac via Docker)
	
3. render.html didn't download body of the webpage

	Solution : Increase the waiting time for the webpage to load into Splash. Finally can select the links inside list of product!!!!!!
	
	```bash
	response.xpath("//div[@class='textContainer']/a/@href").extract()
	```
	


