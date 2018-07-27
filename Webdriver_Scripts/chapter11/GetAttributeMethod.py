__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk/chapter1"

# Open the link
webDriver.get(baseUrl)

# Locate Button and Store the value of button to 'attributeValue' variable
attributeValue = webDriver.find_element_by_id("verifybutton").get_attribute("value")

# Printing value of 'attributeValue'
print("Attribute Value : " + attributeValue)

# This will close the browser
webDriver.quit()