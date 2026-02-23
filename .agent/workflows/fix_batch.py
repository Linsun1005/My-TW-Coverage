import os
import glob
import sys
import re

# Add current dir to path to import data chunks
sys.path.append(os.path.dirname(__file__))

DATA = {
    # "TICKER": {
    #     "desc": "...",
    #     "up": "...",
    #     "mid": "...",
    #     "down": "...",
    #     "cust": "...",
    #     "supp": "..."
    # }
}

BASE_DIR = r"F:\My TW Coverage\Pilot_Reports"

def update_file(filepath, ticker):
    if ticker not in DATA:
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_data = DATA[ticker]
    
    # 1. Business Description (Replace everything between 企業價值 and 供應鏈位置)
    content = re.sub(
        r'(## 業務簡介.*?企業價值:.*?\n\n)(.*?)(?=\n## 供應鏈位置)', 
        rf'\g<1>{new_data["desc"]}\n', 
        content, 
        flags=re.DOTALL
    )
    
    # 2. Supply Chain Data
    supply_chain_text = f"*   **上游**: {new_data['up']}\n" \
                        f"*   **中游**: {new_data['mid']}\n" \
                        f"*   **下游**: {new_data['down']}\n"
    content = re.sub(
        r'(## 供應鏈位置\n)(.*?)(?=\n## 主要客戶及供應商)',
        rf'\g<1>{supply_chain_text}', 
        content, 
        flags=re.DOTALL
    )
    
    # 3. Key Customers & Suppliers
    cust_supp_text = f"### 主要客戶\n*   {new_data['cust']}\n\n" \
                     f"### 主要供應商\n*   {new_data['supp']}\n"
    content = re.sub(
        r'(## 主要客戶及供應商\n)(.*?)(?=\n## 財務概況)',
        rf'\g<1>{cust_supp_text}', 
        content, 
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Enriched: {os.path.basename(filepath)}")

def main():
    for filepath in glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True):
        filename = os.path.basename(filepath)
        match = re.search(r'^(\d{4})_', filename)
        if match:
            ticker = match.group(1)
            if ticker in DATA:
                update_file(filepath, ticker)

if __name__ == "__main__":
    main()
