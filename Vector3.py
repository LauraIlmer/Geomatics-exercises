# geopackage

from pyqgis_scripting_ext.core import *

folder = "/Personal/laurailmer/onedrive_geomatics"
gpkgPATH = folder + "miniGPKG.gpkg"

HMap.remove_layers_by_name(["centroids",countries_Name,"OpenStreetMap"])
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countries_Name = "ne_50m_admin_0_countries"

#layers
schema = {
    "name":"string",
}

centroids_Layer = HVectorLayer.new("centroids","Point","EPSG: 4326", schema)
countries_Layer = HVectorLayer.open(gpkgPATH, countries_Name)

nonInCountryList = []
nameIndex = countries_Layer.field_index("NAME")
for country in countries_Layer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    centroids_Layer.add_feature(centroid, [name])
    
    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)
    
simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo ()
centroids_Layer.set_style(simpleStyle)
HMap.add_layer(centroids_Layer)

print("Countries with centroids outside:")
for c in nonInCountryList:
    print(c)
    
ranges = [
    [80000000, float('inf')],
    [1000000, 80000000],
    [float('-inf'),1000000]
]

styles = [
    HFill("255, 0, 0, 70"),
    HFill("0, 255, 0, 70"),
    HFill("0, 0, 255, 70"),
]

#results    
labelstyle = HLabel("POP_EST") + HHalo()
countries_Layer.set_graduated_style("POP_EST", ranges, styles, labelstyle)
HMap.add_layer(countries_Layer)