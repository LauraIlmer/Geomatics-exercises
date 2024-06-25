# working with lists

mylist = ['merano', 'Bolzano', 'Trento']
print(mylist)
print("The elements start at position 0: ", mylist[0])

## add objets and remove objects
mylist.append("Postdam")
print(mylist)

mylist.remove("Postdam")
print(mylist)

### remove by position: pop also returns the removed item
mylist.pop(0)
print(mylist)

## to check if my list includes something
mylist = ['merano', 'Bolzano', 'Trento']
doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)

doIHavePostdam = "Postdam" in mylist
print(doIHavePostdam)


for item in mylist:
    print(item)

colors = ["red", "pink", "green", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]


for index in range(len(colors)):
    color = colors[index]
    ratio = ratios[index]
    
    print(f"{colors} -> {ratio}")

for i in range(10):
    if i == 5:
        break
    print(f"A) {i}")
print("_____")

for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")
print("_____")



for i in range(2, 10):
    print(f"C) {i}")
for i in range(0, 10, 2):
    print(f"D) {i}")

for i in range(10, 0, -2):
    print(f"E) {i}")

print("_____")


mylist = ['merano', 'Bolzano', 'Trento']
print(f"My original list: {mylist}")
mylist.sort()
print(f"My sorted list: {mylist}")

mylist.sort(reverse = True)
print(f"My re-sorted list: {mylist}")

# second exercise with fruits
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(f"A mixed case list, sorted: {mylist}")
mylist.sort(key = str.lower)
print(f"A mixed case list, properly sorted: {mylist}")


numlist =["002", "01", "3", "004"]
numlist.sort()
print(numlist)

numlist =["002", "01", "3", "004"]

def toInt(string):
    return int(string)

numlist.sort(key = toInt)
print(numlist)


abc = ["a", "b", "c"]
cde = ["c", "d", "e"]

newabcde = abc + cde
print(newabcde)

print(";".join(newabcde))
print("|".join(newabcde))

numlist = [1.0,2.0,3.5,6,11,34,12]
print(max(numlist))
print(min(numlist))
print(sum(numlist))

print("_____")

suma = 0

for i in range(len(numlist)):
    suma += numlist[i]
    print(suma)

print("__________")

suma = 0
count = 0

for i in range(len(numlist)):
    suma += numlist[i]
    count+=1
    print(suma)

average = suma/count
print(average)

average2 = suma/i
print(average)


print("_____")


diferencia = 0
diferencias = []
squaredvalues =[]
sumaSquared = 0

for n in range(len(numlist)):
    diferencia += numlist[n] - average
    diferencias.append(diferencia)
    squaredvalues.append(diferencia**2)
    sumaSquared += squaredvalues[n]
    
print(diferencias)
print(squaredvalues)
print(sumaSquared)

variance = sumaSquared/n-1
print(variance)

townsProvincesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trento": "TN"
}
print(townsProvincesMap)

print(townsProvincesMap["merano"])
townsProvincesMap["postdam"] = "BR"
print(townsProvincesMap)
townsProvincesMap.pop("postdam")
print(townsProvincesMap)

print(townsProvincesMap.get("Merano"))
if townsProvincesMap.get("Merano") is None:
    print("key doesn't exist")
else: 
    print("key exists")

print(townsProvincesMap.get("Merano", "unknown"))

for key, value in townsProvincesMap.items():
    print(key, "is in the province of", value)

print(townsProvincesMap.keys())
print(townsProvincesMap.values())

keys = list(townsProvincesMap.keys())
keys.sort()
print(keys)

for key in keys:
    print(key, "is in the province of", townsProvincesMap[key])

filePath = "/Users/rominalavarello/Documents/EMMA/2 semester/Advanced geomatics/excercises1/data_class2.txt"

data_class2 = """# stationid, datetime, temperature
1, 2022-01-01 00:00, 12.3

2, 2022-01-01 00:00, 11.3
3, 2022-01-01 00:00, 10.3
"""
with open(filePath, 'w') as file:
    file.write(data_class2)
    
with open(filePath, 'a') as file:
    file.write("1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")

with open(filePath, 'r') as file:
    lines = file.readlines()
    
print(lines)

print("_____")

stationsCount = {}

for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    linesplit = line.split(",")
    stationid = linesplit[0]
    
    counter = stationsCount.get(stationid,0)
    counter += 1
    
    stationsCount[stationid] = counter
    
    print(stationsCount)
print("_____")
print(stationsCount)