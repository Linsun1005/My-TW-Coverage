import yfinance as yf
import pandas as pd

ticker = "2330.TW"
stock = yf.Ticker(ticker)

print(f"Fetching financials for {ticker}...")
try:
    fin = stock.financials
    print("\n--- Income Statement Fields ---")
    print(fin.index.tolist())
    
    cf = stock.cashflow
    print("\n--- Cash Flow Fields ---")
    print(cf.index.tolist())
    
    bs = stock.balance_sheet
    print("\n--- Balance Sheet Fields ---")
    print(bs.index.tolist())

except Exception as e:
    print(f"Error: {e}")
