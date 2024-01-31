import numpy as np
import pandas as pd

# Zufällige Zahlen und NaN-Werte erstellen
liste =np.array([10,5,np.nan,5,np.nan,3])
df = pd.DataFrame(liste,columns=['Spalte 1'])

# Filtern der NAN Werte aus der Liste

df2 = df[df['Spalte 1'].isnull()]

print("Liste ursprünglich:")
print(df)
print("gefiltere Liste")
print(df2)