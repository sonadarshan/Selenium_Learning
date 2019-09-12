from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('http://google.com')
driver.find_element_by_name('q').send_keys("Youtube")
driver.find_element_by_name('q').send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/h3').click()
time.sleep(4)
driver.find_element_by_id('search').send_keys("data structures")
driver.find_element_by_id('search').send_keys(Keys.ENTER)
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
search = 'bhanu priya'
for i in user_data:
    str = i.get_attribute('aria-label')
    if str == None:
        continue
    if(str.find(search)!= -1):
        print(i.get_attribute('href'))
        driver.get(i.get_attribute('href'))
        break
time.sleep(10)
driver.quit()





