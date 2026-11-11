import pandas as pd

# Read everything as text so we control each conversion
df = pd.read_csv("data/raw/transactions_raw.csv", dtype=str)

# Remove "$" and spaces, then convert to numbers
df["amount"] = df["amount"].str.replace("$", "", regex=False).str.strip()
df["amount"] = pd.to_numeric(df["amount"])

print(df["amount"].dtype)
print(df["amount"].describe())