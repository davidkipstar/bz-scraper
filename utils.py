

from BeautifulSoup import BeautifulSoup

import urllib2
from lxml import etree
import requests

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
        page = response.read()
        htmlparser = etree.HTMLParser()
        print(self.url)
        self.tree = etree.parse(page, htmlparser)
        print(self.tree)
        for category,xpathselector in d.items():
            #print(category,xpathselector)
            #print(self.tree.xpath(xpathselector))
            setattr(self,category,self.tree.xpath(xpathselector))
        self.r = requests.get(self.url)
        self.source_code = BeautifulSoup(self.r.text)#
        self.emotions = dict(zip(emotions,[0 for i in range(len(emotions))])) #read in emoitions
        #self.update()


