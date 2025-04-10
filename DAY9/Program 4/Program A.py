import pandas as pd

file_path = "1experience.csv"

try:
    df = pd.read_csv(file_path)

    print("CSV File Content:")
    print(df)

    rows, columns = df.shape
    print(f"\nTotal Rows: {rows}")
    print(f"Total Columns: {columns}")

    print(f"\nLength of the File: {rows} rows")

    print("\nFirst 2 Rows:")
    print(df.head(2))

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' contains invalid data format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
