# Beispiel 2: Schreiben mehrerer Zeilen mit writerows()

import csv
rows = [ ["x","y"],["z","v"]]
with open('test.csv', 'w', newline='') as file:
  mywriter = csv.writer(file, delimiter=',')
  mywriter.writerows(rows)