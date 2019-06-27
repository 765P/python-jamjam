from selenium import webdriver
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
driver.implicitly_wait(5)
driver.get('https://naver.com')
driver.implicitly_wait(2)

while True:
	time.sleep(10)
	driver.find_element_by_name('query').send_keys('자라킹')
	time.sleep(10)
	driver.find_element_by_class_name('ico_search_submit').click()
	time.sleep(10)
	driver.find_element_by_class_name('go_more').click()
	time.sleep(10)
	driver.find_element_by_link_text('자라나는 자신감! 자라킹').click()
	time.sleep(10)
	last_tab = driver.window_handles[0]
	driver.switch_to.window(window_name=last_tab)
	time.sleep(10)
	driver.get('https://naver.com')
	time.sleep(10)
	