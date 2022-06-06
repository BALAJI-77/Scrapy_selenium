# method 4
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import scrapy
from selenium import webdriver  
from scrapy.loader import ItemLoader
from scrapy_project.items import Profile
from scrapy import Request
from scrapy.http import HtmlResponse


class ProductSpider(scrapy.Spider):
    name = "scrapy2_spider"
    start_urls=[]
    
    url_collection = ['https://www.webmd.com/drugs/2/drug-53935/cold-tablet-oral/details',
                  'https://www.geeksforgeeks.org/python-using-variable-outside-and-inside-the-class-and-method/',
                  'https://www.bankbazaar.com/tax/how-calculate-income-tax-on-salary-with-example.html',
                  'https://en.wikipedia.org/wiki/Main_Page',
                  'https://wikimediafoundation.org/'
                 ]
    result_list=[]

    def start_requests(self):
        def get_page_data(url):
            driver = webdriver.Chrome("D:\Project\scarpy-selenium\chromedriver.exe")
            driver.get(url)
            return_data = {}
            try:
                sleep(5)
                return_data['title'] = driver.find_element_by_xpath('//title').get_attribute("innerHTML")
                return_data['url']=url
            except:
                print("Data extraction issue")
            
            body = driver.page_source
            response = HtmlResponse(url=driver.current_url, body=body, encoding='utf-8')
            for value in response.xpath('//head'):
                title=value.css('title::text').get(default='not-found')
                temp_data={'url':response.url,'title':title}
                self.result_list.append(temp_data)

        def my_multithreading():        
            with ThreadPoolExecutor(max_workers=5) as executor:
                return executor.map(get_page_data,self.url_collection,timeout = 60)

        my_multithreading()
        print(self.result_list)
        return []
    
    def parse(self, response, **kwargs):
        print('test ok')
        print('===================>>>>>>>>>>>>>>>',response)
