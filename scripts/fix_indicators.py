import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")
df = pd.read_csv(base + "economic_indicators_final.csv")

# Convert CPI index to year-over-year inflation percentage
df_inflation = df[df['Indicator'] == 'Inflation_Rate'].copy()
df_inflation = df_inflation.sort_values('Date')
df_inflation['Value'] = df_inflation['Value'].pct_change(12) * 100
df_inflation = df_inflation.dropna()

# Keep Interest Rate and Unemployment as is
df_others = df[df['Indicator'] != 'Inflation_Rate'].copy()

# Combine
df_final = pd.concat([df_inflation, df_others])
df_final['Value'] = df_final['Value'].round(2)
df_final.to_csv(base + "economic_indicators_final.csv", index=False)

print("✅ Fixed!")
print(df_final.groupby('Indicator')['Value'].mean().round(2))
