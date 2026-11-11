import random
from datetime import date, timedelta

import pandas as pd

random.seed(42)

MERCHANTS = {
    "Food": ["STARBUCKS #1234 SAN DIEGO CA", "starbucks store 5521", "SBUX*COFFEE",
             "CHIPOTLE 1842", "Chipotle Mexican Grill"],
    "Transport": ["UBER *TRIP", "Uber Technologies", "SHELL OIL 5744", "Shell Station"],
    "Subscriptions": ["NETFLIX.COM", "Netflix Inc", "SPOTIFY USA", "Spotify P0A1B2"],
    "Shopping": ["WALMART #2301", "WAL-MART SUPERCENTER", "AMAZON MKTPLACE PMTS", "Amazon.com*2K4"],
}
DATE_FORMATS = ["%m/%d/%Y", "%Y-%m-%d", "%d-%b-%y"]

rows = []
for _ in range(500):
    category = random.choice(list(MERCHANTS))
    description = random.choice(MERCHANTS[category])
    day = date(2026, 1, 1) + timedelta(days=random.randint(0, 300))
    amount = round(random.uniform(3, 150), 2)
    rows.append({
        "date": day.strftime(random.choice(DATE_FORMATS)),  # formatos misturados
        "description": description,                          # nomes inconsistentes
        "amount": random.choice([f"${amount}", str(amount), f" {amount} "]),  # texto, não número
        "category": category,                                # "gabarito" para o passo de AI
    })

df = pd.DataFrame(rows)
duplicates = df.sample(25, random_state=1)                   # 25 linhas duplicadas de propósito
df = pd.concat([df, duplicates], ignore_index=True)
df = df.sample(frac=1, random_state=2).reset_index(drop=True)  # embaralha
df.to_csv("data/raw/transactions_raw.csv", index=False)
print(f"Saved {len(df)} rows")