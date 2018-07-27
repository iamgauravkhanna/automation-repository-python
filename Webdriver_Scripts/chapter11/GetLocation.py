__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Open the link
webDriver.get("http://www.google.com")

# Find search button
searchButton = webDriver.find_element_by_name("btnK")

# Store cordinates in 'location' variable
location = searchButton.location

# Printing Location
print(location)

# Close Browser
webDriver.close()