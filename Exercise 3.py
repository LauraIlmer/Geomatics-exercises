

def filesSummary(path, idFieldName, avgFieldName):
    with open(path, 'r')as file:
        lines = file.readlines()
        
    idIndex = None
    analyzeIndex = None
    hSum = 0
    count = 0
    uniqueIdsList = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            fields = line.strip("#").split(",")
            
            for index, field in enumerate(fields):
                field = field.strip()
                if field == idFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index

        else:
            lineSplit = line.split(",")
            value = float(lineSplit[analyzeIndex])
            if value != -9999:
                hSum += value
                count += 1
            
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
                
    avg = hSum/count
            
    print(f"File info: {path}")
    print("==============")
    print(f"Distinct count of field {idFieldName}: {len(uniqueIdsList)}")
    print(f"Average value of field {avgFieldName}: {avg}")
    print("Fields:")
    for field in fields:
        print(f"-> {field.strip()}")
        


#results    
filesSummary("/Personal/laurailmer/onedrive_geomatics","STAID", "RR")
print("********")
fileSummary("/Personal/laurailmer/onedrive_geomatics", "CN", "HGHT")