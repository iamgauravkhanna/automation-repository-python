from selenium import webdriver

# Launch Firefox Instance
driver = webdriver.Firefox(executable_path="C:\\office\\code\\workspace-python\\automation-repository-python\\drivers\\windows\\geckodriver-v0.23.0-win64\\geckodriver.exe")

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk"

# Set Time Out
driver.set_page_load_timeout(1)

# Open the link
driver.get(baseUrl)