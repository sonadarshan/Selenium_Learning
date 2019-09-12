# element not interactable error found because of multiple elements with the same name used array to resolve it
# webelemet is not subscritable use find_elemets_by name not find element by name
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.set_page_load_timeout(10)
browser.get("http://google.com")
browser.maximize_window()
browser.find_element_by_name('q').send_keys("Ambur Biriyani")
#browser.find_element_by_name('q').send_keys(Keys.ENTER)
browser.find_elements_by_name('btnK')[1].send_keys(Keys.ENTER)
time.sleep(4)
browser.quit()