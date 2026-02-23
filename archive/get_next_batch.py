import os
import re

def get_next_batch(batch_size=20):
    base_dir = r"f:\My TW Coverage\Pilot_Reports"
    unenriched_reports = []

    print(f"Scanning {base_dir}...")

    # Regex to capture ticker and name: "1234_Name.md"
    file_pattern = re.compile(r"^(\d{4})_(.+)\.md$")

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            match = file_pattern.match(filename)
            if match:
                ticker = match.group(1)
                filepath = os.path.join(root, filename)
                
                # Check for enrichment signature
                # We can check if the file contains "成立於" (Founded in) which is part of our Chinese template
                # Or simply check if the first paragraph is predominantly English.
                is_enriched = False
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read(1000) # Read first 1000 chars
                        if "成立於" in content and "總部位於" in content:
                            is_enriched = True
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
                    continue

                if not is_enriched:
                    unenriched_reports.append({
                        "ticker": int(ticker),
                        "filename": filename,
                        "path": filepath
                    })

    # Sort by ticker
    unenriched_reports.sort(key=lambda x: x["ticker"])

    # Get batch
    batch = unenriched_reports[:batch_size]

    print(f"Found {len(unenriched_reports)} unenriched reports total.")
    print(f"Next {len(batch)} tickers to enrich:")
    for item in batch:
        print(f"{item['ticker']}|{item['path']}")

if __name__ == "__main__":
    get_next_batch()
