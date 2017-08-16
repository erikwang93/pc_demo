from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =  webdriver.Firefox(executable_path='/Users/erikwang/geckodriver')
driver.get('http://www.lairmey.com/login')

elem = driver.find_element_by_name('userName')
elem.send_keys('admin')
elem = driver.find_element_by_name('password')
elem.send_keys('Farewell2014')

elem = driver.find_element_by_name('commit')
elem.click()
#driver.close()