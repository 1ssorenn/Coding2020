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
sortq1 = [x[4] for x in data]
data = [float(x[-1]) for x in data]



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



# Questions Code
quest1 = sortq1.pop(0)
print("The answer to question #1 is",quest1)

quest2 = ((sales[0] - sales[4]) // 1)
print("The answer to question #2 is", quest2, "mil")

quest3 = (sum(sales) // 5)
print("The answer to question #3 is", quest3, "mil")