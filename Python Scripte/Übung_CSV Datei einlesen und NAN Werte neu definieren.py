import numpy as np
import pandas as pd

# Pfad zur CSV-Datei
csv = 'C:/Users/User/Desktop/Projekte/Mitarbeiter_Neu.csv'

# CSV-Datei in ein Pandas DataFrame laden
df = pd.read_csv(csv,na_values='np.nan')

# NaN-Werte durch das Wort "Unbekannt" ersetzen
df2 = df.fillna(value='!!!!INFO FEHLT!!!!')

# Ausgabe des DataFrames
print(df2)