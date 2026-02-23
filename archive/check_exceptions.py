import pandas as pd
import os

exception_path = 'f:/My TW Coverage/Taiwan Stock Exception.xlsx'
missing_tickers = [4567, 4570, 4574, 4578, 4579]

if os.path.exists(exception_path):
    try:
        df = pd.read_excel(exception_path, header=None)
        # Convert to string for comparison
        exceptions = df[0].astype(str).str.strip().tolist()
        print("Exceptions found:")
        for ticker in missing_tickers:
            if str(ticker) in exceptions:
                print(f"{ticker}: YES (In Exception List)")
            else:
                print(f"{ticker}: NO (Not in Exception List)")
    except Exception as e:
        print(f"Error reading exception file: {e}")
else:
    print("Exception file not found.")
