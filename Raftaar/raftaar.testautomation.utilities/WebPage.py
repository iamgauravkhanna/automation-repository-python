from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import select

class WebPageActions:

    def begin(self):
        self.driver = webdriver.Firefox()

    def click(self,locator):
        self.driver.find_element_by_id(locator).click()

    def end(self):
        self.driver.close()