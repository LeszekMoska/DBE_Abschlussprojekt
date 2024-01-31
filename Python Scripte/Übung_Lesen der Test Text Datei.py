import csv

with open("test.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)