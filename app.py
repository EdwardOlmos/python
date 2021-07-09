import os
import csv

data = []

with open('data.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    data.append(row[0])

dataLength = len(data)

if (os.path.exists('script.sql')):
  os.remove("script.sql")

with open("script.sql", "a") as scriptfile:
  scriptfile.write('INSERT INTO `tableName` \n')
  scriptfile.write('VALUES \n')

  for i in range(0, dataLength):
    keyValuePair = data[i].split('=')
    scriptfile.write("('" + keyValuePair[0] + "','" + keyValuePair[1] + "'),\n")

  keyValuePair = data[dataLength-1].split('=')
  scriptfile.write("('" + keyValuePair[0] + "','" + keyValuePair[1] + "');\n")
