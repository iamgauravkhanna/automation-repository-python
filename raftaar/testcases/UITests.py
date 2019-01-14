__author__ = 'Gaurav Khanna'

from raftaar.manager.testManager import TestManager
from raftaar.manager.testDriver import TestDriver

# Before Starting Test Case
TestManager.DataDictionary["browser"] = "firefox"
TestManager.DataDictionary["testcaseid"] = "Selenium.RegisterUser()"
TestManager.DataDictionary["DBConnection"] = "QA_DB_001"
TestManager.DataDictionary["RemoteURL"] = "localhost"

# Test Case
TestCase001 = TestDriver()
TestCase001.runTestCase("Selenium.RegisterUser()")

# After Completing Test Case
print("Data Dictionary Key - Value : ")
print(TestManager.DataDictionary)