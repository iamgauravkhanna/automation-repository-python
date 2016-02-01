__author__ = 'Gaurav.Khanna'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#
print("Hello. How are you ?")

#
webDriver = webdriver.Firefox()

#
webDriver.get("http://not-just-a-tester.blogspot.in/")

#
WebDriverWait(webDriver,60)

#
print("I am good!!!")

#
webDriver.close()
