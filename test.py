from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


op = Options()
op.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=op)
driver.minimize_window()
driver.set_page_load_timeout(30)
driver.get("https://www.nseindia.com/live_market/dynaContent/live_watch/pre_open_market/pre_open_market.htm")
select = Select(driver.find_element_by_id('selId'))
select.select_by_value('all')
time.sleep(30)
for tr in driver.find_elements_by_xpath("//*[@id='preOpenNiftyTab']/tbody/tr"):
    tds = tr.find_elements_by_tag_name('td')
    l = [td.text for td in tds]
driver.close()
driver.quit()

