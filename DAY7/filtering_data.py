import pandas as pd
print (df)
print(df["Age"]>26)
print(df[df["Age"]>26])import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Ram', 'Robert', 'Rahim'],
    'Age': [25, 30, 35],
    'City': ['Ayodya', 'Chennai', 'Delhi']
}
df = pd.DataFrame(data)
print(df)
print("--------------")
print(df["Age"]>26)
print("--------------")
print(df[df["Age"]>26])
