import os
import sys

def main():
    if len(sys.argv) > 1:
        ticker = sys.argv[1].strip()
    else:
        ticker = input("Enter ticker to open: ").strip()
        
    reports_dir = r"f:\My TW Coverage\Pilot_Reports"
    
    for root, dirs, files in os.walk(reports_dir):
        for file in files:
            # Check if the file starts with the ticker (e.g. 2330_台積電.md)
            if file.startswith(str(ticker)) and file.endswith(".md"):
                fpath = os.path.join(root, file)
                print(f"Found: {fpath}")
                # Opens the file in VS Code
                os.system(f'code "{fpath}"')
                return
                
    print(f"Could not find a Markdown report for ticker: {ticker}")

if __name__ == "__main__":
    # You can run this script with `python open_ticker.py 2330` 
    # or just `python open_ticker.py` and it will prompt you.
    main()
