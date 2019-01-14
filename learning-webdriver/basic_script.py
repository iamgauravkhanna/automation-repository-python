from selenium import webdriver

# Launch Firefox Instance
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

# Click on link
driver.find_element_by_link_text('Chapter1').click()

# Click on radio button
driver.find_elements_by_id('radiobutton').click()

# Quit Driver
driver.quit()