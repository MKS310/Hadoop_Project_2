#File: reducer1.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop

import sys
def main(argv):
    curr_cust = None
    curr_key = None
    curr_amt = 0
    customers = []

    for line in sys.stdin:
        line = line.split(':')
        key = line[0]
        values = line[1].strip().split(',')
        amt = float(values[1])
        cust = values[0]
        if curr_key == key or curr_key == None:
            if curr_cust == cust or curr_cust == None:
                curr_amt =+ amt
                curr_cust = cust
            else:
                customers.append([curr_amt, cust])    
                curr_cust = cust
                curr_amt = amt
            curr_key = key
        else:
            print(key + "\t" + max(customers)[1])
            customers = [[amt, cust]]
            curr_key = key
if __name__ == "__main__":
    main(sys.argv)
