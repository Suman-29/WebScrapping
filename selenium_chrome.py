import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:/Python_work/chromedriver_win32/chromedriver.exe')
#driver = webdriver.Chrome('C:\Users\Anurag\Python_workchromedriver_win32')  # Optional argument, if not specified will search path.
driver.get('https://clutch.co/directory/mobile-application-developers')
driver.wait = WebDriverWait(driver,2000)
links_list = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/h3/a')
for link in links_list:
	link.click()
	box = driver.wait.until(lambda driver: driver.find_elements_by_xpath('//*[@id="summary"]/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/p[1]')).text()
	print(box)
	driver.back()

	
'''search_box.send_keys('Wondering, whether ghosts are really there?')
search_box.submit()
time.sleep(10) # Let the user actually see something!
driver.quit()'''
