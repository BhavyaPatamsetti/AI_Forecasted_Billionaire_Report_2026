import pandas as pd
import numpy as np
from prophet import Prophet
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")

WORLD_PROBLEMS = {
    'Eradicate Malaria': 100,
    'End World Hunger': 200,
    'Universal Education': 390,
    'Clean Water For All': 1140,
    'Universal Healthcare': 3710,
    'Stop Climate Change': 50000,
}
TOTAL_COST = 55540

# All 20 billionaires with country and industry
billionaires = {
    'Elon Musk':                  {'wealth': [20,25,30,220,180,200,250,834], 'country': 'United States', 'industry': 'Technology'},
    'Larry Page':                 {'wealth': [50,55,60,70,80,111,150,251],   'country': 'United States', 'industry': 'Technology'},
    'Sergey Brin':                {'wealth': [45,50,55,65,75,100,140,231],   'country': 'United States', 'industry': 'Technology'},
    'Jeff Bezos':                 {'wealth': [110,115,120,130,140,150,170,223], 'country': 'United States', 'industry': 'Technology'},
    'Mark Zuckerberg':            {'wealth': [55,60,65,70,80,90,130,219],    'country': 'United States', 'industry': 'Technology'},
    'Larry Ellison':              {'wealth': [55,58,60,65,70,80,110,203],    'country': 'United States', 'industry': 'Technology'},
    'Jensen Huang':               {'wealth': [3,4,5,10,20,40,80,159],        'country': 'United States', 'industry': 'Technology'},
    'Bernard Arnault & family':   {'wealth': [70,80,90,150,160,170,165,153], 'country': 'France',        'industry': 'Luxury Goods'},
    'Warren Buffett':             {'wealth': [80,85,88,100,105,110,120,145], 'country': 'United States', 'industry': 'Finance'},
    'Michael Dell':               {'wealth': [30,35,40,50,60,80,100,144],    'country': 'United States', 'industry': 'Technology'},
    'Rob Walton & family':        {'wealth': [45,50,55,65,75,85,100,144],    'country': 'United States', 'industry': 'Retail'},
    'Jim Walton & family':        {'wealth': [43,48,53,63,73,83,98,141],     'country': 'United States', 'industry': 'Retail'},
    'Amancio Ortega':             {'wealth': [60,65,70,80,85,90,100,136],    'country': 'Spain',         'industry': 'Retail'},
    'Alice Walton':               {'wealth': [40,45,50,60,70,80,95,132],     'country': 'United States', 'industry': 'Retail'},
    'Steve Ballmer':              {'wealth': [35,40,45,55,65,80,100,129],    'country': 'United States', 'industry': 'Technology'},
    'Carlos Slim Helu & family':  {'wealth': [55,58,60,65,70,80,90,115],     'country': 'Mexico',        'industry': 'Telecom'},
    'Changpeng Zhao':             {'wealth': [0,0,1,10,15,30,50,111],        'country': 'Canada',        'industry': 'Crypto'},
    'Michael Bloomberg':          {'wealth': [45,48,50,55,60,70,80,109],     'country': 'United States', 'industry': 'Finance'},
    'Bill Gates':                 {'wealth': [90,95,98,105,100,103,104,105], 'country': 'United States', 'industry': 'Technology'},
    'Mukesh Ambani':              {'wealth': [40,45,50,60,70,80,85,98],      'country': 'India',         'industry': 'Energy'},
}

years = [2018,2019,2020,2021,2022,2023,2024,2025]
results = []

for name, info in billionaires.items():
    df = pd.DataFrame({
        'ds': pd.to_datetime([f'{y}-01-01' for y in years]),
        'y': info['wealth']
    })
    
    model = Prophet(yearly_seasonality=False, weekly_seasonality=False,
                   daily_seasonality=False, changepoint_prior_scale=0.5)
    model.fit(df)
    future = model.make_future_dataframe(periods=4, freq='YE')
    forecast = model.predict(future)
    
    for _, row in forecast.iterrows():
        year = row['ds'].year
        predicted = round(max(0, row['yhat']), 2)
        pct = round((predicted / TOTAL_COST) * 100, 1)
        
        # Which specific problems can they solve?
        can_solve = [p for p, cost in WORLD_PROBLEMS.items() if predicted >= cost]
        cannot_solve = [p for p, cost in WORLD_PROBLEMS.items() if predicted < cost]
        
        results.append({
            'Name': name,
            'Country': info['country'],
            'Industry': info['industry'],
            'Year': year,
            'Predicted_Wealth_Billions': predicted,
            'Lower_Bound': round(max(0, row['yhat_lower']), 2),
            'Upper_Bound': round(max(0, row['yhat_upper']), 2),
            'Type': 'Historical' if year <= 2025 else 'Future Forecast',
            'Pct_Of_World_Problems': pct,
            'Problems_Can_Solve': ', '.join(can_solve) if can_solve else 'None yet',
            'Problems_Cannot_Solve': ', '.join(cannot_solve) if cannot_solve else 'All solved!',
            'Num_Problems_Solved': len(can_solve),
            'World_Problems_Total_Cost': TOTAL_COST,
            'GDP_Impact_Billions': round(predicted * 0.15, 2),
        })

df_final = pd.DataFrame(results)
df_final.to_csv(base + "wealth_forecast.csv", index=False)

print("✅ Enriched forecast saved!")
print("\n=== FUTURE FORECASTS ===")
future = df_final[df_final['Type'] == 'Future Forecast']
print(future[['Name','Year','Predicted_Wealth_Billions','Problems_Can_Solve','Num_Problems_Solved']].to_string())
