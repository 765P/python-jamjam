from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('/Users/임재원/Downloads/chromedriver')
time.sleep(3)

while True:
	try:
		driver.get('http://kproxyx2.xyz')
		time.sleep(10)
		driver.find_element_by_name('url').send_keys('m.naver.com')
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="frm"]/form/input[2]').click()
		time.sleep(7)
		driver.find_element_by_class_name('sch_inp').send_keys('자라킹')
		time.sleep(2)
		driver.find_element_by_class_name('sch_inp').send_keys(Keys.ENTER)
		time.sleep(8)
		driver.find_element_by_link_text('더보기').click()
		time.sleep(5)
		driver.find_element_by_link_text('자라나는 자신감! 자라킹').click()
		time.sleep(10)
		driver.get('http://kproxyx2.xyz')
		time.sleep(8)
		driver.delete_all_cookies()
		time.sleep(15)
	except:
		continue