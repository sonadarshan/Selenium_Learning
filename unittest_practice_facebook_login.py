from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import unittest

class FacebookLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        co = Options()
        co.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(options=co)

        cls.driver.set_page_load_timeout(10)
        cls.driver.maximize_window()

    def test_right_login(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_name('email').send_keys('sona.ganga12@gmail.com')
        time.sleep(1)
        self.driver.find_element_by_name('pass').send_keys('Sona@2304')
        time.sleep(2)
        self.driver.find_element_by_name('pass').send_keys(Keys.ENTER)
        time.sleep(10)
        #self.driver.refresh()
        self.driver.find_element_by_id('userNavigationLabel').click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('_54nh')[11].click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=="__main__" :
    unittest.main()
