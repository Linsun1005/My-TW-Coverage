import pandas as pd

try:
    df = pd.read_excel('f:/My TW Coverage/Taiwan Stock Coverage.xlsx', header=None)
    print("Shape:", df.shape)
    print("First 5 rows:")
    print(df.head().to_string())
    
    # Assumption: Tickers are in the first column. Let's verify.
    first_col_sample = df.iloc[:, 0].head(10).tolist()
    print("\nSample from first column:", first_col_sample)
    
except Exception as e:
    print(e)
