__author__ = 'Gaurav.Khanna'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import select

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Assigning URL to variable 'baseUrl'
baseUrl = "http://www.webmath.com/"

# Wait for 30 seconds using Implicit Wait
WebDriverWait(webDriver,30)

# Open the link
webDriver.get(baseUrl)

# Click on element
webDriver.find_element_by_id("www-content-wrap").click()

# Select `Simple Interest` option from drop down
select.Select(webDriver.find_element_by_id("topicItem")).select_by_visible_text("Interest, Simple")

# Click on element
webDriver.find_element_by_css_selector("option[value=\"simpinterest.html\"]").click()

# Clear Field
webDriver.find_element_by_name("principal").clear()

# Enter value
webDriver.find_element_by_name("principal").sendKeys("1000")

# Clear Field
webDriver.find_element_by_name("interest").clear()

# Enter value
webDriver.find_element_by_name("interest").send_keys("1")

# Clear Field
webDriver.find_element_by_name("desired_time").clear()

# Enter value
webDriver.find_element_by_name("desired_time").send_keys("5")

# Click on element
webDriver.find_element_by_name("//input[@value='Find the amount of interest']").click()

# Close Browser
webDriver.close()