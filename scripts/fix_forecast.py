import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")
df = pd.read_csv(base + "wealth_forecast.csv")

# Fix Can_Fix_World labels to be more meaningful
def get_label(row):
    pct = row['Pct_Of_World_Problems']
    if pct >= 100:
        return "✅ Can Fix Everything!"
    elif pct >= 50:
        return "🔥 Can Fix Half!"
    elif pct >= 10:
        return "⚠️ Can Fix Some Problems"
    elif pct >= 5:
        return "📈 Making Progress"
    else:
        return "❌ Not Enough Yet"

def get_specific_problems(wealth):
    problems = {
        'Eradicate Malaria': 100,
        'End World Hunger': 200,
        'Universal Education': 390,
        'Clean Water For All': 1140,
        'Universal Healthcare': 3710,
        'Stop Climate Change': 50000,
    }
    can_solve = [p for p, cost in problems.items() if wealth >= cost]
    if not can_solve:
        return "❌ Cannot afford any problem alone"
    return "✅ Can solve: " + ", ".join(can_solve)

df['Can_Fix_World'] = df.apply(get_label, axis=1)
df['Problems_Can_Solve'] = df['Predicted_Wealth_Billions'].apply(get_specific_problems)

df.to_csv(base + "wealth_forecast.csv", index=False)

print("✅ Fixed!")
print("\n=== FUTURE PREDICTIONS 2026-2028 ===")
future = df[df['Type'] == 'Future Forecast 🔮']
print(future[['Name', 'Year', 'Predicted_Wealth_Billions', 'Can_Fix_World', 'Problems_Can_Solve']].to_string())
