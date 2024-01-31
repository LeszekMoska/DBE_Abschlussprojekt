import pandas as pd
import numpy as np

import csv

with open("C:/Users/User/Desktop/Projekte/Mitarbeiter_Neu.csv", newline="") as csvfile:
    mgreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for line in mgreader:
        print(line)
# Die `open`-Funktion öffnet die CSV-Datei im Lesemodus (`"r"` für "read").
# Der Parameter `newline=""` sorgt dafür, dass unterschiedliche Arten von Zeilenumbrüchen
# richtig interpretiert werden.
# Die `csv.reader`-Funktion erstellt einen CSV-Reader, der die Datei zeilenweise liest.
# Der `delimiter=","` gibt an, dass die Spalten in der CSV-Datei durch Kommata getrennt sind.
# Der `quotechar="/"` gibt an, dass Anführungszeichen verwendet werden können,
# um Zellen zu umschließen.
# Die `for`-Schleife geht durch jede Zeile des CSV-Readers.
# In jeder Iteration wird die aktuelle Zeile auf der Konsole ausgegeben.
