__author__ = 'Gaurav.Khanna'

import xlrd

#----------------------------------------------------------------------

def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
    # print number of sheets
    print (book.nsheets)
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

#----------------------------------------------------------------------

if __name__ == "__main__":
    path = r'C:\GK\Python\Raftaar\testData\testcase.xlsx'
    print_sheet_names(path)
    find_sheet(path)