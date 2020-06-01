import matplotlib.pyplot as plt
import csv

# Variables
topgames = []
sales = []
pos = [1, 2, 3, 4, 5]

# Data
with open("vgsalesGlobale.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
names = [x[1] for x in data]
data = [x[-1] for x in data]



# Change to new list
for i in range(5):
    new = names.pop(0)
    new2 = data.pop(0)
    sales.append(new2)
    topgames.append(new)

# Plot creation
plt.figure(1)

# Visuals
plt.bar(pos, sales, color='limegreen')
plt.xticks(pos[0:], topgames, fontsize='6')
plt.title("Top 5 Video Game Sales")
plt.xlabel('Games')
plt.ylabel('Sales(Mil)')
plt.show()

