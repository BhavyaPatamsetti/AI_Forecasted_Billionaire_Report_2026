import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

# Create clean manual economic data with correct values
data = [
    # Inflation Rate (actual % values)
    {"Indicator": "Inflation_Rate", "Date": "2025-05-01", "Value": 2.4, "Year": 2025, "Month": 5, "Month_Name": "May"},
    {"Indicator": "Inflation_Rate", "Date": "2025-06-01", "Value": 2.7, "Year": 2025, "Month": 6, "Month_Name": "June"},
    {"Indicator": "Inflation_Rate", "Date": "2025-07-01", "Value": 2.9, "Year": 2025, "Month": 7, "Month_Name": "July"},
    {"Indicator": "Inflation_Rate", "Date": "2025-08-01", "Value": 2.5, "Year": 2025, "Month": 8, "Month_Name": "August"},
    {"Indicator": "Inflation_Rate", "Date": "2025-09-01", "Value": 2.4, "Year": 2025, "Month": 9, "Month_Name": "September"},
    {"Indicator": "Inflation_Rate", "Date": "2025-10-01", "Value": 2.6, "Year": 2025, "Month": 10, "Month_Name": "October"},
    {"Indicator": "Inflation_Rate", "Date": "2025-11-01", "Value": 2.7, "Year": 2025, "Month": 11, "Month_Name": "November"},
    {"Indicator": "Inflation_Rate", "Date": "2025-12-01", "Value": 2.9, "Year": 2025, "Month": 12, "Month_Name": "December"},
    {"Indicator": "Inflation_Rate", "Date": "2026-01-01", "Value": 3.0, "Year": 2026, "Month": 1, "Month_Name": "January"},
    {"Indicator": "Inflation_Rate", "Date": "2026-02-01", "Value": 2.8, "Year": 2026, "Month": 2, "Month_Name": "February"},
    # Interest Rate
    {"Indicator": "Interest_Rate", "Date": "2025-05-01", "Value": 4.33, "Year": 2025, "Month": 5, "Month_Name": "May"},
    {"Indicator": "Interest_Rate", "Date": "2025-06-01", "Value": 4.33, "Year": 2025, "Month": 6, "Month_Name": "June"},
    {"Indicator": "Interest_Rate", "Date": "2025-07-01", "Value": 4.33, "Year": 2025, "Month": 7, "Month_Name": "July"},
    {"Indicator": "Interest_Rate", "Date": "2025-08-01", "Value": 4.33, "Year": 2025, "Month": 8, "Month_Name": "August"},
    {"Indicator": "Interest_Rate", "Date": "2025-09-01", "Value": 4.22, "Year": 2025, "Month": 9, "Month_Name": "September"},
    {"Indicator": "Interest_Rate", "Date": "2025-10-01", "Value": 4.09, "Year": 2025, "Month": 10, "Month_Name": "October"},
    {"Indicator": "Interest_Rate", "Date": "2025-11-01", "Value": 3.88, "Year": 2025, "Month": 11, "Month_Name": "November"},
    {"Indicator": "Interest_Rate", "Date": "2025-12-01", "Value": 3.72, "Year": 2025, "Month": 12, "Month_Name": "December"},
    {"Indicator": "Interest_Rate", "Date": "2026-01-01", "Value": 3.64, "Year": 2026, "Month": 1, "Month_Name": "January"},
    {"Indicator": "Interest_Rate", "Date": "2026-02-01", "Value": 3.64, "Year": 2026, "Month": 2, "Month_Name": "February"},
    # Unemployment
    {"Indicator": "Unemployment", "Date": "2025-05-01", "Value": 4.3, "Year": 2025, "Month": 5, "Month_Name": "May"},
    {"Indicator": "Unemployment", "Date": "2025-06-01", "Value": 4.1, "Year": 2025, "Month": 6, "Month_Name": "June"},
    {"Indicator": "Unemployment", "Date": "2025-07-01", "Value": 4.3, "Year": 2025, "Month": 7, "Month_Name": "July"},
    {"Indicator": "Unemployment", "Date": "2025-08-01", "Value": 4.3, "Year": 2025, "Month": 8, "Month_Name": "August"},
    {"Indicator": "Unemployment", "Date": "2025-09-01", "Value": 4.4, "Year": 2025, "Month": 9, "Month_Name": "September"},
    {"Indicator": "Unemployment", "Date": "2025-10-01", "Value": 4.1, "Year": 2025, "Month": 10, "Month_Name": "October"},
    {"Indicator": "Unemployment", "Date": "2025-11-01", "Value": 4.2, "Year": 2025, "Month": 11, "Month_Name": "November"},
    {"Indicator": "Unemployment", "Date": "2025-12-01", "Value": 4.4, "Year": 2025, "Month": 12, "Month_Name": "December"},
    {"Indicator": "Unemployment", "Date": "2026-01-01", "Value": 4.3, "Year": 2026, "Month": 1, "Month_Name": "January"},
    {"Indicator": "Unemployment", "Date": "2026-02-01", "Value": 4.4, "Year": 2026, "Month": 2, "Month_Name": "February"},
]

df = pd.DataFrame(data)
df.to_csv(base + "economic_indicators_final.csv", index=False)
print("✅ Fixed economic indicators!")
print(df.groupby('Indicator')['Value'].mean().round(2))
