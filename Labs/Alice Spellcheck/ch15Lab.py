'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Globals
with open('dictionary.txt') as f:
    dict_list = [x.strip().upper() for x in f]

alice200 = open("AliceInWonderLand200.txt")
dict = open('dictionary.txt')
words = []

def Linear():
    print("--- LINEAR SEARCH ---")
    line_num = 0
    for line in alice200:
        line_num += 1
        words = split_line(line.strip())
        for word in words:
            checked = False
            there = 0
            while not checked:
                for w in dict_list:
                    if w == word.upper():
                        there += 1
                if there == 0:
                    print("The word", word, "on line", line_num, "wasn't found in the dictionary")
                checked = True
alice200.close()
dict.close()



alice200 = open("AliceInWonderLand200.txt")
dict = open('dictionary.txt')


def Binary():
    print("--- BINARY SEARCH ---")
    line_num = 0
    for line in alice200:
        line_num += 1
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            found = False
            lower_bound = 0
            upper_bound = len(dict_list) - 1
            while lower_bound <= upper_bound and not found:
                middle_pos = (upper_bound + lower_bound) // 2
                if dict_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dict_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("The word", word, "on line", line_num, "wasn't found in the dictionary")


Linear()
Binary()

alice200.close()
dict.close()

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

