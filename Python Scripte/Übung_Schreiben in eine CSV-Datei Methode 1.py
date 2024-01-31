# Wir werden csv für diese Aufgabe ausschließlich das in Python eingebaute Modul
# verwenden. Aber zuerst müssen wir das Modul importieren als:
# import csv

# Beispiel 1: Mit csv.writer() in CSV-Dateien schreiben
# Angenommen, wir möchten eine CSV-Datei mit den folgenden Einträgen schreiben:
# x,y
# z,v
# ZZ,FF

# So machen wir es:
import csv
with open('.idea/test.csv', 'w', newline='') as file:
   mywriter = csv.writer(file)
   mywriter.writerow(["x", "y"])
   mywriter.writerow(["z", "v"])
   mywriter.writerow(["ZZ", "FF"])

# Wenn wir das obige Programm ausführen, wird im aktuellen Arbeitsverzeichnis eine
# test.csv - Datei mit den angegebenen Einträgen erstellt. Hier haben wir die Datei
# test.csv im Schreibmodus mit der open() Funktion geöffnet.
# Als nächstes wird die csv.writer() Funktion verwendet,
# um ein writer-Objekt zu erstellen. Die writer.writerow()-Funktion wird dann verwendet,
# um einzelne Zeilen in die CSV-Datei zu schreiben. Alternativ könnte auch die Funktion
# writerows verwendet werden. Mehr dazu in der Literatur.