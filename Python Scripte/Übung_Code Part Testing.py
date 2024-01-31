import pandas as pd

# Dateipfade einer Variable zuordnen

csv_1 = "C:/Users/User/Desktop/Projekte/Mitarbeiter.csv"
csv_2 = "C:/Users/User/Desktop/Projekte/Daten Leszek.csv"

# CSV-Dateien in Pandas DataFrames laden

dataframe1 = pd.read_csv(csv_1)
dataframe2 = pd.read_csv(csv_2)

# Beide Deteien, brauchen ein gemeinsames merkmal! Zusammenfuehren der DataFrames
# basierend auf einer gemeinsamen Spalte (z.B. 'ID')
# gemeinsame_spalte = 'ID'
# zusammengefuehrtes_dataframe = pd.merge(dataframe1, dataframe2, on=gemeinsame_spalte)

csv_zusammengefuehrt = pd.merge(dataframe1, dataframe2, on=4)
