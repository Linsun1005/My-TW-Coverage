---
description: Workflow to enrich a single company ticker file with AI-generated, company-specific content.
---

# Enrich Ticker Workflow

This workflow is used to enrich a company's Markdown report with business details, supply chain position, and key customers/suppliers using AI.

## Prerequisites
- The target Markdown file must already exist (e.g., `f:\My TW Coverage\Pilot_Reports\Industry\Ticker_Name.md`).
- Only run this workflow when you are viewing the specific file you want to enrich.

## CRITICAL RULES
- **UTF-8 Encoding**: Every file write or modification MUST use UTF-8 encoding. Never use default shell encoding (like `Set-Content` without `-Encoding utf8`).
- **Clean Filenames**: NEVER use URL-encoded characters in filenames (e.g., use `3624_光頡.md`, NOT `3624_%E5%85%89%E9%A0%A1.md`).
- **Clean Overwrite**: If a file is suspected of containing binary junk or encoding errors, delete it via terminal before writing the fresh content.
- **Data Integrity**: **Metadata** (`板塊`, `產業`, `市值`, `企業價值`) and **Financial Tables** MUST be preserved exactly as they are in the original file. Do not regenerate or modify them.
- **Universal Tagging Rule**: EVERY identifiable entity (companies, vendors, partners) and key product/technology mentioned MUST be wrapped in `[[Wikilinks]]`. Consistency is mandatory: if you tag `[[Broadcom]]`, you must also tag `[[Jabil]]`. Inconsistent tagging breaks our competitive mapping capability.

## Steps

0.  **Missing File Procedure (If file does not exist)**:
    - If the target file is missing, you must generate it first.
    - Run the following command in the terminal:
      ```powershell
      # Optional: Providing --name helps create the correct filename immediately
      python "f:\My TW Coverage\02_generate_base_reports.py" --ticker <TICKER> --name "<COMPANY_NAME>"
      ```
    - **Note**: The script will check `Taiwan Stock Exception.xlsx`. If the ticker is in the exception list, it will skip generation.
    - Check the output to see where the file was created (usually in `f:\My TW Coverage\Pilot_Reports`).
    - Once generated (or skipped), proceed to **Step 1**.

1.  **Read the Target File**:
    - Use `view_file` to read the content of the Markdown file for the specific ticker.
    - **CRITICAL:** Note the existing metadata/header lines at the top of the file, specifically:
        - `板塊:` (Sector)
        - `產業:` (Industry)
        - `市值:` (Market Cap)
        - `企業價值:` (Enterprise Value)
    - **YOU MUST PRESERVE THESE LINES EXACTLY AS THEY ARE.** Do not overwrite, translate, or delete them.

2.  **Research the Company**:
    - Use `search_web` to find information about the company (Ticker + Name).
    - Focus on finding:
        - **Business Description**: What does the company do? What are its main products/services? History?
        - **Supply Chain Position**: Where does it sit in the supply chain (Upstream, Midstream, Downstream)? Who are its upstream suppliers and downstream customers?
        - **Key Customers & Suppliers**: Specific names of major customers and suppliers.

3.  **Enrich the Report (Write to File)**:
    - Use `write_to_file` to overwrite the *entire* file with the enriched content.
    - **Structure:**
        - **Header**: Keep the `# Ticker - Name` header.
        - **Metadata**: **RESTORE the `板塊`, `產業`, `市值`, `企業價值` lines exactly as they were in the original file.**
        - **Business Description (業務簡介)**:
            - **REPLACE the entire original English description** with a **Traditional Chinese** translation.
            - **COMPREHENSIVE TAGGING:** Add `[[Wikilinks]]` for every major product, manufacturing process, and target market. This data is used to find "product peers" and competitors.
            - **ENSURE the original English text is completely removed.**
            - Ensure the tone is professional and informative.
        - **Supply Chain Position (供應鏈位置)**:
            - Describe the company's position (Upstream/Midstream/Downstream).
            - List Upstream (Materials/Components) and Downstream (Applications/End Products) with wikilinks.
        - **Key Customers & Suppliers (主要客戶及供應商)**:
            - List specific major customers and suppliers with wikilinks where possible.
        - **Financial Overview (財務概況)**:
            - **KEEP THE FINANCIAL SECTION UNTOUCHED.**
            - If the original file had a financial table or placeholder, preserve it exactly. Do not regenerate or modify the financial data unless explicitly instructed.

## Example Output Format

```markdown
# 1234 - Example Co

## 業務簡介
**板塊:** Technology
**產業:** Electronic Components
**市值:** 10,000 百萬台幣
**企業價值:** 12,000 百萬台幣

Example Co 是一家專注於 [[半導體]] 封測的廠商... (Traditional Chinese description with [[wikilinks]])

## 供應鏈位置
*   **上游**: [[晶圓代工]] (e.g., [[TSMC]]), [[導線架]].
*   **中游**: **Example Co** (封測).
*   **下游**: [[消費性電子]], [[車用電子]].

## 主要客戶及供應商
### 主要客戶
*   [[Apple]], [[NVIDIA]].

### 主要供應商
*   [[日月光]], [[長華]].

## 財務概況 (單位: 百萬台幣, 只有 Margin 為 %)
(Preserve existing financial tables)
...
```

4.  **Verification**:
    - Review the generated file to ensure:
        - Metadata lines are present and correct.
        - Business description is in Traditional Chinese with wikilinks.
        - **NO original English description remains.**
        - Financial section is present and unmodified.
