"""
update_valuation.py — Refresh ONLY the valuation multiples (估值指標) in ticker reports.

Much faster than update_financials.py since it only fetches stock.info (no financial statements).
Updates: P/E (TTM), Forward P/E, P/S, P/B, EV/EBITDA, stock price, and period dates.
Preserves all other content including financial tables.

Usage:
  python scripts/update_valuation.py                     # ALL tickers
  python scripts/update_valuation.py 2330                # Single ticker
  python scripts/update_valuation.py 2330 2317 3034      # Multiple tickers
  python scripts/update_valuation.py --batch 101         # By batch
  python scripts/update_valuation.py --sector Semiconductors  # By sector
  python scripts/update_valuation.py --dry-run 2330      # Preview without writing
"""

import os
import re
import sys
import time
from datetime import date, datetime

import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import find_ticker_files, parse_scope_args


def fetch_valuation(ticker):
    """Fetch valuation multiples only. Tries .TW then .TWO."""
    for suffix in [".TW", ".TWO"]:
        try:
            stock = yf.Ticker(f"{ticker}{suffix}")
            info = stock.info
            if not info or not info.get("currentPrice"):
                continue

            valuation = {}
            for key, label in [
                ("trailingPE", "P/E (TTM)"),
                ("forwardPE", "Forward P/E"),
                ("priceToSalesTrailing12Months", "P/S (TTM)"),
                ("priceToBook", "P/B"),
                ("enterpriseToEbitda", "EV/EBITDA"),
            ]:
                val = info.get(key)
                valuation[label] = f"{val:.2f}" if val else "N/A"

            # Price and period info
            cur_price = info.get("currentPrice")
            valuation["_price"] = f"{cur_price:,.2f}" if cur_price else None

            mrq = info.get("mostRecentQuarter")
            nfy = info.get("nextFiscalYearEnd")
            valuation["_ttm_end"] = (
                datetime.fromtimestamp(mrq).strftime("%Y-%m-%d") if mrq else None
            )
            valuation["_fwd_end"] = (
                datetime.fromtimestamp(nfy).strftime("%Y-%m-%d") if nfy else None
            )

            # Also update market cap and enterprise value
            market_cap = (
                f"{info['marketCap'] / 1_000_000:,.0f}"
                if info.get("marketCap")
                else None
            )
            enterprise_value = (
                f"{info['enterpriseValue'] / 1_000_000:,.0f}"
                if info.get("enterpriseValue")
                else None
            )

            return {
                "valuation": valuation,
                "market_cap": market_cap,
                "enterprise_value": enterprise_value,
                "suffix": suffix,
            }
        except Exception:
            continue
    return None


def build_valuation_table(v):
    """Build the 估值指標 markdown section."""
    headers = ["P/E (TTM)", "Forward P/E", "P/S (TTM)", "P/B", "EV/EBITDA"]
    values = [v.get(h, "N/A") for h in headers]
    widths = [max(len(h), len(val)) for h, val in zip(headers, values)]
    header_row = "| " + " | ".join(h.rjust(w) for h, w in zip(headers, widths)) + " |"
    sep_row = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    val_row = "| " + " | ".join(val.rjust(w) for val, w in zip(values, widths)) + " |"

    # Period and price annotation
    today = date.today().strftime("%Y-%m-%d")
    ttm_end = v.get("_ttm_end")
    fwd_end = v.get("_fwd_end")
    price = v.get("_price")

    period_parts = []
    if price:
        period_parts.append(f"股價 ${price} as of {today}")
    if ttm_end:
        period_parts.append(f"TTM 截至 {ttm_end}")
    if fwd_end:
        period_parts.append(f"Forward 預估至 {fwd_end}")
    period_note = " | ".join(period_parts) if period_parts else ""

    title = f"### 估值指標 ({period_note})\n" if period_note else "### 估值指標\n"
    return title + header_row + "\n" + sep_row + "\n" + val_row


def update_file(filepath, ticker, dry_run=False):
    """Update only the valuation section in a ticker file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    data = fetch_valuation(ticker)
    if data is None:
        print(f"  {ticker}: SKIP (no data)")
        return False

    v = data["valuation"]
    new_table = build_valuation_table(v)

    # Replace existing 估值指標 section (between ### 估值指標 and ### 年度)
    if "### 估值指標" in content:
        content = re.sub(
            r"### 估值指標.*?(?=\n### 年度)",
            new_table + "\n",
            content,
            flags=re.DOTALL,
        )
    elif "## 財務概況" in content:
        # No valuation section yet — insert before 年度
        content = content.replace(
            "### 年度關鍵財務數據",
            new_table + "\n\n### 年度關鍵財務數據",
        )

    # Update market cap and enterprise value metadata
    if data.get("market_cap"):
        content = re.sub(
            r"(\*\*市值:\*\*) .+?百萬台幣",
            rf"\1 {data['market_cap']} 百萬台幣",
            content,
        )
    if data.get("enterprise_value"):
        content = re.sub(
            r"(\*\*企業價值:\*\*) .+?百萬台幣",
            rf"\1 {data['enterprise_value']} 百萬台幣",
            content,
        )

    if dry_run:
        print(f"  {ticker}: WOULD UPDATE ({data['suffix']})")
        return True

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {ticker}: UPDATED ({data['suffix']})")
    return True


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    args = [a for a in sys.argv[1:]]
    dry_run = "--dry-run" in args
    if dry_run:
        args.remove("--dry-run")

    tickers, sector, desc = parse_scope_args(args)
    print(f"Updating valuation for {desc}...")
    files = find_ticker_files(tickers, sector)

    if not files:
        print("No matching files found.")
        return

    print(f"Found {len(files)} files.\n")
    updated = failed = skipped = 0

    for ticker in sorted(files.keys()):
        try:
            if update_file(files[ticker], ticker, dry_run):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  {ticker}: ERROR ({e})")
            failed += 1
        time.sleep(0.3)  # Lighter rate limit than full financials

    print(f"\nDone. Updated: {updated} | Skipped: {skipped} | Failed: {failed}")


if __name__ == "__main__":
    main()
