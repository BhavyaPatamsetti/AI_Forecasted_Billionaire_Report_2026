import requests
import pandas as pd
import os

print("=== Pulling FRED Economic Data ===")

API_KEY = "655c539b4efc5592efe36746ba439f5b"

indicators = {
    "Inflation_Rate": f"https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={API_KEY}&file_type=json&limit=10&sort_order=desc",
    "Interest_Rate": f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key={API_KEY}&file_type=json&limit=10&sort_order=desc",
    "Unemployment": f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={API_KEY}&file_type=json&limit=10&sort_order=desc",
}

records = []
for name, url in indicators.items():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("observations", [])
        for obs in data:
            if obs["value"] != ".":
                records.append({
                    "Indicator": name,
                    "Date": obs["date"],
                    "Value": float(obs["value"])
                })
        print(f"✅ Got {name} data")
    else:
        print(f"❌ Failed — status: {response.status_code}")

if records:
    df = pd.DataFrame(records)
    print(df.to_string())
    df.to_csv(
        os.path.expanduser("~/Desktop/BillionaireDashboard/data/economic_indicators.csv"),
        index=False
    )
    print("💾 Saved → data/economic_indicators.csv")
else:
    print("❌ No data fetched")

print("✅ Done!")