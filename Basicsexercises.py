# basics exercises for starting; summary of codes

from pyqgis_scripting_ext.core import *

path = "/Personal/laurailmer/onedrive_geomatics"
with open(path, "r") as file:
    readLines = file.readlines()
    
points = []
lines = []
polygons = []
for line in readLines:
    line = line.strip()

    split = line.split(";")
    gtype = split[0]
    coords = split[1]
    num = split[2]
    
    if gtype == "point":
        coordSplit = coords.split(",")
        longi = float(coordSplit[0])
        lati = float(coordSplit[1])
        point = HPoint(longi, lati)
        print(point)
        points.append(point)
    elif gtype == "line":
        coordSplit = coords.split(" ")
        pointList = []
        for coordString in coordSplit:
            split = coordString.split(",")
            longi = float(split[0])
            lati = float(split[1])
            pointList.append
            pointList.append([longi, lati])
        line = HLineString.fromCoords(pointList)
        lines.append(line)
    elif gtype == "polygon":
        coordSplit = coords.split(" ")
        pointList = []
        for coordString in coordSplit:
            split = coordString.split(",")
            longi = float(split[0])
            lati = float(split[1])
            pointList.append
            pointList.append([longi, lati])
        polygon = HPolygon.fromCoords(pointList)
        polygons.append(polygon)
        
        
canvas = HMapCanvas()

for point in points:
    canvas.add_geometry(point, "green", 50)
for line in lines:
    canvas.add_geometry(line, "yellow", 3)
for polygon in polygons:
    canvas.add_geometry(polygon, "red", 1)
    
bounds = [0, 0, 50, 50]
canvas.set_extent(bounds)
canvas.show()

# Exercise 2

from pyqgis_scripting_ext.core import *

extent = 6
polygons = []

for lon in range (-180, 180, extent):
    minX = lon
    maxX = lon + extent
    minY = -84
    maxY = 84
    
    coords = [[ minX, minY], [minX, maxY], [maxX, maxY], [maxX, minY], [minX, minY]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)

canvas = HMapCanvas.new()

for polygon in polygons:
    canvas.add_geometry(polygon)
    
canvas.set_extent([-180, -84, 180, 84])
canvas.show()





# Exercise 03
path = "/Personal/laurailmer/onedrive_geomatics/Data/stations.txt"

with open(path, 'r') as file:
       lines = file.readlines()

country_Code = []
points = []

for line in lines[1:]:
    lineSplit = line.split(",")
    
    country = lineSplit[2]
    country_Code.append(country)
    
    lat = lineSplit[3].strip("+")
    lon = lineSplit[4]. strip("+")
    
    latSplit = lat.split(":")
    lonSplit = lon.split(":")
    
    convLat1 = float(latSplit[1])/60
    convLat2 = float(latSplit[2])/3600
    convLon1 = float(lonSplit[1])/60
    convLon2 = float(lonSplit[2])/3600
    
    latFinal = float(latSplit[0]) + convLat1 + convLat2
    lonFinal = float(lonSplit[0]) + convLon1 + convLon2
    
    point = HPoint(lonFinal, latFinal)
    points.append(point)

print(points[0])
    
canvas = HMapCanvas()

for point in points:
    canvas.add_geometry(point, "green", 1)

bounds_data = [0, 0, 180, 90]
canvas.set_extent(bounds_data)
canvas.show()

uniqueValues = set(country_Code)

for item in uniqueValues:
    statNum = country_Code.count(item)
    print(f"{item}: {statNum}")