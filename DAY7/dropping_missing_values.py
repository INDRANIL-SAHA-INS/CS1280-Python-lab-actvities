import pandas as pd
import numpy as py
data = {'A': [1, 2, np.nan, 4],
'B': [5, np.nan, 7, 8],
'C': [9, 10, 11, np.nan]}
df = pd.DataFrame(data)
print(df)
print("-------------------------")
# Drop rows with missing values
df.dropna(inplace=True) # Modify df directly
print(df) # Print the modified DataFrame
print("-------------------------")
# Fill missing values with 0
df.fillna(0, inplace=True)
print(df)
print("-------------------------")
# Fill missing values with the mean of the column
df["C"].fillna(df["C"].mean(), inplace=True)
print(df)
print("-------------------------")
# Fill missing values with mean - no warning
df_new = df.copy()
df_new["C"] = df_new["C"].fillna(df_new["C"].mean())
print(df_new)
