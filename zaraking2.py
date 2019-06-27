from selenium import webdriver
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
time.sleep(3)
driver.get('https://naver.com')
time.sleep(2)

while True:
	driver.find_element_by_name('query').send_keys('자라킹')
	time.sleep(5)
	driver.find_element_by_class_name('ico_search_submit').click()
	time.sleep(5)
	driver.find_element_by_link_text('NAVER').click()
	time.sleep(5)
	