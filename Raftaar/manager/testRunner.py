__author__ = 'Gaurav.Khanna'

from Raftaar.testDriver.testDriver

class TestRunner:
   def runTestCase(self,test_case_id):
       print("Test Case ID : " + test_case_id)
       testDriverObject = testDriver()
       # tcid, summary, description, keyword, locator, value, data, iterations, flags):
       testDriverObject.runTestStep('click','click','click','openBrowser','click','click','http://wwww.google.com','click','click')