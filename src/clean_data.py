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

# 3. merchant: map messy descriptions to one clean name
merchant_rules = {
    "sbux": "Starbucks",
    "starbucks": "Starbucks",
    "chipotle": "Chipotle",
    "uber": "Uber",
    "shell": "Shell",
    "netflix": "Netflix",
    "spotify": "Spotify",
    "wal-mart": "Walmart",
    "walmart": "Walmart",
    "amazon": "Amazon",
}

def clean_merchant(text):
    text = text.lower()
    for keyword, name in merchant_rules.items():
        if keyword in text:
            return name
    return "Unknown"

df["merchant"] = df["description"].apply(clean_merchant)

print("\nUnique merchants:", df["merchant"].nunique())
print(df["merchant"].value_counts())

# 4. Remove duplicate rows (same date, merchant and amount)
before = len(df)
df = df.drop_duplicates(subset=["date", "merchant", "amount"]).reset_index(drop=True)
print(f"\nRows before: {before} | after: {len(df)} | removed: {before - len(df)}")

# 5. Save the cleaned file
df = df[["date", "merchant", "amount", "category", "description"]]
df.to_csv("data/clean/transactions_clean.csv", index=False, date_format="%Y-%m-%d")
print("Saved data/clean/transactions_clean.csv")