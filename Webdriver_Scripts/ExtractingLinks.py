__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Open URL
webDriver.get("http://not-just-a-tester.blogspot.in/")

# Find all anchor tags
allLinks = webDriver.find_elements_by_tag_name("a")

# Print All Links
for links in allLinks:
    print(links.get_attribute('href'))
    print("\n")

# Close Browser
webDriver.close()