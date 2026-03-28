# 🛒 E-Commerce Sales Analysis — Portfolio Project

**Author:** Səid Qurbanov  
**Tools Used:** Python (pandas) | Excel | Tableau  
**Dataset:** Online Retail Dataset — 816,019 transactions (2010–2011)  
**Status:** ✅ Completed

---

## 📌 Project Overview

This project performs a full end-to-end analysis of a UK-based e-commerce company's transaction data. The goal was to answer key business questions about revenue, customer behavior, and product performance — using the full data analytics workflow taught in the **Google Data Analytics Certificate**.

---

## 🎯 Business Questions Answered

- Which months generate the highest revenue?
- Which countries contribute the most to total sales?
- Who are the top 10 customers by spending?
- Which products generate the most revenue?

---

## 🗂️ Dataset Description

| Column | Description |
|--------|-------------|
| InvoiceNo | Unique transaction ID (prefix "C" = cancellation) |
| StockCode | Product code |
| Description | Product name |
| Quantity | Number of units sold (negative = return) |
| UnitPrice | Price per unit in £ |
| CustomerID | Unique customer identifier |
| Country | Customer's country |
| Date | Transaction date |
| Hour | Hour of transaction |
| Revenue | Calculated field: Quantity × UnitPrice |

---

## 🔧 Tools & Workflow

### 1️⃣ Excel — Data Preparation
- Added **Revenue column** (Quantity × UnitPrice)
- Identified and flagged negative quantities (returns)
- Reviewed missing CustomerIDs
- Built **PivotTable** and **PivotChart** for monthly revenue

### 2️⃣ Python (pandas) — Data Analysis
- Loaded and cleaned dataset
- Calculated **Total Revenue**, **Monthly Revenue**, **Revenue by Country**, **Top 10 Customers**
- Exported results to separate Excel files

### 3️⃣ Tableau — Data Visualization
- Built interactive **Monthly Revenue line chart**
- Built **Revenue by Country** filled map
- Built **Top 10 Products** horizontal bar chart
- Combined all into a single **interactive dashboard**

---

## 📊 Key Findings

- 🏆 **November 2011** was the highest revenue month — **£221,411**
- 🌍 **United Kingdom** accounts for approximately **82% of total revenue**
- 📦 **REGENCY CAKESTAND** was the best-selling product by revenue
- 👥 Top 10 customers contributed a significant share of total revenue
- 📉 **December 2011** shows incomplete data — revenue appears artificially low
- ⚠️ Returns (negative quantities) account for a notable portion of transactions

---

## 💡 Business Recommendations

1. **Focus marketing on September–November** — peak buying season, likely driven by Christmas shopping
2. **Invest in international expansion** — UK dominates but Europe shows growth potential
3. **Retain top customers** — top 10 customers are disproportionately valuable
4. **Investigate December data** — incomplete month may be skewing annual totals
5. **Reduce return rates** — analyse which products are returned most frequently

---

## 📁 Project Files

```
ecommerce/
├── index.py                  # Main Python analysis script
├── REVENUE.csv.xlsx          # Cleaned dataset with Revenue column
├── Monthly_Revenue.xlsx      # Monthly revenue results
├── Revenue_by_Country.xlsx   # Revenue by country results
├── Top_Customers.xlsx        # Top 10 customers by spending
├── results.xlsx              # Combined results workbook
└── README.md                 # This file
```

---

## 🚀 How to Run

1. Clone or download this repository
2. Install required libraries:
```bash
pip install pandas openpyxl matplotlib seaborn
```
3. Run the analysis:
```bash
python index.py
```
4. Open Tableau dashboard via the public link below

---

## 📡 Tableau Dashboard

🔗 (https://public.tableau.com/app/profile/s.id.qurbanov/viz/E-CommerceSalesAnalysis2011/E-CommerceSalesAnalysis2011)

---

## 📚 Learning Source

This project was completed as part of the **Google Data Analytics Professional Certificate** on Coursera, applying skills from all course modules including data cleaning, analysis, and visualization.

---

## 👤 About Me

I am a 20-year-old pharmacy student and practicing pharmacist from Ganja, Azerbaijan, currently expanding into data analytics. This project demonstrates my ability to work with real-world datasets using industry-standard tools.

---
https://www.linkedin.com/in/said-gurbanov-4a77763b8/
*Feel free to connect with me on LinkedIn or reach out for collaboration opportunities!*
