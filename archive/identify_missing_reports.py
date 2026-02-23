import pandas as pd
import os

def main():
    excel_path = 'f:/My TW Coverage/Taiwan Stock Coverage.xlsx'
    output_dir = 'f:/My TW Coverage/Pilot_Reports'
    report_path = 'f:/My TW Coverage/Missing_Reports.md'
    
    # 1. Read Master List
    try:
        df = pd.read_excel(excel_path, header=None)
        # Ensure tickers are strings and stripped of whitespace
        master_tickers = set(df.iloc[:, 0].astype(str).str.strip())
        master_dict = dict(zip(df.iloc[:, 0].astype(str).str.strip(), df.iloc[:, 1]))
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return

    # 2. Read Generated Reports
    generated_tickers = set()
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            if filename.endswith(".md"):
                # Extract ticker from filename "1234_Name.md"
                # Split by first underscore
                parts = filename.split('_')
                if parts:
                    ticker = parts[0]
                    generated_tickers.add(ticker)
    
    # 3. Find Missing
    missing_tickers = sorted(list(master_tickers - generated_tickers))
    
    # 4. Generate Markdown Report
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Missing Base Reports\n\n")
        f.write(f"**Total Tickers in Excel:** {len(master_tickers)}\n")
        f.write(f"**Total Reports Generated:** {len(generated_tickers)}\n")
        f.write(f"**Missing Count:** {len(missing_tickers)}\n\n")
        f.write("| Ticker | Name | Recommended Action |\n")
        f.write("| :--- | :--- | :--- |\n")
        
        for ticker in missing_tickers:
            name = master_dict.get(ticker, "Unknown")
            f.write(f"| {ticker} | {name} | Verify if delisted or requires specific suffix |\n")
            
    print(f"Missing reports list generated at: {report_path}")
    print(f"Found {len(missing_tickers)} missing tickers.")

if __name__ == "__main__":
    main()
