__author__ = 'Gaurav.Khanna'

from selenium import webdriver

# Declaring Variables
rowcount = 0

#
webDriver = webdriver.Firefox()

#
baseUrl = "http://www.espncricinfo.com/icc_cricket_worldcup2011/engine/match/473326.html"

#
webDriver.get(baseUrl)

#
webDriver.maximize_window()

# Storing the first part of xPath leaving the row number
start = "//*[@id='inningsBat1']/tbody/tr["

#Storing the last part of xPath leaving the row number
end = "]/td[2]"



for i in range(1,17):
    print(i)
    to_find = start + i + end
    result = webDriver.find_element_by_xpath(to_find).text
    print(result)
    rowcount+=1

print(rowcount)

webDriver.quit()
