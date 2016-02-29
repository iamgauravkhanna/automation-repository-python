__author__ = 'Gaurav Khanna'

from Raftaar.manager.testManager import TestManager
from Raftaar.manager.testDriver import TestDriver

TestDriver.DataDictionary["browser"] = "firefox"
TestDriver.DataDictionary["testcaseid"] = "Selenium.RegisterUser()"
TestDriver.DataDictionary["DBConnection"] = "QA_DB_001"
TestDriver.DataDictionary["RemoteURL"] = "localhost"

TestCase001 = TestManager()
TestCase001.runTestCase("Selenium.RegisterUser()")

print(TestDriver.DataDictionary)