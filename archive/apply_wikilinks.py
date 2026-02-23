import os
import re

reports_dir = r"f:\My TW Coverage\Pilot_Reports"

ENTITIES = [
    "Apple", "NVIDIA", "Google", "Meta", "Microsoft", "Amazon", "Tesla", "AMD", "Intel", 
    "TSMC", "鴻海", "聯發科", "廣達", "緯創", "技嘉", "微星", "華碩", "宏碁", "日月光", "Macnica",
    "台達電", "聯電", "台積電", "Samsung", "LG", "Sony", "Panasonic", "Siemens", "Bosch", 
    "Continental", "Denso", "Dell", "HP", "Lenovo", "SpaceX", "ON Semi", "OmniVision",
    "AI", "AI伺服器", "5G", "6G", "IoT", "物聯網", "車聯網", "ADAS", "電動車", "EV", 
    "低軌衛星", "Wi-Fi 6", "Wi-Fi 7", "Bluetooth", "Type-C", "PCIe", "伺服器", "資料中心",
    "消費性電子", "醫療器材", "網通", "工業電腦", "IPC", "EMS", "OEM", "ODM", "AR", "VR",
    "CSP", "雲端服務", "半導體", "第三代半導體", "SiC", "GaN", "MCU", "記憶體", "DRAM", "NAND",
    "CIS", "光通訊", "CPO", "連接器", "PCB", "ABF", "散熱", "水冷", "自動化", "機器人", "營造"
]

ENTITIES.sort(key=len, reverse=True)

def apply_wikilinks(text):
    # Split by existing wikilinks or bold text to avoid messing them up
    # Bold text like **company** will not be linked. That is okay.
    parts = re.split(r'(\[\[.*?\]\]|\*\*.*?\*\*)', text)
    
    for i in range(0, len(parts), 2):
        if not parts[i].strip(): continue
        for entity in ENTITIES:
            # For pure English entities, match whole word
            if re.match(r'^[A-Za-z0-9\-\s]+$', entity):
                escaped = re.escape(entity)
                # Ignore case for english matching
                parts[i] = re.sub(r'(?<![A-Za-z0-9\[\_\-\*])' + escaped + r'(?![A-Za-z0-9\]\_\-\*])', f'[[{entity}]]', parts[i], flags=re.IGNORECASE)
            else:
                parts[i] = parts[i].replace(entity, f'[[{entity}]]')
                
    return "".join(parts)

count = 0
for root, dirs, files in os.walk(reports_dir):
    for file in files:
        if file.endswith('.md'):
            fpath = os.path.join(root, file)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(fpath, 'r', encoding='big5') as f:
                        content = f.read()
                except Exception:
                    print(f"Skipping {file} due to encoding")
                    continue
            
            # Find the index of ## 財務概況
            fin_idx = content.find('## 財務概況')
            if fin_idx == -1:
                fin_idx = len(content)
                
            intro_text = content[:fin_idx]
            fin_text = content[fin_idx:]
            
            num_links = intro_text.count('[[')
            if num_links > 15:
                continue # Skip heavily linked files
                
            new_intro = apply_wikilinks(intro_text)
            
            if new_intro != intro_text:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_intro + fin_text)
                count += 1
                if count % 100 == 0:
                    print(f"Processed {count} files...")

print(f"Applied wikilinks to {count} files.")
