from selenium import webdriver

# Launch Firefox Instance
driver = webdriver.Firefox(executable_path="C:\\office\\code\\workspace-python\\automation-repository-python\\drivers\\windows\\geckodriver-v0.23.0-win64\\geckodriver.exe")

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk/chapter2"

# Open the link
driver.get(baseUrl)

# Maximize browser window
driver.maximize_window()

# Get Element
element = driver.find_element_by_id('random')

# Print text of button
print('Text of Button : ' + element.get_attribute('value'))

# Quit Driver
driver.quit()