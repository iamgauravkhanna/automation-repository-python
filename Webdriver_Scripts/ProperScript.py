__author__ = 'Gaurav.Khanna'

from selenium import webdriver

class ProperScript:

    def begin(self):
        self.driver = webdriver.Firefox()

    def end(self):
        self.driver.close()

    def test(self):
        rowcount = 0
        baseUrl = "http://www.espncricinfo.com/icc_cricket_worldcup2011/engine/match/473326.html"
        self.driver.get(baseUrl)
        self.driver.maximize_window()

TestDriver = ProperScript()
TestDriver.begin()
TestDriver.test()
TestDriver.end()