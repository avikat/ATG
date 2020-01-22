import scrapy
from ..items import QuotetutorialItem
#books
class QuoteSpider(scrapy.Spider):
	name='first'
	start_urls=['http://books.toscrape.com/']


	def parse(self,response):
		items=QuotetutorialItem()
		ite=QuotetutorialItem()
		div=response.css('.product_pod')
		for x in div:
			# name=
			price=x.css('.price_color::text').extract()
			# ite['qut']=price
			yield {'price':price}

#quotes
class QuoteSpider2(scrapy.Spider):
	name='second'
	start_urls=['http://quotes.toscrape.com/']
	def parse(self,response):
		items=QuotetutorialItem()
		div=response.css('div.quote')
		for x in div:
			qut=x.css('.text::text').extract()
			athr=x.css('.author::text').extract()
			tags=x.css('.tag::text').extract()
			items['qut']=qut
			items['athr']=athr
			items['tag']=tags

			yield items
#quicklinks
class QuoteSpider3(scrapy.Spider):
	name='third'
	start_urls=['http://iitmandi.ac.in/']
	def parse(self,response):
		div=response.css('li')
		for x in div:
			links=x.css('a').xpath('@href').extract()

			yield{
			'Quicklinks':links
			}

#links
class QuoteSpider4(scrapy.Spider):
	name='fourth'
	start_urls=['https://www.fresherslive.com/current-affairs/article/list-of-world-president-and-prime-ministers-47']
	def parse(self,response):
		div=response.css('li')
		for x in div:
			country=x.css('a').xpath('@href').extract()

			yield{
			'links':country



			}
#Topics
class QuoteSpider5(scrapy.Spider):
	name='fifth'
	start_urls=['https://www.w3schools.com/']
	def parse(self,response):
		subjects=response.css('a').extract()
		yield{
		'Topics':subjects
		}
#heading		
class QuoteSpider6(scrapy.Spider):
	name='sixth'
	start_urls=['https://one-week-in.com/whatsapp-status-quotes-love-sad/']
	def parse(self,response):
		div=response.css('h2')
		for x in div:
			heading=x.xpath('@id').extract()
			yield{
			'heading':heading
			}
#bcrumbstags
class QuoteSpider7(scrapy.Spider):
	name='seventh'
	start_urls=['https://one-week-in.com/whatsapp-status-quotes-love-sad/']
	def parse(self,response):
		div=response.css('div')
		for x in div:
			bcrumbs=x.css('a').xpath('@href').extract()
			yield{
			'bcrumbs':bcrumbs
			}
#names
class QuoteSpider8(scrapy.Spider):
	name='eighth'
	start_urls=['https://ubuntu.com/']
	def parse(self,response):
		div=response.css('div.col-4')
		for x in div:
			named=x.css('h3 a').xpath('@href')

		yield{
		'names':named
		}
#blog
class QuoteSpider9(scrapy.Spider):
	name='ninth'
	start_urls=['https://www.popads.net/']
	def parse(self,response):
		div=response.css('div.spaced::text').extract()
		yield{
		'Blog':div
		}
#para
class QuoteSpider10(scrapy.Spider):
	name='tenth'
	start_urls=['https://getpocket.com/firefox_learnmore?s=ffi&t=autoredirect&tv=page_learnmore&src=ff_ext']
	def parse(self,response):
		div=response.css('p.mktg-panel__blurb').extract()
		yield{
		'para':div
		}


