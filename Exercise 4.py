rom pyqgis_scripting_ext.core import*


#Import function we need:
from math import cos, sin, radians

n = 8
d = 7
iterations = max(n,d)
#exercise 4

max_Angle = 360*iterations
coords = []
#Define an angle:
for angle in range(0, max_Angle, 1):
    radAngle = radians(angle)
    #Formulas:
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)
    
    coords.append([x, y])
    # print(x, y)
    
line = HLineString.fromCoords(coords)

canvas = HMapCanvas.new()
canvas.add_geometry(line)
canvas.set_extent(line.bbox())
canvas.show()