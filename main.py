from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from BeautifulSoup import BeautifulSoup
#import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#
from ppretty import ppretty

import os
import requests
from selenium import webdriver
import urllib
from lxml import etree
from utils import article


#variables
class_1 = "vc-feelback-category-btn ng-scope ng-binding" #a emotion
class_2 = "vc-feelback-category-stats ng-scope ng-binding" #div count
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#open URL
#bz_url = 'http://www.bz-berlin.de/berlin/charlottenburg-wilmersdorf/jugendamt-nahm-ihr-das-baby-weg-weil-sie-an-epilepsie-leidet'
urls = ['http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus','https://www.bz-berlin.de/deutschland/jamaika-aus-bedeutet-nichts-gutes-fuer-deutschland','https://www.bz-berlin.de/berlin/jamaika-gescheitert-was-jetzt-alle-entwicklungen-im-live-blog']


class article():


    def update(self):
        driver = webdriver.Chrome(chromedriver) #start chrome
        driver.get(self.url) #read in article
        xpath = '//*[@id="vcFeelbackWidget"]/div/div[2]/div[1]/div'
        delay = 10 # seconds
        frame_id = 'iframe-widget'
        try:
            frame = WebDriverWait(driver, delay).until(lambda x: x.find_element_by_id(frame_id))
            driver.switch_to_frame(frame)
            #
            for i in range(1,6):
                xpath = '/html/body/div/div/div[2]/div'+'['+str(i)+']'
                xpath = '//*[@id="vcFeelbackWidget"]/div/div[2]/div'+'['+str(i)+']'
                element = driver.find_element(By.XPATH, xpath)
                emotion = element.find_element_by_tag_name('a').text
                count =  element.find_element_by_tag_name('div').text
                self.emotions[emotion] = count 
            print "Page is ready!"
            driver.close()

        except TimeoutException:
            driver.close()
            print "Loading took too much time!"
    def scrap_content(self):
        #article
        a = self.soup.find('div',{'class':'article-text'})
        paragraphs =  a.findAll('p')
        #DO PREPROCESSING HERE I WANT BAG OF WORDS IN BLOCK
        self.paragraphs = paragraphs 
        #self.article = oparagraphs.text
        meta = self.soup.find('header',{'class':'article-meta'})
        self.meta = meta
        self.author = meta.find('span',{'class':'author-name'}) #author as unicode
        self.date = meta.find('time',{'datetime':True}) #date as unicode
        self.title = 'title'

    def __init__(self,url):

        emotions = ['angry','amused','sad','buff','informed']
        f = urllib.urlopen(url)

        #
        self.url = url
        self.article = []
        self.bow = [] #bag of words for the article
        
        self.soup = BeautifulSoup(f)
        self.emotions = dict()#zip(emotions,[0 for i in range(len(emotions))])) #read in emoitions
        self.scrap_content()
        self.update()
        #
    #def __repr__(self):
        #

    def __str__(self):
        print('URL : ',self.url)
        print('HEADER:',self.author.text)
        print('DATE :',self.date.text)
        print('ARTICLE: ',self.paragraphs)
        print('EMOTIONS: ',self.emotions)
        print('BOW:',self.bow)
        return 'BZ-Article'

#print ppretty(article(url), seq_length=10)
for url in urls:
    a = article(url)
    #print(a)
