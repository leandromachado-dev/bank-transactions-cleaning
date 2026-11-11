import pandas as pd

# Load the cleaned data
df = pd.read_csv("data/clean/transactions_clean.csv", parse_dates=["date"])

# Total spent and number of transactions per merchant
by_merchant = (
    df.groupby("merchant")["amount"]
    .agg(["count", "sum"])
    .round(2)
    .sort_values("sum", ascending=False)
)

# Total spent per month
df["month"] = df["date"].dt.to_period("M").astype(str)
by_month = df.groupby("month")["amount"].sum().round(2)

# Write three sheets into one Excel file
with pd.ExcelWriter("data/clean/summary.xlsx") as writer:
    df.drop(columns="month").to_excel(writer, sheet_name="Clean data", index=False)
    by_merchant.to_excel(writer, sheet_name="By merchant")
    by_month.to_excel(writer, sheet_name="By month")

print("Saved data/clean/summary.xlsx")