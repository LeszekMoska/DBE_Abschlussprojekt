# Aufgabe: Öffne die Datei c:/Python/test1.txt zum Schreiben mit dem modus a für Anhängen
# mit Python. Damit wir den Inhalt nicht direkt überschreiben, sondern einfach unten an die Datei
# dran schreiben.

# 1. Dateipfad Festlegen:
dateipfad = "C:/Users/User/Desktop/Projekte/test1.txt"

# 2. Öffnen mit der with open funktion, dies stellt sicher, dass die Datei auch wieder ordnungsgemäß
# geschlossen wird. dies wird im Allgemeinen empfohlen.

with open(dateipfad, "a") as f:
    f.write("Ich, Leszek, füge eine weitere Zeile hinzu")

# 3. Ausgabe Information auf der Konsole
print(f"Der Text wurde erfolgreich an die Datei angehängt: {dateipfad}")