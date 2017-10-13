#!/usr/bin/env python3
#File: reducer3.py
#Author: Maggie Schweihs
#DS730, Fall 2017
#Project2: Hadoop
#!/usr/bin/env python3

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
