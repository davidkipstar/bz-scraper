

from BeautifulSoup import BeautifulSoup

import urllib2
from lxml import etree
import requests

x_category = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[1]'
x_subjects = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]'
x_author = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[1]/author'
d = {'category': x_category ,'subjects': x_subjects ,'author': x_author}


url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
response = urllib2.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
	
for category,xpathselector in d.items():	
	setattr(self,category,self.tree.xpath(xpathselector))
"""
def scrap(xpath,):
    # 
    #
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    article = soup.findAll('section',{'class':'article-content'})
    a = article[0]
    article = a.findAll('p')
    author = a.findAll('span',{'class':'author-name'})
    databox = a.findAll('div',{'class':'article-meta-box-right pull-right'})
    a.findAll('time')

    return article
  """