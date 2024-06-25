#Covid exercise

#import data regioni italiane covid; output
from pyqgis_scripting_ext.core import *
folder = "/Personal/laurailmer/onedrive_geomatics"
gpkgPATH = folder + "/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
data = "/Personal/laurailmer/onedrive_geomatics/coviddata"
covidPATH = data + "/dpc-covid19-ita-regioni.csv"
outputFolder = "/Personal/laurailmer/onedrive_geomatics/coviddata-output"

# Provinces import and remove
prov_Name = "ne_10m_admin_1_states_provinces"
HMap.remove_layers_by_name(["ne_10m_admin_1_states_provinces"])
prov_Layer = HVectorLayer.open(gpkgPATH, prov_Name)
prov_Features = prov_Layer.features()
prov_Layer.subset_filter("iso_a2='IT'")


# Hmap; loading the layers and making a dictionary
HMap.add_layer(prov_Layer)
regionsName2GeomMap = {}
regionsIndex = prov_Layer.field_index("region")

for prov_Feature in prov_Layer.features():
    geometry = prov_Feature.geometry
    regionsName = prov_Feature.attributes[regionsIndex]
    
    regionsGeometry = regionsName2GeomMap.get(regionsName) 
    if regionsGeometry:
       
        regionsGeometry = regionsGeometry.union(geometry)
    else: 
        regionsGeometry = geometry
    
    regionsName2GeomMap[regionsName] = regionsGeometry 

with open(covidPATH,'r') as file:
    lines = file.readlines()
    
day2featuresMap = {} 
    
for index, line in enumerate(lines):
    line = line.strip()
    if index < 50000:
        lineSplit = line.split(",")
       
        
        dayAndTime = lineSplit[0]
        dayAndTime = dayAndTime.split("T")
        day = dayAndTime[0]
        
        if day.endswith("01"):
            region = lineSplit[3]
            totalCovidCases = int(lineSplit[17])
            
            lat = float(lineSplit[4])
            lon = float(lineSplit[5])
            dataPoint = HPoint(lon, lat)
            
            for regionsName, regionsGeometry in regionsName2GeomMap.items():
                if regionsGeometry.intersects(dataPoint):
                    featureslist = day2featuresMap.get(day)
                    if featureslist:
                        featureslist.append((regionsGeometry, [day, region, totalCovidCases]))
                    else:
                        featureslist = [(regionsGeometry, [day, region, totalCovidCases])] 
                    day2featuresMap[day] = featureslist

imagePathsList = []

for day, featureList in day2featuresMap.items():
        
    print("Generating day", day)
    newLayerName = "covid_italy"
    HMap.remove_layer_by_name(newLayerName)
    
    schema = {
        "day": "string",
        "region": "string",
        "totalCovidCases": "int"
    }
    covidLayer = HVectorLayer.new(newLayerName, "MultiPolygon", "EPSG:4326", schema)
    
    for geometry, attributes in featureList:
        covidLayer.add_feature(geometry, attributes)
        
    ranges = [
        [float('-inf'),1000],
        [1001, 3000],
        [3001, 10000],
        [10001, 40000],
        [40001, 1000000],
        [1000001,float('inf')]
    ]
    
    styles = [
        HFill('arcticblue') + HStroke('white',0.5),
        HFill('skyblue') + HStroke('white',0.5),
        HFill('saphireblue') + HStroke('white',0.5),
        HFill('cobaltblue') + HStroke('white',0.5),
        HFill('indigoblue') + HStroke('white',0.5),
        HFill('black') + HStroke('white',0.5)
    ]
    
    labelStyle = HLabel('totalCovidCases', size = 7, color = 'black') + HHalo() + HFill()
    covidLayer.set_graduated_style("totalCovidCases", ranges, styles, labelStyle)
    HMap.add_layer(covidLayer)
    printer = HPrinter(iface)
    mapProp = {
        "x": 5,
        "y": 25,
        "width": 285,
        "height": 180,
        "frame": True,
        "extent": covidLayer.bbox()
    }
    printer.add_map(**mapProp)
    
#description -> legenda
    
    legendProp = {
        "x": 210,
        "y": 30,
        "width": 150,
        "height": 100,
        "frame": True,
    }
    printer.add_legend(**legendProp)
    
    labelProp = {
        "x": 120,
        "y": 10,
        "text": "COVID in Italy, total Covid cases",
        "bold":True,
        "italic":False
    }
    printer.add_label(**labelProp)
    
    labelProp = {
        "x": 30,
        "y": 190,
        "text": day,
        "bold":True,
        "font_size": 28,
    }
    printer.add_label(**labelProp)
    
    imageName = f"{day}_coviditaly.png"
    imagePath = f"{outputFolder}/{imageName}"
    printer.dump_to_image(imagePath)
    imagePathsList.append(imagePath)

# pip and animation 

from PIL import Image
imagesList = []
for path in imagePathsList:
    img = Image.open(path)
    imagesList.append(img)
    
animationPath = f"{outputFolder}/covid_animationitaly.gif"
imagesList[0].save(animationPath, save_all=True, append_images=imagesList[1:], duration=500, loop=2) #miliseconds, loop to restart

for path in imagePathsList:
    os.remove(path)