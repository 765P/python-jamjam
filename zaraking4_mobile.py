from selenium import webdriver
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
time.sleep(3)
driver.get('https://m.naver.com')
time.sleep(2)

while True:
	driver.find_element_by_class_name('sch_inp').send_keys('자라나는 자신감! 자라킹')
	time.sleep(5)
	driver.find_element_by_class_name('sch_submit').click()
	time.sleep(3)
	driver.find_element_by_link_text('자라나는 자신감! 자라킹').click()
	time.sleep(5)
	driver.get('https://m.naver.com')
	time.sleep(5)
	driver.delete_all_cookies()
	time.sleep(3)