# Aufgabe: Nun ändere den Modus von a auf w. Damit wird der bereits bestehende Inhalt
# der Datei überschrieben mit dem neuen Inhalt.

# 1. Dateipfad Festlegen:
dateipfad = "C:/Users/User/Desktop/Projekte/test1.txt"

# 2. Öffnen mit der with open funktion, dies stellt sicher, dass die Datei auch wieder ordnungsgemäß
# geschlossen wird. dies wird im Allgemeinen empfohlen.

with open(dateipfad, "w") as f:
    f.write("Ich, Leszek, Überschreibe nun den Inhalt dieser Zeile")

# VORSICHT: Wenn mit Modus auf "w" gearbeitet wird da dies den gesamten vorherigen Inhalt
# der Datei löschen wird.

# 3. Ausgabe Information auf der Konsole
print(f"Der Text wurde erfolgreich an die Datei angehängt: {dateipfad}")