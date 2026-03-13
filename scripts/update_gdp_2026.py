import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

# Load existing historical data
df_old = pd.read_csv(base + "gdp_historical.csv")

# Add 2025 and 2026 IMF estimates
new_data = [
    {"Country": "United States", "Country_Code": "USA", "GDP_USD_Trillions": 29.92, "Year": 2025, "GDP_Category": "Major Economy (10T+)"},
    {"Country": "United States", "Country_Code": "USA", "GDP_USD_Trillions": 31.22, "Year": 2026, "GDP_Category": "Major Economy (10T+)"},
    {"Country": "China", "Country_Code": "CHN", "GDP_USD_Trillions": 19.53, "Year": 2025, "GDP_Category": "Major Economy (10T+)"},
    {"Country": "China", "Country_Code": "CHN", "GDP_USD_Trillions": 20.43, "Year": 2026, "GDP_Category": "Major Economy (10T+)"},
    {"Country": "Germany", "Country_Code": "DEU", "GDP_USD_Trillions": 4.75, "Year": 2025, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "Germany", "Country_Code": "DEU", "GDP_USD_Trillions": 4.89, "Year": 2026, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "India", "Country_Code": "IND", "GDP_USD_Trillions": 4.19, "Year": 2025, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "India", "Country_Code": "IND", "GDP_USD_Trillions": 4.52, "Year": 2026, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "United Kingdom", "Country_Code": "GBR", "GDP_USD_Trillions": 3.81, "Year": 2025, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "United Kingdom", "Country_Code": "GBR", "GDP_USD_Trillions": 3.95, "Year": 2026, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "France", "Country_Code": "FRA", "GDP_USD_Trillions": 3.27, "Year": 2025, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "France", "Country_Code": "FRA", "GDP_USD_Trillions": 3.39, "Year": 2026, "GDP_Category": "Large Economy (3-10T)"},
    {"Country": "Mexico", "Country_Code": "MEX", "GDP_USD_Trillions": 1.92, "Year": 2025, "GDP_Category": "Medium Economy (<3T)"},
    {"Country": "Mexico", "Country_Code": "MEX", "GDP_USD_Trillions": 1.98, "Year": 2026, "GDP_Category": "Medium Economy (<3T)"},
    {"Country": "Australia", "Country_Code": "AUS", "GDP_USD_Trillions": 1.81, "Year": 2025, "GDP_Category": "Medium Economy (<3T)"},
    {"Country": "Australia", "Country_Code": "AUS", "GDP_USD_Trillions": 1.87, "Year": 2026, "GDP_Category": "Medium Economy (<3T)"},
]

df_new = pd.DataFrame(new_data)
df_final = pd.concat([df_old, df_new])
df_final = df_final.sort_values(['Country', 'Year'])
df_final.to_csv(base + "gdp_historical.csv", index=False)

print("✅ GDP data updated to 2026!")
print(f"Total rows: {len(df_final)}")
print(df_final[df_final['Year'] >= 2025][['Country', 'Year', 'GDP_USD_Trillions']].to_string())
