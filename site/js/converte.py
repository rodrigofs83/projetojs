import csv
import json
arqcsv='data.csv'
arqjs='data.js'
data = {}
with open(arqcsv)  as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['R_fighter']
        data[id]=rows
with open(arqjs,'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))
print('fim')
