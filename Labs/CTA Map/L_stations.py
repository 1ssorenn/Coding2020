# Folium train map
import folium
import csv
from folium import plugins


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

loc = [eval(x[-1]) for x in data]
names = [x[3] for x in data]
c = []
# All train color

for tra in data:
    if tra[7] == 'true':
        c.append('red')
    elif tra[8] == 'true':
        c.append('blue')
    elif tra[9] == 'true':
        c.append('green')
    elif tra[10] == 'true':
        c.append('	#A52A2A')
    elif tra[11] == 'true':
        c.append('purple')
    elif tra[12] == 'true':
        c.append('purple')
    elif tra[13] == 'true':
        c.append('#FFFF00')
    elif tra[14] == 'true':
        c.append('pink')
    elif tra[15] == 'true':
        c.append('orange')
    else:
        c.append('black')

# creation of the map
map = folium.Map(location=[41.880443, -87.644107], zoom_start=11, tiles='Stamen Toner Lite')
for i in range(len(data)):
    folium.Marker(location=(loc[i]),
                  popup=names[i],
                  icon=folium.plugins.BeautifyIcon(border_color=(c[i]), icon='train', prefix='fa')
                  ).add_to(map)


map.save('cta_map.html')