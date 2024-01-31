import csv

# Dateipfad für die CSV-Datei
csv_dateipfad = "C:/Users/User/Desktop/Projekte/Zufallsdaten.csv"

# Header für die CSV-Datei
header = ["Name", "Alter", "Stadt"]

# Daten erstellen
daten = [
    ["Beate", 46, "Marburg"],
    ["Benjamin", 43, "Winden"],
    ["Sebastian", 44, "Bad Ems"],
    ["Leszek",37,"Welschneudorf"],
    ["Martin",34,"Winden"],
    ["Kasia", 35, "Winden"],
]

# CSV-Datei schreiben, Header und Daten:
with open(csv_dateipfad, "w", newline='') as csv_datei:
    csv_writer = csv.writer(csv_datei)
    csv_writer.writerow(header)
    csv_writer.writerows(daten)

# Inhalt der Datei ausgeben auf der Konsole:
# CSV-Datei lesen und Inhalt ausgeben
with open(csv_dateipfad, "r") as csv_datei:
    csv_reader = csv.reader(csv_datei)
    for zeile in csv_reader:
       print(zeile)

# Ausgabe auf der Konsole:
print(f"Die CSV-Datei wurde erstellt: {csv_dateipfad}")
