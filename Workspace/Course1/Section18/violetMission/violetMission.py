print("========================================================================")

print("1--------------------------------")
print("open the txt file with goe locations\n")

with open("message_new_pen.txt") as f:
	text = f.read()
	#print(text)


print("\n2--------------------------------")
print("extract latitudes and longitudes\n")
import re

latLong = []
pattern = "\(.{15,25}\)"

latLong = re.findall(pattern, text)
#print(latLong)
print("\nNumber of points: ", len(latLong))


print("\n3--------------------------------")
print("convert into a list of floats\n")

# go through all points and extract lats and longs
patternLat = 	"\-?\d{1,3}.?\d{1,5}"
patternLong = 	"\-?\d{1,3}.?\d{1,5}\)"
patternLong2 = 	"\-?\d{1,3}.?\d{1,5}"

coordinates = []

for idx, point in enumerate(latLong):
	# get points only (str)
	coordinates.append(re.findall(patternLat, point))
	# convert into float
	coordinates[idx][0] = float( coordinates[idx][0] )
	coordinates[idx][1] = float( coordinates[idx][1] )
	
	print(coordinates[idx])
	

print("\n4--------------------------------")
print("create a map object")

# folium
# https://python-visualization.github.io/folium/quickstart.html
# pip install folium
import folium

map = folium.Map()				# create a map object
mapfg = folium.FeatureGroup()	# create a feature group layer

for lat, long in coordinates:
	#print("Coordinates: ", lat, ", ", long)
	mapfg.add_child(folium.CircleMarker(location = [lat, long], fill = True))

map.add_child(mapfg)

map.save("map.html")

print("display maps with points on it")

import webbrowser
webbrowser.open("map.html")


print("========================================================================")
