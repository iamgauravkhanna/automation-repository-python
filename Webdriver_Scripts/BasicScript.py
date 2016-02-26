__author__ = 'Gaurav.Khanna'

from selenium import webdriver
from selenium.webdriver.support import select

import

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk"

# Open the link
webDriver.get(baseUrl)

# Maximize browser window
webDriver.maximize_window()

# Click on link
webDriver.find_element_by_link_text("Chapter1").click()

# Click on Radio Button
webDriver.find_element_by_id("radiobutton").click()

# Locate drop down
element = select.Select(webDriver.find_element_by_id("selecttype"))

# Select option from drop down
element.select_by_visible_text("Selenium Core")

# Verify Text Present
assert "Assert that this text is on the page" in webDriver.find_element_by_id("divontheleft").text

# Verify Button Present
assert "Verify this button he here" in webDriver.find_element_by_id("verifybutton").get_attribute('value')

# Close Browser
webDriver.close()