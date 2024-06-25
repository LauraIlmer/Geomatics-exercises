# vector data and geopackaging

from pyqgis_scripting_ext.core import *
def convert_coords(coords):
    list = []
    for latorlon in coords:
        grad = float(latorlon[0])
        minuten = float(latorlon[1])
        sekunden = float(latorlon[2])
        
        sign = 1 if grad >= 0 else -1
        
        decimales = abs(grad) + minuten / 60 + sekunden / 3600
        decimales *= sign
        
        list.append(decimales)
    return list


# second step

folder = "/Personal/laurailmer/onedrive_geomatics_vector"
path = folder + "stations.txt"

with open(path, 'r') as file:
    lines = file.readlines()

fields = {
    "id":"int",
    "station":"str",
    "country":"str",
    "lat":"str",
    "lon":"str",
    "elevation":"int"
    }

stationslayer = HVectorLayer.new("stations", "Point", "EPSG: 4326", fields)
HMap.remove_layers_by_name(["stations","stations_forever"])

latitudes = []
longitudes = []

for line in lines[:500]:
    if not line.startswith("#"):
        line = line.strip()
        lineSplit = line.split(",")
        
        lat = lineSplit[3]
        latSplit = lat.split(":")
        latitudes.append(latSplit)
        
        lon = lineSplit[4]
        lonSplit = lon.split(":")
        longitudes.append(lonSplit)
        
        name = lineSplit[1]
        
        LATs = convert_coords(latitudes)
        LONs = convert_coords(longitudes)
        
        for lat,lon in zip(LATs,LONs):
            stationslayer.add_feature(HPoint(lon,lat),[1,name])
    
HMap.add_layer(stationslayer)


# make the geopackage
gpkgpath = folder + "test.gpkg" 
error = stationslayer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)

stationslayerF = HVectorLayer.open(gpkgpath, "stations_forever")
HMap.add_layer(stationslayerF)