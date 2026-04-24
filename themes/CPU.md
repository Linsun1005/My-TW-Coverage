# CPU 處理器產業鏈 CPU Supply Chain

> 從 CPU 架構 IP、晶片設計、晶圓代工、封裝基板、測試、散熱到系統組裝 — 台灣在 Intel/AMD/Arm/RISC-V 生態系中的完整角色

**涵蓋公司數:** 42

**相關主題:** [[CoWoS]] (39) | [[AI 伺服器]] (154) | [[ABF 載板]] (14) | [[HBM]] (17) | [[探針卡與鑽針]] (28)

---

## 全球 CPU 設計競爭格局

| 架構/陣營 | 主要設計商 | 台灣供應鏈角色 |
|-----------|-----------|----------------|
| x86 | [[Intel]] (美)、[[AMD]] (美) | 代工 (台積電)、封裝 (日月光)、基板 (欣興/南電)、Socket (嘉澤) |
| [[Arm]] | [[Qualcomm]] (美)、[[Apple]] (美)、[[聯發科]] (台)、[[Samsung]] (韓) | IP 授權→SoC 設計→台積電代工→日月光封測 |
| [[RISC-V]] | [[晶心科]] (台)、SiFive (美) | 台灣唯一 RISC-V CPU IP 領導廠 |
| 伺服器 CPU | [[Intel]] Xeon、[[AMD]] EPYC、[[Arm]] Neoverse | 台灣 ODM 佔全球伺服器 90%+ 產能 |

---

## A. CPU 架構 IP 與晶片設計 (6)

### CPU IP 矽智財
- **6533 晶心科** (Semiconductor Equipment & Materials) — 全球第五大處理器 CPU IP 供應商、[[RISC-V]] 國際協會創始首席會員；有別於 [[Arm]] 高授權費模式，專注開源高效 RISC-V 架構
- **3035 智原** (Semiconductor Equipment & Materials) — ASIC 設計服務及矽智財授權；IP 涵蓋 [[Arm]] 相容 CPU、[[DDR]] 控制器、[[USB]]、[[PCIe]] 介面

### ASIC / SoC 設計服務
- **3661 世芯-KY** (Semiconductors) — AI/HPC 客製化 ASIC 設計服務龍頭；專注台積電 7nm/5nm/3nm 先進製程，[[CoWoS]] 封裝整合
- **3443 創意** (Semiconductors) — ASIC 設計服務與 IP 供應商；台積電最大股東，涵蓋先進製程 IP 驗證
- **8054 安國** (Computer Hardware) — IC 設計及 ASIC 服務；最新 [[Arm]] 架構 CPU 平台「Mobius100」(8 核 CSS V3)

### 行動/通訊 SoC 設計
- **2454 聯發科** (Semiconductors) — 全球前四大 IC 設計公司；手機 AP SoC（含 CPU/GPU/ISP/Modem）、AI ASIC 晶片、[[Wi-Fi 7]]、[[5G]] 數據機

## B. 晶圓代工 Manufacturing (2)

- **2330 台積電** (Semiconductors) — 全球最大純晶圓代工廠（市佔逾 60%）；為 [[AMD]] EPYC/Ryzen、[[Apple]] M 系列、[[Qualcomm]] Snapdragon、[[聯發科]] 天璣系列代工 3nm/5nm
- **2303 聯電** (Semiconductors) — 成熟及特殊製程代工 (22nm–0.6μm)；CPU 周邊晶片（電源管理 IC、I/O 控制器）

## C. 封裝與基板 Packaging & Substrate (6)

### IC 封裝測試
- **3711 日月光投控** (Semiconductors) — **全球最大封測廠 (OSAT)**；CPU/GPU [[覆晶封裝]] (Flip Chip)、[[CoWoS]]、[[InFO]] 先進封裝

### ABF 載板（CPU 封裝關鍵）
- **3037 欣興** (Electronic Components) — **全球最大 [[ABF 載板]]及 PCB 廠**；供應 [[Intel]]、[[AMD]] 伺服器 CPU 及 AI GPU 載板
- **8046 南電** (Electronic Components) — 全球前三大 [[ABF 載板]]供應商；高階 GPU/CPU/網通 ASIC 封裝基板，AI 伺服器受惠
- **3189 景碩** (Semiconductor Equipment & Materials) — 前三大 Flip Chip IC 基板廠；ABF/BT/BGA 基板

