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

from ppretty import ppretty

import os
import requests
from selenium import webdriver
import urllib
from lxml import etree


x_category = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[1]'
x_subjects = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]'
x_author = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[1]/author'
d = {'category': x_category ,'subjects': x_subjects ,'author': x_author}


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
    def scrap_content(self):
        #article
        a = self.soup.find('div',{'class':'article-text'})
        for block in self.a.findAll('p'):
            #DO PREPROCESSING HERE I WANT BAG OF WORDS IN BLOCK
            self.article.append(block.text)
            print(block)
        meta = self.soup.find('header',{'class':'article-meta'})
        self.meta = meta
        self.author = meta.find('div',{'class':'author-name'})
        self.date = meta.find('time',{'datetime':True})

    def __init__(self,url):
        self.url = url
        self.article = []
        self.bow = [] #bag of words for the article
        f = urllib.urlopen(url)
        self.soup = BeautifulSoup(f)
        #self.source_code = BeautifulSoup(self.r.text)#
        self.emotions = dict(zip(emotions,[0 for i in range(len(emotions))])) #read in emoitions
        #
        self.update()
        self.scrap_article()
        #
    #def __repr__(self):
        #

    def __str__(self):
        print('URL : ',self.url)
        print('HEADER:',self.author.text)
        print('DATE :',self.date.text)
        print(a.text for a in self.article)