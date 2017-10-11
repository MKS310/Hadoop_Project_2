#File: reducer2.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop
#!/usr/bin/env python3

import sys

def main(argv):
    line = sys.stdin.readline()
    curr_swaps, word = line.split('\t')
    #Create a list of words for each key
    curr_words = []
    while line:
        swaps, word = line.split('\t')
    #If the key is the same, add the word to the list
        if curr_swaps == swaps or curr_swaps == None:
            curr_words.append(word.strip())
            line = sys.stdin.readline()
    #Otherwise, print the key and the word list for the previous key. Reinitialize vars
        else:
            if curr_swaps:
                print(curr_swaps + ' : ' + ','.join(str(s) for s in curr_words))
            curr_swaps = swaps
            curr_words = [word.strip()]
            line = sys.stdin.readline()
    #Print the last key, value
    if curr_swaps == swaps:
        print(curr_swaps + ' : ' + ','.join(str(s) for s in sorted(curr_words)))
if __name__ == "__main__":
    main(sys.argv)
