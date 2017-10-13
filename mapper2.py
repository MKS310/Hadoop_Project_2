#!/usr/bin/env python3
#File: mapper2.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop

import sys

def main(argv):
#read line from std in
    line = sys.stdin.readline()
    while line:
        line = line.split()
        for word in line:
            swaps = 0
        #Check if word has odd number of letters
            if len(word) % 2 != 0: 
                j = 1
                i = int(len(word)/2) 
        #Count how many swaps to make a palindrome by counting the letters that are not symmetrical about the middle letter.
                while j <= i:
                    if word[int(i + j)] != word[int(i-j)]:
                        swaps += 1
                        j += 1
                    else:
                        j += 1
        #Otherwise, word has even number of letters
            else:
                j = 0
                i = int(len(word)/2)
        #Count the number of swaps to make palindrome
                while j < i:
                    if word[int(i + j)] != word[int(i-j-1)]:
                        swaps +=1
                        j += 1
                    else:
                        j += 1
        #Output (key, value) as (word, swaps)
            print(str(swaps) + '\t' + word)
        line = sys.stdin.readline()
if __name__ == "__main__":
    main(sys.argv)

