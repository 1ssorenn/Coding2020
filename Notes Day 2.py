# LISTS
import random

my_names = ["Grangi", "Cormali", "Jaquamious", "Ja-moousee", "Skquank"]
my_numbers = [1, 2, 12, -5, 17]

# Indexing

print(my_names)
print(my_names[2])
print(my_names[-1])
print(my_names[:3])  # Everyone from 0-2
print(my_names[3:5])  # Everyone from 3-4
print(my_names[:])  # Everybody

# copy list
my_copy = my_names  # Nay bad bad bad ur stup
my_copy.append("Hubor")
print(my_copy)
print(my_names)
my_copy.append("Hal")
my_copy = my_names[:]  # Doo it this way!
print(my_copy)
print(my_names)

# 2d list
my_2d = [["ouch", "shid", "larva"], [8, "yort"], ["Quando", "se", "llavarme"]]
print(my_2d[1])  # Second list inside my_2d
print(my_2d[1][1])  # Second word inside second list inside my_2d
my_2d[1].append("skquank")
print(my_2d[1])


# if in
if "Hal" in my_names:
    print("You are gmaer")

# List functions
print(len(my_names))  # length, number of items
print(min(my_numbers))  # Lowest value
print(max(my_numbers))  # Highest value
print(sum(my_numbers))  # Adds them up


print(min(my_names))  # First in lexicon
my_names.append("Aa-ron")
print(min(my_names))


# List methods
print(my_names.index("Hal"))  # returns index of Hal
my_names.append("Hal")
print(my_names.index("Hal"))

my_names.append("Deb")
print(my_names)
del my_names[my_names.index("Aa-ron")]
print(my_names)
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)


# Modifying lists
del my_names[4]
print(my_names)

my_names.pop()
print(my_names)

end_of_list = my_names.pop()  # pops off and AND returns it
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0)  # pop by index
print(my_names)
print(front_of_list)

# Concatenation
first = "Ryan"
last = "Soren"
print(first, last)  #smooshed together

print(my_names + my_numbers)



# Iterating through lists
my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)



for item in my_list:
    item += 1
    print(item)

print(my_list)

for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)


# Same
my_list = [x + 1 for x in range(10)]
print(my_list)


# List comprehensions

# make list 0-100
my_list = []

for i in range(101):
    my_list.append(i)

print(my_list)

# Using list comprehension
# Output for item in loop
my_list = [x for x in range(101)]

print(my_list)


# Make a list 0-100 squared
my_list = []
for i in range(101):
    my_list.append(i ** 2)

print(my_list)


# List ocmprehension way
my_list = [x ** 2 for x in range(101)]
print(my_list)


# make a list of 1 - 100 squared, but filter out odd numbers
my_list = []

for i in range(101):
    if i ** 2 % 2 == 0:
        my_list.append(i ** 2)

print(my_list)

# List comprehension way
my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]

print(my_list)

# roll a single die 100 times and add it to a list
my_list = []

for i in range(100):
    my_list.append(random.randrange(1, 7))

print(my_list)


# List comprehension way
my_list = [random.randrange(1, 7) for x in range(101)]

print(my_list)

# roll 2 dice
my_list = []
for i in range(100):
    my_list.append([random.randrange(1, 7), random.randrange(1, 7)])

print(my_list)


# List comprehension way
my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]

print(my_list)


# go back through list adn make a new list of sums of two die
my_sums = [sum(x) for x in my_list]
print(my_sums)


# make a list from the 100 rolls that shows only the doubles

my_doubles = [x for x in my_list if x[0] == x[1]]

print(my_doubles)



# all at once
# roll 100 pairs and only put in the doubles
my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]

print(my_list)


# Working wiht strings is a lot like lists
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

for letter in first:
    print(letter)

if "N" in first:
    print("Yes")