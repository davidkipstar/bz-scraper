from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from BeautifulSoup import BeautifulSoup
#import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


#my import 
from utils import scrap_article

#variables
class_1 = "vc-feelback-category-btn ng-scope ng-binding" #a emotion
class_2 = "vc-feelback-category-stats ng-scope ng-binding" #div count
#settings - firefox
#fp = webdriver.FirefoxProfile()
#fp.set_preference("http.response.timeout", 5)
#fp.set_preference("dom.max_script_run_time", 5)
#driver = webdriver.Firefox(firefox_profile=fp)

import os
from selenium import webdriver

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


#open URL
bz_url = 'http://www.bz-berlin.de/berlin/charlottenburg-wilmersdorf/jugendamt-nahm-ihr-das-baby-weg-weil-sie-an-epilepsie-leidet'
url = 'http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus'


#xpath = '/html/body/div/div/div[2]/div[2]/div'
#details = driver.find_elements_by_xpath(xpath)


emotions = ['anger','amused','sad','','informed']
class article():
    def update(self):
        #scrape emotions and update differnece 
        driver = webdriver.Chrome(chromedriver)
        driver.get(bz_url)
        #print(driver..tags)
        //*[@id="vcFeelbackWidget"]/div/div[2]/div[1]/div




        soup = BeautifulSoup(driver.page_source) 
        print(soup.pretify()) 
        driver.quit()
        return 'deine mutter'
    def __init__(self,url):

        self.article = scrap_article(url) # initialize article
        self.id = 123
        self.author = 'David Arnold'
        self.bow = ''
        self.title = ''
        self.emotions = dict(zip(emotions,[0 for i in range(len(emotions))])) #read in emoitions
        self.update()




article(url)


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
