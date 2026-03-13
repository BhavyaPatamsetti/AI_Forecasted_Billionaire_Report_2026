import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

# Copy 2026 data as the main billionaires file
df = pd.read_csv(base + "billionaires_2026.csv")
df.to_csv(base + "billionaires_final.csv", index=False)
print("✅ billionaires_final.csv updated with 2026 data!")
print(df[["Name", "Net_Worth_USD_Billions"]].to_string())
