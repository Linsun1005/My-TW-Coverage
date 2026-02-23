import pandas as pd

try:
    df = pd.read_excel('f:/My TW Coverage/Taiwan Stock Exception.xlsx', header=None)
    print("First 5 rows:")
    print(df.head())
    print("\nColumns:")
    print(df.columns)
except Exception as e:
    print(f"Error reading excel: {e}")
