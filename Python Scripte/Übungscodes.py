import numpy as np
import pandas as pd

# Bestehende Arrays erstellen,
# "a_header" stellt hierbei Spaltenüberschriften der künftigen Tabelle dar
a_header = np.array(["Name", "Nachname", "Wohnort"])
b_data = np.array([["Leszek", "Moska", "Welschneudorf"],
                   ["Kasia", "Moska", "Winden"],
                   ["Martin", "Moska", "Winden"]])

# Erstellung einer Tabelle in dem das a_header als Spaltenüberschrift dargestellt wird
# Dazu nutzen wir den Befehl pd.DataFrame, mir diesem legt man fest, welche Informationen
# aus den gegeben Arrays was in der gewünschten Tabelle darstellen sollen
df = pd.DataFrame(b_data, columns=a_header)
print(df)
import pandas as pd