import yfinance as yf
import pandas as pd

def test_tickers(tickers):
    for symbol in tickers:
        ticker_str = f"{symbol}.TW"
        print(f"\nTesting {ticker_str}...")
        try:
            stock = yf.Ticker(ticker_str)
            info = stock.info
            
            # Check for key data points
            print(f"Name: {info.get('longName', 'N/A')}")
            print(f"Sector: {info.get('sector', 'N/A')}")
            print(f"Industry: {info.get('industry', 'N/A')}")
            print(f"Business Summary: {info.get('longBusinessSummary', 'N/A')[:100]}...")
            
            # Financials
            print("Income Statement (Last 2 years):")
            print(stock.income_stmt.iloc[:, :2] if not stock.income_stmt.empty else "Empty")
            
        except Exception as e:
            print(f"Error fetching {ticker_str}: {e}")

if __name__ == "__main__":
    # 2330: TSMC (known good), 1708: Sample from user list
    test_tickers(['2330', '1708'])
