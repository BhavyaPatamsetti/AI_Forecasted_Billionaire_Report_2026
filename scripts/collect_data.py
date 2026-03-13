import pandas as pd
import requests
import os

print("=== Billionaire Dashboard - Data Collection ===")

# ── 1. LOAD BILLIONAIRES DATA ──────────────────────────────────────
print("\n📊 Loading billionaires dataset...")

df = pd.read_csv(os.path.expanduser(
    "~/Desktop/BillionaireDashboard/data/Billionaires Statistics Dataset.csv"
))

# Keep only the columns we need
billionaires = df[[
    'personName', 'rank', 'finalWorth', 'category',
    'country', 'age', 'industries', 'selfMade'
]].copy()

# Rename columns to clean names
billionaires.columns = [
    'Name', 'Rank', 'Net_Worth_USD_Billions',
    'Category', 'Country', 'Age', 'Industry', 'Self_Made'
]

# Convert worth from millions to billions
billionaires['Net_Worth_USD_Billions'] = (
    billionaires['Net_Worth_USD_Billions'] / 1000
).round(2)

# Keep top 20
billionaires = billionaires.head(20)

print(f"✅ Loaded {len(billionaires)} billionaires")
print(billionaires[['Name', 'Net_Worth_USD_Billions', 'Country']].to_string())

# Save it
billionaires.to_csv(
    os.path.expanduser("~/Desktop/BillionaireDashboard/data/billionaires_clean.csv"),
    index=False
)
print("\n💾 Saved → data/billionaires_clean.csv")


# ── 2. PULL WORLD BANK DATA ────────────────────────────────────────
print("\n🌍 Pulling GDP data from World Bank API...")

# Countries we care about (where billionaires are from)
countries = "US;CN;FR;DE;IN;GB;MX;AU"
url = f"https://api.worldbank.org/v2/country/{countries}/indicator/NY.GDP.MKTP.CD?format=json&mrv=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    records = []
    for item in data[1]:
        if item['value']:
            records.append({
                'Country': item['country']['value'],
                'Country_Code': item['countryiso3code'],
                'GDP_USD_Trillions': round(item['value'] / 1e12, 2),
                'Year': item['date']
            })

    gdp_df = pd.DataFrame(records)
    print(f"✅ Got GDP data for {len(gdp_df)} countries")
    print(gdp_df.to_string())

    gdp_df.to_csv(
        os.path.expanduser("~/Desktop/BillionaireDashboard/data/gdp_data.csv"),
        index=False
    )
    print("\n💾 Saved → data/gdp_data.csv")
else:
    print("❌ World Bank API call failed — check your internet connection")


print("\n✅ Phase 2 Complete! Check your data folder for 2 new CSV files.")
