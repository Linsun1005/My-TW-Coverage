import yfinance as yf
import pandas as pd

ticker = "2330.TW" # TSMC as proxy
stock = yf.Ticker(ticker)

print(f"Checking fields for {ticker}...")

try:
    fin = stock.income_stmt
    cf = stock.cashflow
    
    required_fin = [
        "Total Revenue",
        "Gross Profit",
        "Selling And Marketing Expense",
        "General And Administrative Expense",
        "Operating Income",
        "Net Income"
    ]
    
    required_cf = [
        "Operating Cash Flow",
        "Investing Cash Flow",
        "Financing Cash Flow",
        "Capital Expenditure"
    ]
    
    print("\n--- Income Statement Check ---")
    for field in required_fin:
        if field in fin.index:
            print(f"[OK] {field}")
        else:
            print(f"[MISSING] {field}")
            # Try to find close matches
            matches = [i for i in fin.index if "Selling" in str(i) or "General" in str(i) or "Admin" in str(i)]
            if matches and ("Selling" in field or "General" in field):
                 print(f"   Potential matches: {matches}")

    print("\n--- Cash Flow Check ---")
    # yfinance cashflow keys can be tricky (often 'Total Cash From Operating Activities' etc)
    # Let's check common ones
    for field in required_cf:
        if field in cf.index:
            print(f"[OK] {field}")
        else:
            print(f"[MISSING] {field}")
            if field == "Capital Expenditure":
                matches = [i for i in cf.index if "Capital" in str(i) or "Purchase" in str(i)]
                print(f"   Potential matches: {matches}")
            elif "Operating" in field:
                 matches = [i for i in cf.index if "Operating" in str(i)]
                 print(f"   Potential matches: {matches}")
            elif "Investing" in field:
                 matches = [i for i in cf.index if "Investing" in str(i)]
                 print(f"   Potential matches: {matches}")
            elif "Financing" in field:
                 matches = [i for i in cf.index if "Financing" in str(i)]
                 print(f"   Potential matches: {matches}")

except Exception as e:
    print(f"Error: {e}")
