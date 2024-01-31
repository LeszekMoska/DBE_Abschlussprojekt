import pickle

data = (1.4, 5, 4.5)
output = open("data.pkl","wb")
pickle.dump(data,output)
output.close()
# Beim Öffnen von Dateien mit open ist es wichtig, den richtigen Modus zu verwenden.
# In diesem Fall ist der Binärmodus ("wb") erforderlich, da pickle binäre Daten schreibt und liest.
# Mit dieser Änderung sollte dein Code wie erwartet funktionieren.

# Laden der erstellten Datei data.pkl
f = open("data.pkl","rb")
data = pickle.load(f)
print(data)