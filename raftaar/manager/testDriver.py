__author__ = 'Gaurav.Khanna'

from raftaar.manager.testManager import TestManager
import xlrd
import xlwt
import os
from raftaar.utilities.ExcelUtils import excelUtils

class TestDriver:

    TestCaseStepDetails={}
    TestCaseSteps={}

    def runTestCase(self,test_case_id):

        print("Test Case ID : " + test_case_id)
        self.createTestCaseMap()

    def createTestCaseMap(self):
        #print("Hello Test Case")
        path = "C:\\Python\\automationrepositorypython\\raftaar\\assets\\testcase.xlsx"
        ExcelObject = excelUtils(path)
        #excelUtils.open_file(path)
        sheetCount = ExcelObject.getSheetCount()
        #print("Main Sheet Count : " + sheetCount)
        sheetCount = int(sheetCount)
        for x in range(0,sheetCount):
            sheetName = ExcelObject.workbook.sheet_names()
            sheetNameValue = str(sheetName[x])
            sheetNameValue.strip()
            print("Sheet Name is : " + sheetNameValue)
            if(sheetNameValue == "Sheet1"):
                print("Sheet Found")
                y = 0
                sheet = ExcelObject.workbook.sheet_by_name("Sheet1")
                print("No. of Rows : ")
                rowCount = sheet.nrows
                print(rowCount)
                for row in range(1,rowCount):
                    self.TestCaseStepDetails["testcaseid"] = str(sheet.cell(row,0).value)
                    self.TestCaseStepDetails["summary"] = str(sheet.cell(row,1).value)
                    self.TestCaseStepDetails["description"] = str(sheet.cell(row,2).value)
                    self.TestCaseStepDetails["parent"] = str(sheet.cell(row,3).value)
                    self.TestCaseStepDetails["object"] = str(sheet.cell(row,4).value)
                    self.TestCaseStepDetails["action"] = str(sheet.cell(row,5).value)
                    self.TestCaseStepDetails["data"] = str(sheet.cell(row,6).value)
                    self.TestCaseStepDetails["iterations"] = str(sheet.cell(row,7).value)
                    self.TestCaseStepDetails["flags"] = str(sheet.cell(row,8).value)
                    #print(self.TestCaseStepDetails)
                    #for column in range(0,9):
                    #print("row::::: ", row)
                    #print("column:: ", column)
                    #print("value::: ", sheet.cell(row,column).value)
                    self.TestCaseSteps[row]=self.TestCaseStepDetails
                    print(self.TestCaseSteps)
            else:
                print("Boo...")