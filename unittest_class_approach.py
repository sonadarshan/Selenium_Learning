from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner


class GoogleSearch (unittest.TestCase):

    #There will be two classes setup(one sets everything for each test case) and setupclass(one sets up the beinning of the test case)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_page_load_timeout(10)
        cls.driver.maximize_window()

    def test_search_extreme(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name('q').send_keys("Extreme")
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        time.sleep(3)

    def test_search_networks(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name('q').send_keys("Networks")
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        time.sleep(3)

    #There will be two functions teardownclass and teardown the later runs everytime after a test case and the former onvce after all test cases
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


#To Run in cmd copy the path and <cd path> then <python -m unittest filename.py>

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sogangadhara/PycharmProjects/Selenium_Learning/Reports'))

#If I add the above then there is no need to use the -m flag just we can use python filename.py