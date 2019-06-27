from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
driver.get('https://naver.com')
time.sleep(2)
driver.find_element_by_name('query').send_keys('자라킹')
time.sleep(2)
driver.find_element_by_name('query').send_keys(Keys.ENTER)
time.sleep(2)