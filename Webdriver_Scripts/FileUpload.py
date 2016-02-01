__author__ = 'Gaurav.Khanna'

from selenium import  webdriver

# Initializing FireFox Driver
webDriver = webdriver.Firefox()

# Assigning URL to variable 'baseUrl'
baseUrl = "http://www.htmlcodetutorial.com/forms/_INPUT_TYPE_FILE.html"

# Open the link
webDriver.get(baseUrl)

# Maximize browser window
webDriver.maximize_window()

# Upload File
webDriver.find_element_by_name("upfile").send_keys("C:\\gaurav\\gaurav.txt")

# Click on Submit Button
webDriver.find_element_by_xpath("//input[@value='Submit']").click()

#This will close the browser
webDriver.quit()