__author__ = 'Gaurav.Khanna'

from raftaar.manager.testDriverOld import TestDriver

class TestManager:

   def runTestCase(self,test_case_id):
       print("Test Case ID : " + test_case_id)
       testDriverObject = TestDriver()
       # tcid, summary, description, keyword, locator, value, data, iterations, flags):
       testDriverObject.runTestStep('click','click','click','openBrowser','click','click','http://wwww.google.com','click','click')
       TestDriver.DataDictionary["testManagerStatus"] = "SUCCESS"