### 基板上游材料
- **1303 南亞** (Specialty Chemicals) — 台塑集團電子材料事業：[[銅箔基板]] (CCL)、[[玻纖布]]、[[銅箔]]；ABF 載板核心原料供應
- **6213 聯茂** (Electronic Components) — 高頻高速 CCL 銅箔基板；供應 [[AMD]]、高階伺服器/網通板材

## D. CPU Socket 與焊接 (2)

- **3533 嘉澤** (Electronic Components) — **全球前三大 CPU Socket 供應商**；與 [[Intel]] 及 [[AMD]] 長期共同開發 LGA/PGA 腳座，跨足 [[DDR5]] DIMM Socket 及高速連接器
- **3305 昇貿** (Electronic Components) — 全球前三大錫膏/焊接材料廠；CPU/GPU Socket 高可靠度焊接材料，[[AI 伺服器]]帶動高毛利產品需求

## E. 散熱解決方案 Thermal (4)

- **3017 奇鋐** (Electronic Components) — **全球散熱方案龍頭 ([[AVC]])**；[[AI 伺服器]]散熱頭號概念股，[[液冷]]冷板/CDU、氣冷散熱模組
- **3653 健策** (Electronic Components) — **台灣最大均熱片 (Vapor Chamber) 廠**；[[NVIDIA]] GPU 及 CPU 高階均熱片與散熱模組關鍵供應商
- **3324 雙鴻** (Computer Hardware) — 全球前三大散熱管理與[[液冷]]方案廠；伺服器/筆電散熱模組
- **2241 艾姆勒** (Auto Parts) — 高功率晶片散熱方案；[[粉末冶金]]及 [[MIM]] 技術，跨足 AI 伺服器 GPU 散熱及雙相浸沒式[[液冷]]

## F. 測試介面 Test Interface (3)

- **6510 精測** (Semiconductor Equipment & Materials) — 全球前三大 MEMS [[探針卡]]；CPU/GPU 晶圓測試，美國客戶佔營收逾 60%
- **6223 旺矽** (Semiconductor Equipment & Materials) — 全球前五大[[探針卡]]廠；AI GPU/CPU 高頻高速量測
- **6515 穎崴** (Semiconductors) — 全球第一大測試座；[[CoWoS]]/[[InFO]] 先進封裝測試，全球前 20 大半導體廠 90% 為客戶

## G. BIOS 韌體 Firmware (1)

- **6231 系微** (Software - Application) — **UEFI BIOS 韌體全球領導廠**；[[Intel]]、[[AMD]]、[[Arm]] 伺服器/PC 平台 BIOS；BMC 管理韌體

## H. 主機板設計 Motherboard (3)

- **2376 技嘉** (Computer Hardware) — 主機板/顯卡/AI 伺服器；[[Intel]]、[[AMD]] 桌機/伺服器處理器平台，[[NVIDIA]] GPU 板卡
- **2377 微星** (Computer Hardware) — 電競品牌主機板/顯卡/筆電；[[Intel]]、[[AMD]] CPU 平台，跨足 AI 伺服器
- **3515 華擎** (Computer Hardware) — 主機板設計與 AI 伺服器 ODM；[[AMD]]、[[Intel]]、[[NVIDIA]] 平台

## I. 伺服器 ODM / 系統整合 (7)

### Tier 1 伺服器 ODM
- **2382 廣達** (Computer Hardware) — **全球最大筆電 ODM 及主要 AI 伺服器 ODM**；[[Intel]] Xeon、[[AMD]] EPYC、[[NVIDIA]] GPU 伺服器
- **3231 緯創** (Computer Hardware) — 筆電/伺服器 ODM；[[NVIDIA]]、[[Intel]]、[[AMD]] AI 伺服器
- **6669 緯穎** (Computer Hardware) — 雲端超大規模伺服器 ODM-Direct 模式；[[AMD]]、[[Intel]]、[[NVIDIA]] GPU/CPU 平台

### AI / HPC 伺服器
- **3706 神達** (Computer Hardware) — 伺服器設計/製造；[[Intel]] Xeon 6、[[AMD]] EPYC 平台，[[NVIDIA]] H100/B200 AI 伺服器
- **3693 營邦** (Computer Hardware) — 伺服器與儲存系統方案 (Barebone/ODM)；[[AMD]]、[[Intel]] 伺服器平台
- **6245 立端** (Communication Equipment) — 高階 x86 網路安全設備/白牌伺服器；[[Intel]]、[[AMD]]、[[NVIDIA]] CPU/GPU 平台
- **6933 AMAX-KY** (Computer Hardware) — AI/HPC 伺服器系統整合；[[AMD]]、[[Intel]] 伺服器 CPU、[[NVIDIA]] [[HBM]] GPU

