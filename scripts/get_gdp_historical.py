import requests
import pandas as pd
import os

print("=== Fetching Historical GDP Data (2018-2024) ===")

countries = "US;CN;FR;DE;IN;GB;MX;AU"
url = f"https://api.worldbank.org/v2/country/{countries}/indicator/NY.GDP.MKTP.CD?format=json&mrv=7&per_page=100"

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
                'Year': int(item['date']),
                'GDP_Category': (
                    "Major Economy (10T+)" if item['value']/1e12 >= 10
                    else "Large Economy (3-10T)" if item['value']/1e12 >= 3
                    else "Medium Economy (<3T)"
                )
            })

    df = pd.DataFrame(records)
    df = df.sort_values(['Country', 'Year'])
    print(f"✅ Got {len(df)} rows!")
    print(df.to_string())

    base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")
    df.to_csv(base + "gdp_historical.csv", index=False)
    print("\n💾 Saved → gdp_historical.csv")
else:
    print(f"❌ Failed — status: {response.status_code}")
