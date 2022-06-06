# method 4
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import scrapy
from selenium import webdriver  
from scrapy.loader import ItemLoader
from scrapy_project.items import Profile
from scrapy import Request
from scrapy.http import HtmlResponse



# class SeleniumMiddleware(object):
#     def process_request(self, request, spider):
#         url = spider.driver.current_url
#         body = spider.driver.page_source
#         return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)

class ProductSpider(scrapy.Spider):
    name = "scrapy2_spider"
    start_urls=[]
    
    url_collection = ['https://www.webmd.com/drugs/2/drug-53935/cold-tablet-oral/details',
                  'https://www.geeksforgeeks.org/python-using-variable-outside-and-inside-the-class-and-method/',
                  'https://www.bankbazaar.com/tax/how-calculate-income-tax-on-salary-with-example.html'
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
            
            # r=Request(url='https://www.bankbazaar.com/tax/how-calculate-income-tax-on-salary-with-example.html', callback=self.parse, dont_filter=True)
            # # r.meta['item']=result_list
            # yield r
            body = driver.page_source
            response = HtmlResponse(url=driver.current_url, body=body, encoding='utf-8')
            for value in response.xpath('//head'):
                title=value.css('title::text').get(default='not-found')
                # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",title)
                # loader = ItemLoader(item=Profile())
                # loader.add_value('title', title)
                # loader.add_value('url', response.url)
                # yield loader.load_item()
                temp_data={'url':response.url,'title':title}
                self.result_list.append(temp_data)

            
        def my_multithreading():        
            with ThreadPoolExecutor(max_workers=5) as executor:
                return executor.map(get_page_data,self.url_collection,timeout = 60)

        # thread_call=my_multithreading()
        my_multithreading()
        # loader = ItemLoader(item=Profile())
        # loader.add_value('data', result_list)
        # yield loader.load_item()
        # r=Request(url='https://www.bankbazaar.com/tax/how-calculate-income-tax-on-salary-with-example.html', callback=self.parse, dont_filter=True)
        # r.meta['item']=result_list
        # yield r
        print(self.result_list)
        return []
    

        
    
    def parse(self, response, **kwargs):
        # item=response.meta['item']
        print('test ok')
        # print(item)
        print('===================>>>>>>>>>>>>>>>',response)
        # for value in response.xpath('//tbody/tr'):
        #     print(value.css('td::text').extract()[1])
        #     print("ok"*200)

# import scrapy
# from scrapy import Request
# from scrapy.http import HtmlResponse
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# class SeleniumMiddleware(object):
#     def process_request(self, request, spider):
#         url = spider.driver.current_url
#         body = spider.driver.page_source
#         return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)


# class FloorSheetSpider(scrapy.Spider):
#     name = "scrapy2_spider"


#     driver = webdriver.Chrome("D:\Project\scarpy-selenium\chromedriver.exe")

#     def start_requests(self):
#         # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         # for date in floorsheet_dates:
#         self.driver.get("https://merolagani.com/Floorsheet.aspx")
#         self.body = self.driver.page_source
#         self.url = 'https://www.webmd.com/drugs/2/drug-53935/cold-tablet-oral/details'
#         print("+++++++++++++++++++",self.url)
#         yield Request(url=self.url, callback=self.parse, dont_filter=True)

#     def parse(self, response, **kwargs):
#         print('test ok')
#         print('===================>>>>>>>>>>>>>>>',response.url)
#         # for value in response.xpath('//tbody/tr'):
#         #     print(value.css('td::text').extract()[1])
#         #     print("ok"*200)