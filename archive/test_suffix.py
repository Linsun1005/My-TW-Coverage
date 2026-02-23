import yfinance as yf

def test_ticker(ticker_symbol):
    print(f"Testing {ticker_symbol}...")
    try:
        t = yf.Ticker(ticker_symbol)
        info = t.info
        if info and 'longName' in info:
            print(f"SUCCESS: {ticker_symbol} -> {info['longName']}")
            return True
        else:
            print(f"FAILED: {ticker_symbol} (No info/longName)")
            return False
    except Exception as e:
        print(f"ERROR: {ticker_symbol} -> {e}")
        return False

# Test a known OTC stock (2071 is likely one based on previous failure)
# and a known listed stock just to be sure.
test_ticker("2071.TW")
test_ticker("2071.TWO")
test_ticker("1480.TW")
test_ticker("1480.TWO")
