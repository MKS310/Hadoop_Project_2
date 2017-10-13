#!/usr/bin/env python3 
# 
# File: reducer1.py
# Author: Maggie Schweihs
# DS730, Fall 2017
# Project2: Hadoop
# Description: 
# Assume you work for a large business and have access to all orders made in any given time period.
# Download the orders.csv file from http://www.uwosh.edu/faculty_staff/krohne/ds730/orders.csv). 
# Find the big spenders for each month and country. 
# 
# Your goal is this: for each month/country combination, 
# display the customerID of the top spender for that month/country combination. 
# The amount spent in each row is determined by multiplying the Quantity by the UnitPrice. 
# A few caveats:
# a.  The InvoiceDate is in Month/Day/Year format.
# b.  An InvoiceNo that starts with a C is a return. You must ignore these rows.
# c.  A row may not have a CustomerID. These rows must be ignored.
# d.  I am not looking for month/year/country combinations here. 
# There are two years worth of data and I am only interested in the month and country.
#
# This final output file should contain the following data:
#
# Month,Country : CustomerID
#
# It should be sorted by month first. If the months are the same, then sort them by country second. 
# If there is a tie, you can print out either customer or you can print out all of them who tied.
########################################################################################################

import sys

def main(argv):
#read line from std in
    #line = sys.stdin.readline()

    for line in sys.stdin:
        line = line.split(',')
        custID = line[6]
        InvoiceNo = line[0]
    #Check if there is no Customer ID, if order is a return, 
    #or if it is the header row. If so, skip
        if not custID or InvoiceNo[0].isalpha():
            continue
    #Otherwise, parse the line
        else:    
            country = line[7]
        #date[0] is the month
            date = line[4].split('/')
        #amtSpent = Qty * Price
            amtSpent = float(line[3]) * float(line[5])
        #Print <key, value> where key is month , country and value is customerID , amountSpent
        # eg. 5,Canada  17443,534.24
            print(str(date[0]) +  " , " + country.strip() + '\t' + custID + " , " + str(amtSpent))
if __name__ == "__main__":
    main(sys.argv)

