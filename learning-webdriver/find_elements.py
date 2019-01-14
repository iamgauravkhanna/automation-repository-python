from selenium import webdriver

# Launch Firefox Instance
driver = webdriver.Firefox(executable_path="C:\\office\\code\\workspace-python\\automation-repository-python\\drivers\\windows\\geckodriver-v0.23.0-win64\\geckodriver.exe")

# Assigning URL to variable 'baseUrl'
baseUrl = "http://book.theautomatedtester.co.uk"

# Open the link
driver.get(baseUrl)

# Maximize browser window
driver.maximize_window()

# Find Element

# Find element by id
driver.find_element_by_id('radiobutton').click()

# Find element by name
driver.find_element_by_name('radiobutton').click()

# Find element by linktext
driver.find_element_by_link_text('radiobutton').click()

# Find element by partial link text
driver.find_element_by_partial_link_text('partial').click()

# Find element by xpath
driver.find_element_by_xpath("//a[text()='a']").click()

# Find element by CSS
driver.find_element_by_css_selector("//a[text()='a']").click()

# Find element by class name
driver.find_element_by_class_name('alpha').click()

# Find element by tag
driver.find_element_by_tag_name('a').click()

# Find Elements

# Find elements by id
driver.find_elements_by_id('radiobutton').click()

# Find elements by name
driver.find_elements_by_name('radiobutton').click()

# Find elements by linktext
driver.find_elements_by_link_text('radiobutton').click()

# Find elements by partial link text
driver.find_elements_by_partial_link_text('partial').click()

# Find elements by xpath
driver.find_elements_by_xpath("//a[text()='a']").click()

# Find elements by CSS
driver.find_elements_by_css_selector("//a[text()='a']").click()

# Find elements by class name
driver.find_elements_by_class_name('alpha').click()

# Find elements by tag
driver.find_elements_by_tag_name('a').click()

# Quit Driver
driver.quit()