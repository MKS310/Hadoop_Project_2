#!/usr/bin/env python3
#File: mapper2.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop
#
# Description:
# Palindromes are important in the field of computational biology. 
# The characteristic we are interested in is called palindromedness (not a word). 
# Palindromedness is defined as the minimum number of edits that must happen to a word in order to make it a palindrome. 
# The palindrome that is created with the edits need not be an actual word. An edit can be any of the following:
#   i.  Removing a letter in any spot.
#  ii.  Adding a letter in any spot.
# iii.  Replacing a letter in any spot with any other letter.
#
# We’ll define it as p(X) where X is some word. For example, p(“cat”) == 1. 
# If you replace ‘c’ with ‘t’ the word becomes “tat” and that word is a palindrome. 
# You can mix and match edits to get a palindrome. 
# In general, p(someWord) == k if there are k edits of any type that turn someWord into a palindrome and 
# no sequence of (k-1) edits can turn someWord into a palindrome. 
# Your goal is this:
# calculate the palindromedness of every word that is passed in and group words in the output by their palindromedness value. 
# For example, assume the input is:
#
# hello this is a test
#
# The output would be:
#
# 0 : a
# 1 : is, test
# 2 : hello, this
#
# The words on the righthand side must be in alphabetical order. You can assume that the words will contain only letters. 
# However, they may be upper or lowercase and that should not affect the palindromedness. 
# For example, Tat is a palindrome even though ‘T’ is not identical to ‘t’ but they are the same letter. 
# There will be no numbers or special symbols in the input. 
# All words will be separated by whitespace (either a space, tab or newline). 
# Your output should be what you see above. 
###############################################################################################################################


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

