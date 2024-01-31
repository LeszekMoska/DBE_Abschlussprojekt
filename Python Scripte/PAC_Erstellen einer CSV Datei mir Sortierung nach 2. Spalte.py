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

# CSV-Datei lesen
with open(csv_dateipfad, "r") as csv_datei:
    csv_reader = csv.reader(csv_datei)
# Daten in eine Liste umwandeln und nach der 2. Spalte sortieren
    daten = sorted(list(csv_reader), key=lambda x: x[1])
# Sortierte Daten ausgeben
for zeile in daten:
    print(zeile)

# Ausgabe auf der Konsole:
print(f"Die CSV-Datei wurde erstellt: {csv_dateipfad}")
