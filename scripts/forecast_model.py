import pandas as pd
import numpy as np
from prophet import Prophet
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

# Create historical wealth data for top 5 billionaires
data = {
    'Elon Musk': [20, 25, 30, 220, 180, 200, 250, 834],
    'Larry Page': [50, 55, 60, 70, 80, 111, 150, 251],
    'Jeff Bezos': [110, 115, 120, 130, 140, 150, 170, 223],
    'Mark Zuckerberg': [55, 60, 65, 70, 80, 90, 130, 219],
    'Larry Ellison': [55, 58, 60, 65, 70, 80, 110, 203],
}

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
forecast_results = []

for name, wealth in data.items():
    df = pd.DataFrame({
        'ds': pd.to_datetime([f'{y}-01-01' for y in years]),
        'y': wealth
    })
    
    model = Prophet(yearly_seasonality=False, 
                   weekly_seasonality=False,
                   daily_seasonality=False,
                   changepoint_prior_scale=0.5)
    model.fit(df)
    
    future = model.make_future_dataframe(periods=5, freq='Y')
    forecast = model.predict(future)
    
    for _, row in forecast.iterrows():
        year = row['ds'].year
        if year >= 2025:
            forecast_results.append({
                'Name': name,
                'Year': year,
                'Predicted_Wealth_Billions': round(max(0, row['yhat']), 2),
                'Lower_Bound': round(max(0, row['yhat_lower']), 2),
                'Upper_Bound': round(max(0, row['yhat_upper']), 2),
                'Type': 'Historical' if year <= 2025 else 'Forecast'
            })

df_forecast = pd.DataFrame(forecast_results)
df_forecast.to_csv(base + "wealth_forecast.csv", index=False)
print("✅ Forecast complete!")
print(df_forecast[df_forecast['Type'] == 'Forecast'][['Name', 'Year', 'Predicted_Wealth_Billions']].to_string())
