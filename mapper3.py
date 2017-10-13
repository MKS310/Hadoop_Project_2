#!/usr/bin/env python3
#File: mapper3.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop
#Decription: 
# Assume you work for a pet store and you want to know where to spend your marketing money. 
# A “pet census” was sent to all cities in your area. Each city compiled the data and sent you the results. 
# Each city compiled the data in different ways but they all followed a basic rule. 
# For each citizen, a string appears in the file with the following information:
#
# a.  If the citizen owns 3 cats, 3 C’s show up in the string.
# b.  If the citizen owns 2 dogs, 2 D’s show up in the string.
# c.  If the citizen owns 4 fish, 4 F’s show up in the string.
# d.  If the citizen owns 1 monkey, 1 M shows up in the string.
#
# For example, the citizen with 3 cats, 2 dogs, 4 fish and 1 monkey might appear as CCCDDFFFFM. 
# However, another city may have compiled their information differently and have CCDFDFCFMF. 
# Your goal is to print out how many citizens have the exact same number of pets. 
# For example, assume this is the input file:
#             CCDFM CDCDM FFDM FMDCC CDMFC MDFF
# Your output would be:
#                CCDFM : 3
#                CCDDM : 1
#                DFFM : 2
################################################################################################

import sys
import re

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z0-9]+")
    while line:
    #for line in sys.stdin, process each word (string ):
        for word in pattern.findall(line):
    #Output the string of pet info with letters of the string sorted, followed by '1'
            print(''.join(sorted(word))+"\t"+"1")
        line = sys.stdin.readline()
if __name__ == "__main__":
    main(sys.argv)
