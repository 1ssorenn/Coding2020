'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
file = open('dictionary.txt', 'r')

x = 0
winner = 0
dictionary_file = open('dictionary.txt', 'r')
for word in dictionary_file:
    if len(word) >= x:
        x = len(word)
        winner = word

print(winner)



# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
total = 0
avg_length = 0
alice_file = open('AliceInWonderLand.txt', 'r')
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)

    for word in words:
        total += 1
        avg_length += (len(word))

print(total)
print(avg_length // total)



# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_file = open('AliceInWonderLand.txt', 'r')
count = 0
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word.upper() == "Alice".upper():
            count += 1
print(count)
# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt
from collections import Counter



alice_file = open('AliceInWonderLand.txt', 'r')
sevens = []
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if len(word) == 7:
            sevens.append(word)

def most_fre(List):
    occ = Counter(List)
    return occ.most_common(1)[0][0]

print(most_fre(sevens))

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
alice_file = open('AliceInWonderLand.txt', 'r')
count = 0
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word.upper() == "Cheshire".upper():
            count += 1
print(count)

file.close()
# How many times does "Cat" occur?
alice_file = open('AliceInWonderLand.txt', 'r')
count = 0
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word.upper() == "CAT".upper():
            count += 1
print(count)
# How many times does "Cheshire" immediately followed by "Cat" occur?
file.close()
count = 0
current_word = 0
a_list = []
alice_file = open('AliceInWonderLand.txt', 'r')
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        a_list.append(word)
        if current_word <= len(a_list) - 2:
            if a_list[current_word] == "Cheshire".upper():
                if a_list[current_word + 1] == "Cat".upper():
                    count += 1
        else:
            break
print(count)

file.close()

