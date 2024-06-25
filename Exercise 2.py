csvPath = "C:/Users/laura/Downloads/01_exe2_data.csv"

#Step 2
with open(csvPath, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    lineSplit= line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
    print(x1)
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    print(y2)
    
    maxaanalogString = lineSplit[2]
    x2 = float(maxaanalogString.split(":")[1])
    print(x2)
    
    #x2/x1=y2/y1---- float changes it to numbers
    y1 = (y2*x1/x2)
    print(y2*x1/x2)
