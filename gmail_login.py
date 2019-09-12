from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.set_page_load_timeout(10)
browser.get("https://kite.zerodha.com")
browser.find_ele