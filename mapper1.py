#File: mapper1.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop

import sys
from decimal import Decimal

def main(argv):
#read line from std in
    line = sys.stdin.readline()

    while line:
        line = line.split(',')
        custID = line[6]
    #Check if there is no Customer ID
        if custID == '':
            line = sys.stdin.readline()
    #Check if the order is a return or if header row
        elif custID[0].isalpha():
            line = sys.stdin.readline()
    #Otherwise, parse the line
        else:    
            country = line[7]
        #date[0] is the month
            date = line[4].split('/')
        #amtSpent = Qty * Price
            amtSpent = Decimal(line[3]) * Decimal(line[5])
            print(str(date[0]) +  "," + country.strip() + " : " + custID + "," + str(amtSpent))
            line = sys.stdin.readline()
if __name__ == "__main__":
    main(sys.argv)

