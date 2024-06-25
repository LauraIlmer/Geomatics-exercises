folder = r"C:/Personal/laurailmer/onedrive_geomatics"
csvpath = f"{folder}/datasets/stations.txt"

from pyqgis_scripting_ext.core import *
with open(csvpath,"r")as file:
    lines = file.readlines()
    
crsHelper = HCrs() 
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)


cordinates_name=[]
stations = []  
for line in lines:
    line = line.strip()
    if line.startswith('#')or len(line)==0:
        continue
    lineSplit = line.split(",")
    name=lineSplit[1].strip()
    long = lineSplit[4].replace("+","")
    longSplit=long.split(":")
    
    long_deg = int(longSplit[0])
    long_min = int(longSplit[1])/60
    long_sec = int(longSplit[2])/3600

    longitude = float(long_deg+long_min+long_sec)
    
    lat = lineSplit[3].replace("+","")
    latSplit=lat.split(":")
    lat_deg = int(latSplit[0])
    lat_min = int(latSplit[1])/60
    lat_sec = int(latSplit[2])/3600

    latitude = float(lat_deg+lat_min+lat_sec)
    station_Point = HPoint(longitude,latitude)
    stations.append(station_Point)
    cordinates_name.append((name, longitude, latitude))

#canvas
canvas = HMapCanvas.new()
 
osm= HMap.get_osm_layer()
canvas.set_layers([osm])

TransStations =[]

for item in stations:
    point3857 = crsHelper.transform(item)
    TransStations.append(point3857)
    canvas.add_geometry(point3857,'red',1)
    

canvas.set_extent([-1000000, 4000000, 5000000, 10000000])
canvas.show()

stationDic ={}
country=[]
for line in lines:
    line = line.strip()
    if line.startswith('#')or len(line)==0:
        continue
    lineSplit = line.split(",")
    countries = lineSplit[2]
    country.append(countries)
    
for character in country:
    count =stationDic.get(character,0)
    count +=1
    stationDic[character]=count
    
for key,value in stationDic.items():
    print(f"{key}:{value}")

distances = []

university = HPoint(11.34999, 46.49809)
for station in stations:
    distance = university.distance(station)
    distances.append(distance)
    
closest_station_e = distsnces.index(min(distances))
closest_station = stations[closest_station_e]

print("Closest station:", closest_station)

longstation = closest_station.x
latstation = closest_station.y

print(longstation)
print(latstation)

for line in cordinates_name:
    
    if longstation == line[1]:
        if latstation == line[2]:
            print("name of the closest station is", line[0])
   

rand_point =HPoint(11.34999, 46.49809)

transrand_point = crsHelper.transform(rand_point)


radius = 20000 
listwithin =[]

bufferarea = transrand_point.buffer(radius)


for stat in TransStations:
    if bufferarea.contains(stat):
        listwithin.append(stat)
    else: continue

print("stations within the bufferarea")
print(listwithin)

transformedwithin =[]

for item in listwithin:
    backwithin = crsHelper.transform(item, inverse = True) 
    transformedwithin.append(backwithin)


print("transformed within the bufferarea")
print(transformedwithin)


longiii =[]
latiii=[]
for points in transformedwithin:
    longiii.append(points.x)
    latiii.append(points.y)
    

print("longiii is")
print(longiii)
print("latiii is")
print(latiii)

counter =0
print(longiii[counter])

station_names=[]
count = 0

for line in cordinates_name:
    if  line[1]== longiii[count] and line[2] == latiii[count]:
        station_names.append(line[0])
    else:
        continue
    count+= 1
        
print("Name of the stations in the buffer zone are:")
print (station_names)


print(cordinates_name[:10])
