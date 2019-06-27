from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
driver.get('https://naver.com')
time.sleep(2)
driver.get('chrome://settings/clearBrowserData')
time.sleep(4)
driver.find_elements_by_name('more-actions').send_keys(Keys.ENTER)
time.sleep(2)