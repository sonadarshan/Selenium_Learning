from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.minimize_window()
driver.get("hhtps://www.google.com")
time.sleep(4)
driver.find_element_by_name('q').send_keys("Extreme networks")
driver.find_element_by_name('q').send_keys(Keys.ENTER)
