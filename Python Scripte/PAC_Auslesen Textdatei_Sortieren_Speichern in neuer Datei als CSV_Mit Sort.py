import csv

# Dateipfad zur Textdatei auf dessen Repository festlegen
text_dateipfad = "C:/Users/User/Desktop/Projekte/Mitarbeiter_Gehalt.txt"
# Dateipfad zum neuen Repository der neu zu kreierenden CSV Datei, welche ich erstellen will festlegen:
csv_dateipfad = "C:/Users/User/Desktop/Projekte/Mitarbeiter_Gehalt2.csv"

# Liste für die Daten erstellen
daten = []

# Die Textdatei öffnen und Zeilenweise lesen, CSV-Reader erstellen, den Header der Datei extrahieren, dann
# Daten aus der Datei lesen mit "r" und zur Liste hinzufügen
with open(text_dateipfad, 'r') as gehalt_datei:
    csv_reader = csv.reader(gehalt_datei, delimiter=';')
    header = next(csv_reader)
    for zeile in csv_reader:
        daten.append(zeile)

# Jetzt nach dem Header sortieren, ich nehme hier an die erste Zeile ist der header in der Liste.
# Alternative Sortierung ohne Lambda sondern mit sort:
# In diesem Codebeispiel erstelle ich eine Funktion namens alphabetisch, die als Eingabe ein Element
# erhält und das erste Element dieses Elements zurückgibt. Das bedeutet, wenn das Element eine Liste ist,
# gibt die Funktion das erste Element dieser Liste zurück.
# Zusammengefasst: Diese Codezeilen sortieren die Liste daten nach dem ersten Element
# jeder Unterliste in aufsteigender Reihenfolge.
def alphabetisch(element):
    return element[0]
# Verwendung der sort-Methode mit einer separaten Funktion als Vergleichsschlüssel
daten.sort(key=alphabetisch)

# Nun müssen die Daten in eine neue CSV-Datei geschrieben werden mit "w" für write. Newline='',
# Die Einstellung newline='' sorgt dafür, dass Python die Zeilenumbruchkonventionen
# des jeweiligen Betriebssystems verwendet. Diese Einstellung stellt sicher, dass Textdateien
# auf verschiedenen Betriebssystemen korrekt interpretiert werden können.
# Es muss dazu ein CSV-Writer erstellt werden, der header muss geschrieben werden, dann die
# sortierten Daten in die Datei schreiben mit "w". Die Trennzeichen Semikolon mir delimiter=';' festlegen
with open(csv_dateipfad, 'w', newline='') as neue_datei:
    csv_writer = csv.writer(neue_datei, delimiter=';')
    csv_writer.writerow(header)
    csv_writer.writerows(daten)

# Diese Zeile print(f'Die sortierten Daten wurden in "{csv_dateipfad}" gespeichert.')
# verwendet sogenannte f-Strings (formatted string literals) in Python. Ein f-String ermöglicht es,
# Ausdrücke innerhalb von Zeichenketten einzubetten, indem man sie mit geschweiften Klammern {} einschließt.

print(f'Die sortierten Daten wurden in "{csv_dateipfad}" gespeichert.')

# Hier wird neuer_dateipfad als Ausdruck innerhalb des f-Strings verwendet. neuer_dateipfad ist zuvor
# als Variable definiert worden und enthält den Dateipfad der neuen CSV-Datei, in die die sortierten Daten
# geschrieben wurden.
# Wenn diese Zeile ausgeführt wird, wird der Text in den geschweiften Klammern durch den Wert von
# csv_dateipfad ersetzt, und das Ergebnis wird auf der Konsole ausgegeben.