## J. 通路代理 Distribution (2)

- **3709 鑫聯大投控** (Electronics & Computer Distribution) — 3C 零組件代理經銷；子公司捷元以 [[Intel]]、[[AMD]] CPU/主機板為核心產品線
- **3033 威健** (Electronics & Computer Distribution) — 半導體零組件代理；[[AMD]]、[[Infineon]] 為主力代理線，涵蓋 CPU/[[MCU]]/功率半導體

---

## 供應鏈全景圖

```
┌─────────────────────────────────────────────────────────────────┐
│               CPU 架構設計 (全球)                                │
│  x86: Intel / AMD    Arm: Qualcomm / Apple / 聯發科            │
│  RISC-V: 晶心科 / SiFive                                       │
└────────────────────────┬────────────────────────────────────────┘
                         │ RTL → GDSII
           ┌─────────────┼──────────────┐
           │             │              │
   ┌───────▼──────┐ ┌───▼────────┐ ┌───▼──────────┐
   │ ASIC 設計服務 │ │ SoC 設計    │ │ CPU IP 授權   │
   │ 世芯/創意    │ │ 聯發科      │ │ 晶心科(RISC-V)│
   │ 安國(Arm)    │ │             │ │ 智原(Arm IP)  │
   └───────┬──────┘ └───┬────────┘ └──────────────┘
           │             │
   ┌───────▼─────────────▼──────┐
   │      晶圓代工 Foundry       │
   │  台積電 (3nm/5nm/CoWoS)    │
   │  聯電 (周邊晶片)           │
   └─────────────┬──────────────┘
                 │
   ┌─────────────┼──────────────────────┐
   │             │                      │
┌──▼──────┐ ┌───▼──────────┐ ┌─────────▼────────┐
│ 測試     │ │ 封裝 & 基板   │ │ 基板上游材料      │
│ 精測     │ │ 日月光(封測)  │ │ 南亞(CCL/玻纖布) │
│ 旺矽    │ │ 欣興(ABF #1)  │ │ 聯茂(高頻CCL)    │
│ 穎崴    │ │ 南電(ABF #3)  │ └──────────────────┘
└─────────┘ │ 景碩(FC基板)  │
            └───────┬──────┘
                    │
   ┌────────────────┼───────────────────┐
   │                │                   │
┌──▼──────────┐ ┌───▼────────┐ ┌────────▼───────┐
│ CPU Socket   │ │ 散熱方案    │ │ BIOS 韌體      │
│ 嘉澤(#3)    │ │ 奇鋐(AVC)  │ │ 系微(UEFI)     │
│ 昇貿(焊材)  │ │ 健策(VC)   │ └────────────────┘
└─────────────┘ │ 雙鴻(液冷) │
                │ 艾姆勒     │
                └─────┬──────┘
                      │
   ┌──────────────────▼──────────────────┐
   │          系統組裝 System Assembly     │
   ├──────────────────────────────────────┤
   │ 主機板: 技嘉 / 微星 / 華擎          │
   │ 伺服器ODM: 廣達 / 緯創 / 緯穎       │
   │ AI/HPC: 神達 / 營邦 / AMAX / 立端   │
   │ 通路: 鑫聯大(捷元) / 威健           │
   └──────────────────────────────────────┘
```

## 台灣 CPU 供應鏈關鍵卡位

| 環節 | 全球地位 | 台灣代表 |
|------|----------|----------|
| 晶圓代工 | 全球 60%+ | 台積電 (3nm 獨家) |
| ABF 載板 | 全球前三佔三席 | 欣興 (#1)、南電 (#3)、景碩 |
| CPU Socket | 全球前三 | 嘉澤 (Intel/AMD 共同開發) |
| 封裝測試 | 全球最大 OSAT | 日月光投控 |
| 探針卡 | 全球前三 | 精測 (MEMS)、穎崴 (測試座#1) |
| AI 伺服器散熱 | 全球龍頭 | 奇鋐 (AVC)、健策 (VC) |
| UEFI BIOS | 全球領導 | 系微 |
| 伺服器 ODM | 全球 90%+ 產能 | 廣達/緯創/緯穎/英業達 |
| RISC-V CPU IP | 全球第五 | 晶心科 |
