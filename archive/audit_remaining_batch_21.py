import os

# Remaining tickers in Batch 21
remaining_tickers = [
    "4933", "4934", "4935", "4938", "4939", 
    "4942", "4943", "4949", "4950", "4951", 
    "4952", "4953", "4956", "4958", "4960", 
    "4961", "4966", "4967"
]

print(f"Auditing {len(remaining_tickers)} remaining tickers in Batch 21...")

to_enrich = []
missing = []
already_done = []

for ticker in remaining_tickers:
    found_path = None
    # Find file
    for root, dirs, files in os.walk('f:/My TW Coverage/Pilot_Reports'):
        for file in files:
            if file.startswith(f"{ticker}_"):
                found_path = os.path.join(root, file)
                break
        if found_path: break
    
    if not found_path:
        missing.append(ticker)
    else:
        # Check enrichment
        try:
            with open(found_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Check for "業務簡介" and absence of English "Business Description"
                if "## 業務簡介" in content and "Business Description" not in content:
                    already_done.append(ticker)
                else:
                    to_enrich.append(ticker)
        except:
             print(f"{ticker}: ERROR READING")

print("-" * 30)
print(f"ALREADY DONE ({len(already_done)}): {already_done}")
print(f"MISSING ({len(missing)}): {missing}")
print(f"TO ENRICH ({len(to_enrich)}): {to_enrich}")
