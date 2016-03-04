__author__ = 'Gaurav.Khanna'

from Raftaar.manager.testManager import TestManager

class TestDriver:

    def runTestCase(self,test_case_id):

       print("Test Case ID : " + test_case_id)

       testManagerObject = TestManager()

       # tcid, summary, description, keyword, locator, value, data, iterations, flags):
       #testManagerObject.runTestStep('click','click','click','openBrowser','click','click','http://wwww.google.com','click','click')

       #TestManager.DataDictionary["testManagerStatus"] = "SUCCESS"

       createTestCaseMap(self)
       createTestDataMap(self)

    def createTestCaseMap(self):
        print("This is createTestCaseMap Method")

    def createTestDataMap(self):
        print("This is createTestData Method")

    def getTestCaseDetails(self):
        print("This is getTestCaseDetails Method")

    def getTestDataDetails(self):
        print("This is getTestDataDetails Method")

    def executeTestCase(self):
        print("This is executeTestCase Method")