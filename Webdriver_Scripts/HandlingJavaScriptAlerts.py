__author__ = 'Gaurav.Khanna'

from selenium import webdriver
from selenium import webdriver

#
webDriver = webdriver.Firefox()

#
webDriver.get("http://in.rediff.com")

#
webDriver.find_element_by_xpath("//*[@id='signin_info']/a[1]").click()

#
webDriver.find_element_by_xpath("//input[@id='btn_login']").click()

#
alert = webDriver.switch_to.alert

#
print(alert.text)

#
alert.accept()

#
alert.dismiss()