from selenium import webdriver

#https://www.techbeamers.com/selenium-webdriver-python-tutorial/

driver = webdriver.Firefox(executable_path="C:\\office\\code\\workspace-python\\automation-repository-python\\drivers\\windows\\geckodriver-v0.23.0-win64\\geckodriver.exe")

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk"

# Open the link
driver.get(baseUrl)

# Maximize browser window
driver.maximize_window()

# Get Page Title
title = driver.title

# Print Page Title
print('Page Title :' + title)

# Quit Driver
driver.quit()