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
    curr_cust = None
    curr_key = None
    curr_amt = 0
    customers = []

    for line in sys.stdin:
        line = line.split('\t')
    #key is month,country
        key = line[0].strip()
    #values has two values: custID, amount spent on an invoice
        values = line[1].split(',')
        cust = values[0].strip()
        amt = float(values[1].strip())     
    #First pass and when working on current key
        if curr_key == key or curr_key == None:
        #First pass and when working on current customer, update total amount spent per customerID "curr_amt"
            if curr_cust == cust or curr_cust == None:
                curr_amt = curr_amt + amt
                curr_cust = cust
                curr_key = key
        #When gets to the next custID, add the previous custID and customer total to the list customers
            else:
                customers.append([curr_amt, curr_cust])    
                curr_cust = cust
                curr_amt = amt
                curr_key = key
        #When gets to the next month,country combo, print the results of the previous month, country
        #Results: (key   value) = (month,country   bigspender_custID)
        #eg. 5,Canada   17443
        elif curr_key != key or len(customers) == 1 :
            customers.append([curr_amt, curr_cust])
            print(curr_key + '\t' + max(customers)[1])
            curr_cust = cust
            curr_amt = amt
            curr_key = key
            customers = [[amt, cust]]
    #Process and print after the last line of input 
    if curr_key == key:
        if curr_cust == cust:
            curr_amt = curr_amt + amt
            customers.append([curr_amt, curr_cust])
            print(key + '\t' + max(customers)[1])
        else:
            customers = [[amt, cust]]
            print(key + '\t' + max(customers)[1])
if __name__ == "__main__":
    main(sys.argv)
