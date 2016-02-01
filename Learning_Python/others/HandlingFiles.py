__author__ = 'Gaurav.Khanna'

fr = open("c://gaurav//gaurav.txt","ab+")


fr.write(bytes("Hello".encode("UTF-8")))

fr.close()

def sum1(a,b):
    return a+b

print(sum1(3,6))

import random2