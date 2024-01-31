import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000, np.nan],
    'Duration':[np.nan,'40days','35days'],
    'Discount':[1000,np.nan,1500]
               }
df = pd.DataFrame(technologies)
print(df)

#Replace NaN with zero on all columns
df2 = df.fillna(0)
print(df2)

#Repalce inplace
df = pd.DataFrame(technologies)
df.fillna(0,inplace=True)
print(df)

# Replace on single column
df = pd.DataFrame(technologies)
df["Fee"] = df["Fee"].fillna(0)
print(df)

# Replace on multiple columns
df = pd.DataFrame(technologies)
df[["Fee","Duration"]] = df[["Fee","Duration"]].fillna(0)
print(df)

# Using replace()
df = pd.DataFrame(technologies)
df["Fee"] = df["Fee"].replace(np.nan, 0)
print(df)

# Using replace()
df = pd.DataFrame(technologies)
df2 = df.replace(np.nan, 0)
print(df2)