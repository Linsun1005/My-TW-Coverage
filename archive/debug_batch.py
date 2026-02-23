import os

# Tickers for Batch 17 from task.md
tickers = [
    "3712", "3713", "3714", "3715", "3717", "4113", "4154", "4171", "4303", "4304", 
    "4305", "4306", "4401", "4402", "4406", "4413", "4414", "4416", "4417", "4420", 
    "4426", "4430", "4431", "4432", "4433", "4438", "4439", "4440", "4441", "4442"
]

print(f"Checking {len(tickers)} tickers for Batch 17...")

missing_files = []
unenriched_files = []

for ticker in tickers:
    found = False
    # Walk through Pilot_Reports to find the file
    for root, dirs, files in os.walk('f:/My TW Coverage/Pilot_Reports'):
        for file in files:
            if file.startswith(f"{ticker}_"):
                found = True
                path = os.path.join(root, file)
                
                # Check for enrichment
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                        has_chinese_header = "## 業務簡介" in content
                        has_english_residue = "Business Description" in content
                        
                        status = "Enriched" if has_chinese_header else "NOT Enriched"
                        if not has_chinese_header:
                            unenriched_files.append(ticker)
                        else:
                            # print(f"{ticker}: {status} - {file}")
                            pass
                            
                except Exception as e:
                    print(f"{ticker}: Error reading file - {e}")
                
                break
        if found: break
    
    if not found:
        print(f"{ticker}: MISSING FILE")
        missing_files.append(ticker)

print("-" * 30)
print(f"Summary for Batch 17:")
print(f"Missing Files: {len(missing_files)} -> {missing_files}")
print(f"Unenriched Files: {len(unenriched_files)} -> {unenriched_files}")
if len(missing_files) == 0 and len(unenriched_files) == 0:
    print("Batch 17 appears COMPLETE.")
else:
    print("Batch 17 is INCOMPLETE.")
