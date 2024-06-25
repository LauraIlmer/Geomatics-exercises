from pyqgis_scripting_ext.core import *

osm = HMap.get_osm_layer()

folder = "/Personal/laurailmer/onedrive_geomatics"
gpkgPATH = folder + "miniGPKG.gpkg"

countries_Name = "ne_50m_admin_0_countries"
countries_Layer = HVectorLayer.open(gpkgPATH, countries_Name)

print("Schema (first 20 fields):")
counter = 0
for name, type in countries_Layer.fields.items():
    counter += 1 
    if counter < 21:
        print("\t", name, "of type", type)

countries_Features = countries_Layer.features()

fieldNames = countries_Layer.field_names
print(fieldNames)

nameIndex = countries_Layer.field_index("NAME")
print(nameIndex)

for feature in countries_Features:
    name = feature.attributes[nameIndex]
    if name == 'France':
        frechGeom = feature.geometry # get the geometry 
        print("GEOM:", frechGeom.asWkt()[:100] + "...") 


cities_Name = "ne_10m_populated_places"
cities_Layer = HVectorLayer.open(gpkgPATH, cities_Name)
fieldNames = cities_Layer.field_names
print(fieldNames)

cities_Features = cities_Layer.features()

cityIndex = cities_Layer.field_index("NAME")
print(cityIndex)

countcities = 0

for feature in cities_Features:
    name = feature.attributes[cityIndex]
    cities_points = feature.geometry
    
#results
    if cities_points.intersects(frechGeom):
        countcities += 1
        print(name,": ",cities_points)

print(countcities)