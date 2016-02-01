__author__ = 'Gaurav.Khanna'

class HelloWorldClass:
    employeeCount = 0

    def __init__(self,name):
        self.varName = name
        self.employeeCount+=1

    def printingMessage(self):
        print("Hello Grv")
        print(self.varName)
        print(self.employeeCount)

my = HelloWorldClass("Gaurav Khanna")
my.printingMessage()
my1 = HelloWorldClass("Gaurav Kumar")
my1.printingMessage()