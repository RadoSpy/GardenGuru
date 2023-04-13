from lxml import html  
import json, requests, re, time, datetime, mysql.connector, csv, random
from dateutil import parser as dateparser
from bs4 import BeautifulSoup

region = None

regions = {'UK':'co.uk','IT':'it','FR':'fr','DE':'de','ES':'es'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


if region == None:
	region = regions['UK']
else:
	try:
		region = regions[region]
	except:
		region = regions['UK']
		print('Region Not Recognized - set to UK')

amazon_url = 'http://www.amazon.'+region+'/dp/'+ASIN
response = requests.get(amazon_url,headers = headers,verify=False)
soup = BeautifulSoup(response.content, "lxml")
#page = response.text
#parser = html.fromstring(page)
'''
XPATH_AGGREGATE = '//span[@id="acrCustomerReviewText"]'
XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'
XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'
XPATH_PRODUCT_PRICE  = '//span[@id="priceblock_ourprice"]/text()'
XPATH_CUSTOMER_REVIEWS = '//span[@id="acrCustomerReviewText"]/text()'
XPATH_CUSTOMER_RATING = '//span[@id="acrPopover"]/@title'
XPATH_FIRST_CREATED = '//tr[@class="date-first-available"]//text()'
XPATH_NUMBER_SELLERS = '//span[@class="olp-padding-right"]//text()'
XPATH_SELLER = '//div[@id="merchant-info"]//text()'
XPATH_TOP100_URL = '//tr[@id="SalesRank"]//a/@href'
XPATH_RELATED_PRODUCTS = '//div[@class="a-section similarities-widget"]//a/@href'
XPATH_RELATED_SHOPPED = '//div[@class="a-carousel-viewport"]//a/@href'
XPATH_BRAND = '//a[@id="bylineInfo"]//text()'
'''


'''
ProductName = 
ProductCategoryName = 
ProductBrand = 
ProductCost =
AmazonLink =
AmazonStar = 
Productimg: = 
ProductDesc: = 
ProductScore = 0
ProductScoreSummary = 
'''