from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from BeautifulSoup import BeautifulSoup
#import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


#my import 
#from utils import scrap_article,scrap_id,scrap_author,scrap_title
from ppretty import ppretty
#variables
class_1 = "vc-feelback-category-btn ng-scope ng-binding" #a emotion
class_2 = "vc-feelback-category-stats ng-scope ng-binding" #div count
#settings - firefox
#fp = webdriver.FirefoxProfile()
#fp.set_preference("http.response.timeout", 5)
#fp.set_preference("dom.max_script_run_time", 5)
#driver = webdriver.Firefox(firefox_profile=fp)

import os
import requests
from selenium import webdriver
import urllib2
from lxml import etree

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


#open URL
#bz_url = 'http://www.bz-berlin.de/berlin/charlottenburg-wilmersdorf/jugendamt-nahm-ihr-das-baby-weg-weil-sie-an-epilepsie-leidet'
url = 'http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus'

x_category = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[1]'
x_subjects = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]'
x_author = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[1]/author'
d = {'category': x_category ,'subjects': x_subjects ,'author': x_author}

#xpath = '/html/body/div/div/div[2]/div[2]/div'
#details = driver.find_elements_by_xpath(xpath)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
def load_page(url):
    driver = webdriver.Firefox()
    driver.get("url")
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print "Page is ready!"
        frame = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("dsq1"))
        driver.switch_to_frame(frame)
        result = WebDriverWait(driver, 30).until( lambda x: x.find_element_by_id("post-count"))
    except TimeoutException:
        print "Loading took too much time!"
#


#
#
emotions = ['anger','amused','sad','','informed']
class article():
    def update(self):
        driver = webdriver.Chrome(chromedriver) #start chrome
        driver.get(self.url) #read in article
        xpath = '//*[@id="vcFeelbackWidget"]/div/div[2]/div[1]/div'
        delay = 10 # seconds
        frame_id = 'iframe-widget'
        try:
            frame = WebDriverWait(driver, delay).until(lambda x: x.find_element_by_id(frame_id))
            driver.switch_to_frame(frame)#x
            
            for i in range(1,6):
                xpath = '/html/body/div/div/div[2]/div'+'['+str(i)+']'+'/div'
                element = driver.find_element(By.XPATH, xpath)
                print element.text,'text'
                print element.tag_name,'tag_name'
                print element.parent,'parent'
                print element.location,'location'
                print element.size,'size'
            print "Page is ready!"
            driver.close()

        except TimeoutException:
            driver.close()
            print "Loading took too much time!"
        
        #url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
        #htmlparser = etree.HTMLParser()
        #tree = etree.parse(driver.page_source, htmlparser)
        #tree.xpath(xpath)
        #print(tree)

    def __init__(self,url):
        self.url = url
        response = urllib2.urlopen(self.url)
        htmlparser = etree.HTMLParser()
        self.tree = etree.parse(response, htmlparser)    
        for category,xpathselector in d.items():
            print(category,xpathselector)
            print(self.tree.xpath(xpathselector))
            setattr(self,category,self.tree.xpath(xpathselector))
        self.r = requests.get(self.url)
        self.source_code = BeautifulSoup(self.r.text)#
        self.emotions = dict(zip(emotions,[0 for i in range(len(emotions))])) #read in emoitions
        #self.update()



print ppretty(article(url), seq_length=10)


#html_source = driver.page_source
#
#open bf4
#print(html_source)
#soup = BeautifulSoup(html_source,'html.parser')  
#class "postText" is not defined in the source code
#emotions = soup.findAll('a',{'class':class_1})
#counter = soup.findAll('div',{'class':class_2})
#print(emotions,counter)
#print comments
#xpath = '//*[@id="vcFeelbackWidget"]/div/div[2]/div[1]/div'
#xpath = '/html/body/div/div/div[2]/div[1]/div'
#soup = BeautifulSoup(driver.page_source)
#url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
#htmlparser = etree.HTMLParser()
#tree = etree.parse(driver.page_source, htmlparser)
#tree.xpath(xpath)