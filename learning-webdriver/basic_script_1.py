from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys 

#https://www.techbeamers.com/selenium-webdriver-python-tutorial/

driver = webdriver.Firefox(executable_path="C:\\office\\code\\workspace-python\\automation-repository-python\\drivers\\windows\\geckodriver-v0.23.0-win64\\geckodriver.exe")

driver.get("http://www.google.com")

driver.quit()