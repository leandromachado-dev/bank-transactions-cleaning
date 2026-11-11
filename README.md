# Bank Transactions Cleaning

Cleaning and standardizing messy bank transaction data with Python and pandas.

> **Status:** work in progress. Data generation is done; the cleaning pipeline is next.

## Problem

Transaction exports from banks and card processors are rarely ready to use. The same merchant appears under many names, dates come in different formats, amounts are stored as text, and duplicate rows are common. This project builds a repeatable pipeline that turns that raw data into a clean, analysis-ready dataset.

## The data

Real bank data is private, so this project uses **synthetic transactions** created by `src/generate_data.py`. The script deliberately plants the problems found in real exports:

| Problem | Example |
|---|---|
| Mixed date formats | `03/15/2026`, `2026-03-15`, `15-Mar-26` |
| Amounts stored as text | `$74.81`, ` 70.31 `, `12.5` |
| Inconsistent merchant names | `STARBUCKS #1234 SAN DIEGO CA`, `SBUX*COFFEE` |
| Duplicate rows | 25 repeated transactions |

The raw file has **525 rows** and is saved in `data/raw/transactions_raw.csv`.

## Project structure

```
bank-transactions-cleaning/
├── data/
│   ├── raw/          # original, messy data
│   └── clean/        # cleaned output (coming soon)
├── notebooks/
├── src/
│   └── generate_data.py
├── requirements.txt
└── README.md
```

## How to run

```bash
git clone https://github.com/leandromachado-dev/bank-transactions-cleaning.git
cd bank-transactions-cleaning
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py
```

## Roadmap

- [x] Generate synthetic, messy transaction data
- [ ] Inspect the raw data and document the issues
- [ ] Standardize dates and convert amounts to numbers
- [ ] Normalize merchant names
- [ ] Remove duplicate rows
- [ ] Add before/after results to this README
- [ ] Categorize transactions with machine learning
- [ ] Summary report in Excel

## Tools

Python, pandas, Git/GitHub.