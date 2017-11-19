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
import urllib2
from lxml import etree
from utils import article


#variables
class_1 = "vc-feelback-category-btn ng-scope ng-binding" #a emotion
class_2 = "vc-feelback-category-stats ng-scope ng-binding" #div count
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#open URL
#bz_url = 'http://www.bz-berlin.de/berlin/charlottenburg-wilmersdorf/jugendamt-nahm-ihr-das-baby-weg-weil-sie-an-epilepsie-leidet'
url = 'http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus'


#print ppretty(article(url), seq_length=10)
a = article(url)
