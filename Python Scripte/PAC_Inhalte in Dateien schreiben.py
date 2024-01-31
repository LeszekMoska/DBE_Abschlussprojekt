# Öffnen oder erstellen einer Datei im Schreibmodus ('w' für write)
with open('datei.txt', 'w') as file:
    # Schreiben von Inhalten in die Datei
    file.write("Hallo, dies ist ein Text.\n")
    file.write("Hier ist eine weitere Zeile.")

# Diese Methode öffnet die Datei im Schreibmodus ('w'),
# und die write-Methode wird verwendet, um den gewünschten Text in die Datei zu schreiben.
# Beachte, dass der Inhalt der Datei überschrieben wird, wenn die Datei bereits existiert.
# Wenn die Datei nicht existiert, wird eine neue erstellt.

# Öffnen oder erstellen einer Datei im Schreibmodus ('w' für write)
with open('datei.txt', 'w') as file:
    # Verwenden der print-Funktion mit der Datei als Ausgabeziel
    print("Hallo, dies ist ein Text.", file=file)
    print("Hier ist eine weitere Zeile.", file=file)
    print("Hier ist eine weitere Zeile nummer 3.", file=file)

#Hier wird die print-Funktion verwendet, und der Parameter file wird auf die geöffnete Datei gesetzt. Dies ermöglicht das Schreiben von Text in die Datei, ähnlich wie bei der write-Methode.

# Beide Methoden verwenden den with-Kontextmanager (with open(...) as file:),
# um sicherzustellen, dass die Datei ordnungsgemäß geschlossen wird,
# wenn der Codeblock abgeschlossen ist.
# Dies ist eine bewährte Praxis, um sicherzustellen,
# dass Ressourcen ordnungsgemäß freigegeben werden.