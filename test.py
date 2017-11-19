from lxml import html
from lxml import etree

import requests

url = 'http://www.bz-berlin.de/leute/adam-sucht-eva-djamila-rowe-holt-zur-sex-beichte-aus'
x_category = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[1]'
x_subjects = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]/div/div[2]'
x_author = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[1]/author'
d = {'category': x_category ,'subjects': x_subjects ,'author': x_author}

xpath = '/html/body/div[4]/article/div[1]/div[2]/section[1]/div/header/div[2]'

#This will create a list of buyers:

page = requests.get(url)

tree = etree.fromstring(page.text,base_url = url)
html_body = etree.ETXPath(xpath)

print(html_body)
