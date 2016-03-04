__author__ = 'Gaurav Khanna'

from Raftaar.manager.testManagerOld import TestManager
from Raftaar.manager.testDriverOld import TestDriver

TestDriver.DataDictionary["browser"] = "firefox"
TestDriver.DataDictionary["testcaseid"] = "Selenium.RegisterUser()"
TestDriver.DataDictionary["DBConnection"] = "QA_DB_001"
TestDriver.DataDictionary["RemoteURL"] = "localhost"

TestCase001 = TestManager()
TestCase001.runTestCase("Selenium.RegisterUser()")

print(TestDriver.DataDictionary)