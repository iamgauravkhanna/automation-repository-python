__author__ = 'Gaurav.Khanna'

import os
from selenium import webdriver

#
chromedriver = "C:\\Python34\\Scripts"

#
os.environ["webdriver.chrome.driver"] = chromedriver

#
webDriver = webdriver.Chrome(chromedriver)

#
baseUrl = "http://not-just-a-tester.blogspot.in"

#
webDriver.get(baseUrl)

#
webDriver.maximize_window()

#
webDriver.find_element_by_link_text("Selenium")

#
webDriver.close()
