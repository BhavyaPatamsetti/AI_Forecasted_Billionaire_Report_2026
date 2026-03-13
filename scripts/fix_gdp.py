import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

gdp = pd.read_csv(base + "gdp_final.csv")

# Add a unique key combining country + year
gdp["Country_Year"] = gdp["Country_Code"] + "_" + gdp["Year"].astype(str)

gdp.to_csv(base + "gdp_final.csv", index=False)
print("✅ Fixed! gdp_final.csv updated with Country_Year key")
print(gdp[["Country", "Year", "Country_Year"]].to_string())
