__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Open the link
webDriver.get("http://www.google.com")

# Find search button
searchButton = webDriver.find_element_by_name("btnK")

# Printing 'name' attribute
print("Name of the button is: " + searchButton.get_attribute("name"))

# Printing 'id' attribute
print("Id of the button is: " + searchButton.get_attribute("id"))

# Printing 'class' attribute
print("Class of the button is: " + searchButton.get_attribute("class"))

# Printing 'custom' attribute
print("Label of the button is: " + searchButton.get_attribute("aria-label"))

# Close Browser
webDriver.close()