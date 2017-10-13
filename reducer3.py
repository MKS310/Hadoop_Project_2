#!/usr/bin/env python3
#File: reducer3.py
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
#
# This script works exactly the same as a word counter.
################################################################################################

import sys

def main(argv):
    current_word = None
    current_count = 0
    word = None
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        count = int(count)
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(current_word + ':' + str(current_count))
            current_count = count
            current_word = word
    if current_word == word:
        print(current_word + ':' + str(current_count))
if __name__ == "__main__":
    main(sys.argv)
