from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

op = Options()
op.add_argument("--disable-notifications")
#user = input("Enter the user Id: ")
#password = input("Enter the password: ")
user = "FO9349"
password = "JaiSriRam@23"
pin = "280417"
driver = webdriver.Chrome(options=op)
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://kite.zerodha.com")
driver.find_element_by_xpath("//*[@id='container']/div/div/div/form/div[2]/input").send_keys(user)
driver.find_element_by_xpath("//*[@id='container']/div/div/div/form/div[3]/input").send_keys(password)
driver.find_element_by_xpath("//*[@id='container']/div/div/div/form/div[3]/input").send_keys(Keys.ENTER)
driver.minimize_window()
#pin = input("Enter the pin: ")
#driver.maximize_window()
driver.find_element_by_xpath("//*[@id='container']/div/div/div/form/div[2]/div/input").send_keys(pin)
driver.find_element_by_xpath("//*[@id='container']/div/div/div/form/div[2]/div/input").send_keys(Keys.ENTER)
time.sleep(2)
driver.minimize_window()
company = input("Enter the stock name : ")
driver.maximize_window()
#driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/ul/li[5]").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//*[@id='search-input']").send_keys(company)
driver.find_element_by_xpath("//*[@id='search-input']").send_keys(Keys.ENTER)
time.sleep(2)
element = driver.find_element_by_class_name("nice-name")
hover = ActionChains(driver).move_to_element(element).perform()
driver.find_element_by_class_name("buy").click()
# selecting MIS
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[1]/div[1]/div/div[1]/label").click()
# selecting limit
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[1]/div[2]/div/div[2]/label").click()
# selecting dropdown for choosing BO
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[3]/div[1]/a").click()
# selecting cover order
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[3]/div[1]/div[1]/div/div[3]/label").click()
# entering quantity
quantity = 1000
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[2]/div[1]/div/input").send_keys(quantity)
# entering entry price
entry = 108
for i in range(10):
    driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[2]/div[2]/div/input").send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[2]/div[2]/div/input").send_keys(entry)
# entering stop loss
sl = 104
for i in range(10):
    driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[2]/div[3]/div/input").send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[2]/div[3]/div/input").send_keys(sl)
# buying the order
driver.find_element_by_xpath("//*[@id='app']/div[3]/div/form/div[3]/div[3]/div[2]/button[1]").click()
element = driver.find_element_by_class_name("nice-name")
ActionChains(driver).move_to_element(element).perform()
driver.find_elements_by_class_name("button-outline")[2].click()
time.sleep(10)
driver.quit()




