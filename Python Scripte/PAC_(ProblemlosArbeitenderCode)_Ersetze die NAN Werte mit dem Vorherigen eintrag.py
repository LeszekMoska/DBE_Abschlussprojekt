import pandas as pd
import numpy as np

# Beispiel-DataFrame mit NaN-Werten
data = {
    'Spalte1': [1, 2, np.nan, 4, 5],
    'Spalte2': [5, 7, 8, 9, np.nan],
    'Spalte3': [11, 12, 13, np.nan, 15]
}

df = pd.DataFrame(data)

# NaN-Werte mit vorherigem Eintrag ersetzen
df2 = df.fillna(method='ffill')

# Hinweis aus Python: Die Verwendung von DataFrame.fillna mit 'method'
# wird als veraltet betrachtet und wird in einer kommenden Version von Pandas
# eine Warnung auslösen. Es wird empfohlen,
# stattdessen obj.ffill() oder obj.bfill() zu verwenden.""

print("Ursprüngliches DataFrame:")
print(df)

print("\nDataFrame nach Ersetzen von NaN mit vorherigem Eintrag:")
print(df2)