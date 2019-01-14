__author__ = 'Gaurav.Khanna'

from selenium import webdriver

class TestDriver:

    DataDictionary={}

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print("Initializing Object")

    def runTestStep(self,tcid, summary, description, keyword, locator, value, data, iterations, flags):
        print("Running Test Case")
        self.runTestStep1(keyword,data)
        self.driver.quit()

    def runTestStep1(self,keyword,data):
        if keyword == "click":
            print ("click")
        elif keyword == "type":
            print("type")
        elif keyword == "openBrowser":
            print("open browser")
            self.driver.get("http://www.hcentive.com")
            TestDriver.DataDictionary["testDriverStatus"] = "SUCCESS"
        else:
            print("Hard Luck")