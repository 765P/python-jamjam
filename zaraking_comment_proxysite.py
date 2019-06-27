from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
time.sleep(5)
driver.get('https://www.proxysite.com/')
time.sleep(5)

while True:
	driver.find_element_by_name('d').send_keys('naver.com')
	time.sleep(2)
	driver.find_element_by_name('d').send_keys(Keys.ENTER)
	time.sleep(7)
	driver.find_element_by_name('query').send_keys('자라나는 자신감')
	time.sleep(2)
	driver.find_element_by_id('search_btn').click()
	time.sleep(10)
	driver.find_element_by_link_text('자라나는 자신감! 자라킹').click()
	time.sleep(10)
	driver.get('https://www.proxysite.com/')
	time.sleep(10)
	driver.switch_to_window(driver.window_handles[1]) 
	driver.get_window_position(driver.window_handles[1])
	time.sleep(10)
	driver.close()
	time.sleep(5)
	driver.switch_to_window(driver.window_handles[0]) 
	driver.get_window_position(driver.window_handles[0])
	time.sleep(5)
	driver.delete_all_cookies()
	time.sleep(5)