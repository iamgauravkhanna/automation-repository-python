__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk"

# Open the link
webDriver.get("http://book.theautomatedtester.co.uk")

# Maximize browser window
webDriver.maximize_window()

# Click on link
webDriver.find_element_by_link_text("Chapter1").click()

# Print Page Title
print(" Page Title : " + webDriver.title)

# Using Back Method
webDriver.back()

# Print Page Title
print(" Page Title : " + webDriver.title)

# Using Forward Method
webDriver.forward()

# Print Page Title
print(" Page Title : " + webDriver.title)

# This will close the browser
webDriver.quit()