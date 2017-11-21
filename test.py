import urllib
from BeautifulSoup import BeautifulSoup

from lxml import html 
import requests
url = 'http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus'
x_category = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[1]'
x_subjects = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]'
x_author = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[1]/author'
d = {'category': x_category ,'subjects': x_subjects ,'author': x_author}

xpath = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]'

author_path = '/html/body/div[3]/article/div[1]/div[2]/section[1]/div/header/div[1]/author/span[2]'
date_path ='/html/body/div[3]/article/div[1]/div[2]/section[1]/div/header/div[2]/time'
categories_path = '/html/body/div[3]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]/ul'
article_path = '/html/body/div[3]/article/div[1]/div[2]/section[1]'

xpaths = [author_path,date_path,categories_path,article_path]
#This will create a list of buyers:

f = urllib.urlopen(url)
soup = BeautifulSoup(f)
page = requests.get(url)

article = soup.find('div',{'class':'article-text'})

for block in article.findAll('p'):
	block = #
meta = soup.find('header',{'class':'article-meta'})
article.p
#name = soup.find('span'  ,{'class':'author-name'})

