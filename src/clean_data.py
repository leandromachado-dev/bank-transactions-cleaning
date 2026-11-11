import pandas as pd

# Read everything as text so we control each conversion
df = pd.read_csv("data/raw/transactions_raw.csv", dtype=str)

# Remove "$" and spaces, then convert to numbers
df["amount"] = df["amount"].str.replace("$", "", regex=False).str.strip()
df["amount"] = pd.to_numeric(df["amount"])

print(df["amount"].dtype)
print(df["amount"].describe())

# 2. date: try each known format, fill the gaps with the next one
formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%b-%y"]
parsed = pd.to_datetime(df["date"], format=formats[0], errors="coerce")
for fmt in formats[1:]:
    parsed = parsed.fillna(pd.to_datetime(df["date"], format=fmt, errors="coerce"))
df["date"] = parsed

print("\nDates that failed to parse:", df["date"].isna().sum())
print(df["date"].min(), "->", df["date"].max())