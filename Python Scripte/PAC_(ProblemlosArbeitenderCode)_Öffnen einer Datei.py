# Pfad zur CSV-Datei
Datei = open('C:/Users/User/Desktop/Projekte/Mitarbeiter.csv'
             ,'r')
# Öffnen der Datei mit readlines(), zeigt uns die einzelnen Zeillen nacheinander an.
Mitarbeiter = open('C:/Users/User/Desktop/Projekte/Mitarbeiter.csv'
                   ,'r').readlines()
# Öffnen der Datei mit read(), zeigt und die Datei in Tabellenform an, so wie sie ist.
Mitarbeiter2 = open('C:/Users/User/Desktop/Projekte/Mitarbeiter.csv',
                   'r').read()

# Es gibt verschiedene Modi um eine Datei zu öffnen:
# "r" = zum Lesen öffnen (Standard)
# "w" = zum Schreiben öffnen, wobei die Datei erst abgeschnitten wird
# "x" = öffnen für exklusive Einstellung, schlägt fehl, wenn die Datei bereits geöffnet ist
# "a" = zum Schreiben geöffnet an das Ende der Datei angehängt, falls vorhanden
# "b" = binärer modus "t" = Textmodus (Standard)
# "+" = Öffnen für Aktualisierung (Lesen und schreiben)
print("Öffnen der Datei nur mit Open() im Modus r :")
print(Datei)
print("Öffnen der Datei nur mit Open() und readlines() :")
print(Mitarbeiter)
print("Öffnen der Datei nur mit Open() und read() :")
print(Mitarbeiter2)
