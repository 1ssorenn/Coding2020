'''
Sorting and Intro to Big Data Problems (22pts)
Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

from NBAStats import *



#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
gamer = data.pop(0)
print(gamer)
#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
topten =[[i[-1], i[2]] for i in data]
topten.sort(reverse=True, key=lambda a: a[0])
for i in topten[:10]:
    print(i[1], "points", i[0])


print("\n\n")

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
pos = 0
points = 0
for i in range(1, len(data)):
    pos += 1
    if data[i][2] == "Kobe Bryant":
        points += data[i][-1]

print("Kobe scored:")
print(points)
# 4  What player has the most 3point field goals in a single season. (3pts)
field = [[i[-19], i[2]] for i in data]
field.sort(reverse=True, key=lambda a: a[0])
best = field[0]
pt3 = best[0]
name = best[1]
print("\n")
print(name, "scored", pt3, "three point field goals.")



#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)


wsfe = sorted(data, key=lambda a: a[25])

for item in wsfe:
    save = item
    if item <= save:
        ea = item
    else:
        item = save

print("\n\nHighest WS/48:", ea[2], ea[25])

#6  Who is the oldest player of all time?" (4pts)

age = sorted(data, key=lambda a: a[4])

for item in age:
    save = item
    if item <= save:
        ea = item
    else:
        item = save

print("\n")
print(ea[2], "age", ea[4])
#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)

pts = sorted(data, key=lambda a: a[-1])

tophun = pts[-100:]

fpt = sorted(tophun, key=lambda a: a[43])
my_list = []

for item in fpt:
    x = [item[2], item[43]]
    my_list.append(x)

print("\n\nBest free throw percentage", my_list[-1])
print("Worst free throw percentage", my_list[0])