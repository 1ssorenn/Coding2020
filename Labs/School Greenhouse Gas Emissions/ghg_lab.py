
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''

import csv
import matplotlib.pyplot as plt
import numpy as np
import requests
color = []
valid_data = []
names = []
url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD"




# Def get info
def rec_info(url):
    with requests.Session() as s:
        d = s.get(url)
        c = d.content.decode('utf-8')
        r = csv.reader(c.splitlines(), delimiter=',')
        my_list = list(r)
    return my_list
info = rec_info("https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")
header = info.pop(0)
print(header)

# Index
index1 = header.index("Total GHG Emissions (Metric Tons CO2e)")
index2 = header.index("Primary Property Type")
index3 = header.index("Gross Floor Area - Buildings (sq ft)")

# find valid data
for building in info:
    try:
        int(building[index1])
        int(building[index3])
        name = building[2]
        if building[0] == "2018" and building[index2] == "K-12 School":
            valid_data.append(building)
            names.append(name)
    except:
        pass

plt.figure(1, tight_layout=True)


ghg = [int(x[index1]) for x in valid_data]
ghg.sort()

space = [int(x[index3]) for x in valid_data]
space.sort()




p = np.polyfit(space, ghg, 1)
print(p)

x = [x for x in range(450000)]
y = [p[0] * y + p[1] for y in x]
plt.plot(x, y, c="black")
plt.xlabel("Gross Floor Area (sq ft)")
plt.ylabel("Total GHG Emissions (Metric Tons CO2e)")
plt.title("Emissions vs. Square Footage in Chicago Schools (2018)")
for name in names:
    if name == "Latin School of Chicago Upper School":
        name_index = names.index(name)
        plt.annotate("Latin", xy=(space[name_index], ghg[name_index]))



ten_percent = int(len(ghg) * 0.1)

ghg_bottom10 = [x for x in ghg[:ten_percent]]
ghg_top10 = [x for x in ghg[-ten_percent:]]
print(ghg_top10)
print(ghg_bottom10)


# Set for Color of points
for building in ghg:
    if building in ghg_top10:
        color.append("red")
    elif building in ghg_bottom10:
        color.append("green")
    else:
        color.append("blue")
plt.scatter(space, ghg, alpha=0.5, c=color)
plt.show()
