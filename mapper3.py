#!/usr/bin/env python3
#File: mapper3.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop

import sys
import re

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z0-9]+")
    while line:
    #for line in sys.stdin:
        for word in pattern.findall(line):
            print(''.join(sorted(word))+"\t"+"1")
        line = sys.stdin.readline()
if __name__ == "__main__":
    main(sys.argv)
