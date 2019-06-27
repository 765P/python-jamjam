from selenium import webdriver
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')

driver.get('https://naver.com')
time.sleep(3)
driver.get('https://naver.com')