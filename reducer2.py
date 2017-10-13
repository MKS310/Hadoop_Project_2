#!/usr/bin/env python3
#File: reducer2.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop
#!/usr/bin/env python3
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
    #line = sys.stdin.readline()
    curr_words = []
    curr_swaps = None
    #if line:
    #    curr_swaps, word = line.split('\t')
    #    curr_words.append(word.strip())
    #else:
     #   line = sys.stdin.readline()
      #  curr_swaps, word = line.split('\t')
       # curr_words.append(word.strip())
    #Create a list of words for each key
    #curr_words = []
    for line in sys.stdin:
        swaps, word = line.split('\t')
    #If the key is the same, add the word to the list
        if curr_swaps == swaps or curr_swaps == None:
            curr_words.append(word.strip())
            curr_swaps = swaps
            #line = sys.stdin.readline()
    #Otherwise, print the key and the word list for the previous key. Reinitialize vars
        else:
            if curr_swaps:
                print(curr_swaps + ' : ' + ','.join(str(s) for s in curr_words))
            curr_swaps = swaps
            curr_words = [word.strip()]
            #line = sys.stdin.readline()
    #Print the last key, value
    if curr_swaps:
        print(curr_swaps + ' : ' + ','.join(str(s) for s in sorted(curr_words)))
if __name__ == "__main__":
    main(sys.argv)
