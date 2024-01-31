import pandas as pd
import numpy as np

# Festlegen der Dateipfade und Vergabe von Variablen:
Mitarbeiter = "C:/Users/User/Desktop/Projekte/Mitarbeiter_Neu.csv"
Mitarbeiter2 = "C:/Users/User/Desktop/Projekte/Mitarbeiter_Neu2.csv"

import csv

with open(Mitarbeiter, "r") as fin, open(Mitarbeiter2, "w", newline='') as fout:
    writer = csv.writer(fout, delimiter=',')    # Hier muss das Trennzeichen (delimiter) angegeben werden
    for row in csv.reader(fin, delimiter=','):   # Hier muss das Trennzeichen (delimiter) angegeben werden
        if len(row) < 4:  # Überprüfe, ob die Liste weniger als vier Elemente hat
            continue  # Überspringe die Zeile, wenn sie nicht die erwartete Anzahl von Elementen hat
        if row[3] == '42':
            continue
        writer.writerow(row)

# Ausgabe des Inhalts der neuen CSV-Datei
with open(Mitarbeiter2, "r") as f:
    content = f.read()
    print(content)


# Beachte, dass Zeichenketten mit Anführungszeichen verglichen werden sollten
# if row[3] == '42': Hier wird überprüft, ob der Wert in der vierten Spalte (row[3])
# der aktuellen Zeile der CSV-Datei gleich der Zeichenkette '42' ist.
# continue: Wenn die Bedingung row[3] == '42' wahr ist, wird die continue-Anweisung ausgeführt
# Das bewirkt, dass die aktuelle Iteration der Schleife vorzeitig beendet wird, und der Code springt zum
# nächsten Durchlauf der Schleife. Mit anderen Worten, wenn der Wert in der vierten Spalte gleich '42' ist,
# wird die Schleifeniteration übersprungen.
# writer.writerow(row): Wenn die Bedingung nicht erfüllt ist
# (der Wert in der vierten Spalte ist nicht gleich '42'),
# wird die Zeile mit writer.writerow(row) in die CSV-Datei geschrieben.
# Das bedeutet, dass nur diejenigen Zeilen, bei denen der Wert in der vierten Spalte nicht gleich '42' ist,
# n die neue CSV-Datei geschrieben werden.
# Zusammengefasst: Dieser Code filtert die Zeilen der CSV-Datei und schreibt nur diejenigen
# Zeilen in eine neue Datei, bei denen der Wert in der vierten Spalte nicht gleich '42' ist.

#Hier sind die Änderungen:
#1. In der open-Funktion wurden die Klammern im with-Statement korrigiert.

#2. In der csv.writer- und csv.reader-Funktion wurde das Trennzeichen (delimiter) auf,
#3. festgelegt, da es in CSV-Dateien üblicherweise ein Komma als Trennzeichen gibt.

#4. In der Bedingung if row[3] == 42: wurde '42' verwendet, um sicherzustellen,
#dass der Vergleich mit einer Zeichenkette durchgeführt wird, da CSV-Daten normalerweise als Zeichenketten gelesen werden.

#5. Bitte stelle sicher, dass die Spaltennummer 3 und der Vergleichswert '42' für
#dein spezifisches Szenario korrekt sind.