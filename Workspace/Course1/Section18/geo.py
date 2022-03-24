# geographical maps in Python
# plottin longitudes and latitudes (bokeh lib)
# can work with Google maps to plot points on a map
# pip install bokeh
print("========================================================================")


print("1--------------------------------")
print("open a csv file with goe locations")

import csv

with open("countries.csv") as f:
	file = csv.reader(f)
	for row in file:
		print(row)


print("\n2--------------------------------")
print("get lattitudes and longitudes")

lats = []
longs = []

with open("countries.csv") as f:
	file = csv.reader(f)
	for abrev, lat, long, name in list(file)[1:]:
		lats.append(float(lat))
		longs.append(float(long))
	
print("latitudes:\n")	
for idx in range(5):
	print(lats[idx])

print("longitudes:\n", longs[idx])
for idx in range(5):
	print(longs[idx])
	

print("\n3--------------------------------")
print("create a map object")

# folium
# https://python-visualization.github.io/folium/quickstart.html
# pip install folium
import folium

map = folium.Map()	# create a map object
mapfg = folium.FeatureGroup()	# create a feature group layer

for lat, long in zip(lats, longs):
	mapfg.add_child(folium.CircleMarker(location = [lat, long], fill = True))

map.add_child(mapfg)

map.save("map.html")

print("display maps with points on it")
import webbrowser
webbrowser.open("map.html")



# print("\n3--------------------------------")
# print("create a map object")

# to use bokeh you need a developer key from 
# https://developers.google.com/maps/documentation/javascript/get-api-key
# need to set up an account and provide credit card details

# from bokeh.io import output_file, show
# import bokeh.models
# 
# mapOptions = GMapOptions(lat=0, lng=0, zoom=3)
# plot = GMapPlot(x_range=Range1d(), y_range=Range1d, map_options=MapOptions)
# plot.title.text = "Example Plot"
# plot.api_key = input("API Key: ")
# source = ColumnDataSource(data=dice(lat=lats, lon-longs))
# 
# circle = Circle(x="lon", y="lat", size=15, fill_color="red", fill_alpha=0.6)
# plot.add_glyph(source, circle)
# plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
# 
# outputFile("map.html")
# 
# print("display maps with points on it")
# show(plot)


print("========================================================================")
