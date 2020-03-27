'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
    I see a declining trend in the ridership of the CTA. I believe this is happening because of the new virtual world we live in so many people don't need to be taking public transportation as often. Also in the recent times, the coronavirus will decrease CTA ridership.
'''

import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)
# headers
header = data.pop(0)
print(header)
# Title
plt.title("CTA Ridership over the last 10 years", fontsize=14)

# Axes
plt.xlabel('Years')
plt.ylabel('Ridership')

# Data
data.sort(key=lambda x: int(x[0]))
min_ten = data[-11:]
years = [int(x[0]) for x in min_ten]
rail = [int(x[3]) for x in min_ten]
bus = [int(x[1]) for x in min_ten]
tot = [int(x[4]) for x in min_ten]
plt.plot(years, rail, color='red', marker='*', label='Rail')
plt.plot(years, bus, color='grey', marker='*', label='Bus')
plt.plot(years, tot, color='blue', marker='*', label='Total')
plt.xticks(years, rotation=45)

# Legend
plt.legend()

plt.show()


# pop header
# get last 10 years (years)
# get last 10 years bus
# get last 10 years rail
# get last 10 years total

# plot bus
# plot rail
# plot total

# axis
# labels
# title
# legend (label plots)

# show plot