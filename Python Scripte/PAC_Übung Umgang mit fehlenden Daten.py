import numpy as np
import pandas as pd

# Zufällige Liste erstellen mit Werten und NAN Werten
liste = {
    'Name':["Leszek","Martin",np.nan],
    'Alter':[37,np.nan,35],
    'Wohnort':[np.nan,"Winden","Winden"]
    }
df = pd.DataFrame(liste)

# Ersetzen der NaN Werte durch das Wort "unbekannt"
df2 = df.replace(np.nan, "Unbekannt")

print("Liste ursprünglich:")
print(df)
print("gefiltere Liste")
print(df2)
