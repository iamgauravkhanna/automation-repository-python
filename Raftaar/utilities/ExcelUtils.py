__author__ = 'Gaurav.Khanna'

import xlrd
import xlwt
#----------------------------------------------------------------------

class excelUtils:

    def __init__(self,path):
        self.workbook = xlrd.open_workbook(path)

    def open_file(path):
        book = xlrd.open_workbook(path)
        # print number of sheets
        print ("Number of Sheets : " + str(book.nsheets))
        # print sheet names
        print (book.sheet_names())
        # get the first worksheet
        first_sheet = book.sheet_by_index(0)
        # read a row
        print(first_sheet.row_values(0))
        # read a cell
        cell = first_sheet.cell(0,0)
        print (cell)
        print (cell.value)
        # read a row slice
        print (first_sheet.row_slice(rowx=0,
                                    start_colx=0,
                                    end_colx=2))



    def print_sheet_names(path):
        book = xlrd.open_workbook(path)
        # print number of sheets
        print (book.sheet_names())

    def find_sheet(path):
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_name('BasicScript')
        for row in range(sheet.nrows):
        #for row in range(0,2):
            for column in range(0,10):
                print("row::::: ", row)
                print("column:: ", column)
                print("value::: ", sheet.cell(row,column).value)

    def getSheetCount(self):
        sheet_names = self.workbook.sheet_names()
        print('Sheet Names', sheet_names)
        count = self.workbook.nsheets
        count = str(count)
        print("No. of Sheets : " + count)
        return count