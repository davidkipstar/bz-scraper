from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from BeautifulSoup import BeautifulSoup


bz_url = 'http://www.bz-berlin.de/berlin/charlottenburg-wilmersdorf/jugendamt-nahm-ihr-das-baby-weg-weil-sie-an-epilepsie-leidet'
browser = '/usr/bin/firefox'
binary = FirefoxBinary(browser)	#path of Firefox.exe

#start driver
driver = webdriver.Firefox(firefox_binary=binary)#,executable_path = geckodriver)
driver.get(bz_url)
#widget_id = 'iframe-widget'
#widget2_id = 'vcFeelbackWidget'
#content = driver.find_element_by_id(widget_id)
#content2 = driver.find_element_by_class_name(vc-feelback-title-wrapper)

#wuetend  = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div")
#wuetend  = driver.find_element_by_xpath('//*[@id="iframe-widget"]')
#widget = driver.find_element_by_xpath('//*[@id="vcFeelbackWidget"]')
widget = driver.find_element_by_xpath('//*[@id="vc-feelback-main"]')
widget2  = driver.find_element_by_xpath('//*[@id="iframe-widget"]')

#wue//*[@id="vc-feelback-main"]tend_css = driver.find_element_by_css_selector('html.no-js body div#vcFeelbackWidget.ng-scope.ng-animate.ltr.bz-berlin div.vc-feelback-container.show div.vc-feelback-categories.ng-scope div.vc-feelback-category.ng-scope div.vc-feelback-category-stats.ng-scope.ng-binding')
print(wuetend)
print(wuetend.text)
driver.close()

# Wait for the dyna//*[@id="iframe-widget"]mically loaded elements to show up
 #class="vc-feelback-category-stats ng-scope ng-binding"