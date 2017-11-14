import os
from selenium import webdriver

chromedriver = "/usr/local/bin/chromedriver"
#

os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()