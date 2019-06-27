from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
time.sleep(3)
driver.get('http://kproxyx2.xyz')
time.sleep(2)

while True:
	driver.find_element_by_name('url').send_keys('m.naver.com')
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="frm"]/form/input[2]').click()
	time.sleep(7)
	driver.find_element_by_class_name('sch_inp').send_keys('자라환')
	time.sleep(5)
	driver.find_element_by_class_name('sch_submit').click()
	time.sleep(5)
	driver.find_element_by_link_text('더보기').click()
	time.sleep(3)
	driver.find_element_by_link_text('Shop 자라킹').click()
	time.sleep(7)
	driver.get('http://kproxyx2.xyz')
	time.sleep(5)
	driver.delete_all_cookies()
	time.sleep(3)