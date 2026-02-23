import yfinance as yf
import pandas as pd

ticker = "1708.TW"
stock = yf.Ticker(ticker)

print(f"Fetching data for {ticker}...")
try:
    # Get income statement
    income_stmt = stock.income_stmt
    if not income_stmt.empty:
        # Get Total Revenue for the latest available year
        revenue_row = income_stmt.loc['Total Revenue']
        latest_revenue = revenue_row.iloc[0]
        revenue_date = revenue_row.index[0]
        
        print(f"Date: {revenue_date}")
        print(f"Raw Total Revenue: {latest_revenue}")
        print(f"Format: {latest_revenue:,.0f}")
        
    else:
        print("Income statement is empty.")

except Exception as e:
    print(f"Error: {e}")
