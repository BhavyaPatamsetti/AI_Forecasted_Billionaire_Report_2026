import pandas as pd
import numpy as np
from prophet import Prophet
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

WORLD_PROBLEMS_COST = 55540

# Historical wealth data for all 20 billionaires (2018-2025)
data = {
    'Elon Musk':                  [20,  25,  30,  220, 180, 200, 250, 834],
    'Larry Page':                 [50,  55,  60,  70,  80,  111, 150, 251],
    'Sergey Brin':                [45,  50,  55,  65,  75,  100, 140, 231],
    'Jeff Bezos':                 [110, 115, 120, 130, 140, 150, 170, 223],
    'Mark Zuckerberg':            [55,  60,  65,  70,  80,  90,  130, 219],
    'Larry Ellison':              [55,  58,  60,  65,  70,  80,  110, 203],
    'Jensen Huang':               [3,   4,   5,   10,  20,  40,  80,  159],
    'Bernard Arnault & family':   [70,  80,  90,  150, 160, 170, 165, 153],
    'Warren Buffett':             [80,  85,  88,  100, 105, 110, 120, 145],
    'Michael Dell':               [30,  35,  40,  50,  60,  80,  100, 144],
    'Rob Walton & family':        [45,  50,  55,  65,  75,  85,  100, 144],
    'Jim Walton & family':        [43,  48,  53,  63,  73,  83,  98,  141],
    'Amancio Ortega':             [60,  65,  70,  80,  85,  90,  100, 136],
    'Alice Walton':               [40,  45,  50,  60,  70,  80,  95,  132],
    'Steve Ballmer':              [35,  40,  45,  55,  65,  80,  100, 129],
    'Carlos Slim Helu & family':  [55,  58,  60,  65,  70,  80,  90,  115],
    'Changpeng Zhao':             [0,   0,   1,   10,  15,  30,  50,  111],
    'Michael Bloomberg':          [45,  48,  50,  55,  60,  70,  80,  109],
    'Bill Gates':                 [90,  95,  98,  105, 100, 103, 104, 105],
    'Mukesh Ambani':              [40,  45,  50,  60,  70,  80,  85,  98],
}

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
forecast_results = []

for name, wealth in data.items():
    df = pd.DataFrame({
        'ds': pd.to_datetime([f'{y}-01-01' for y in years]),
        'y': wealth
    })
    
    model = Prophet(
        yearly_seasonality=False,
        weekly_seasonality=False,
        daily_seasonality=False,
        changepoint_prior_scale=0.5
    )
    model.fit(df)
    
    future = model.make_future_dataframe(periods=4, freq='YE')
    forecast = model.predict(future)
    
    for _, row in forecast.iterrows():
        year = row['ds'].year
        predicted = round(max(0, row['yhat']), 2)
        pct = round((predicted / WORLD_PROBLEMS_COST) * 100, 1)
        
        if year == 2024: can_fix = "❌ Not Even Close" if pct < 10 else "⚠️ Getting There" if pct < 50 else "⚠️ Almost" if pct < 100 else "✅ Can Fix World!"
        else: can_fix = "❌ Not Even Close" if pct < 10 else "⚠️ Getting There" if pct < 50 else "⚠️ Almost" if pct < 100 else "✅ Can Fix World!"

        forecast_results.append({
            'Name': name,
            'Year': year,
            'Predicted_Wealth_Billions': predicted,
            'Lower_Bound': round(max(0, row['yhat_lower']), 2),
            'Upper_Bound': round(max(0, row['yhat_upper']), 2),
            'Type': 'Historical' if year <= 2025 else 'Future Forecast 🔮',
            'Can_Fix_World': can_fix,
            'Pct_Of_World_Problems': pct,
            'World_Problems_Cost_Billions': WORLD_PROBLEMS_COST
        })

df_forecast = pd.DataFrame(forecast_results)
df_forecast.to_csv(base + "wealth_forecast.csv", index=False)

print("✅ Forecast complete for all 20 billionaires!")
print("\n=== FUTURE PREDICTIONS 2026-2028 ===")
future = df_forecast[df_forecast['Type'] == 'Future Forecast 🔮']
print(future[['Name', 'Year', 'Predicted_Wealth_Billions', 'Can_Fix_World', 'Pct_Of_World_Problems']].to_string())
