import requests
import pandas as pd
import os

print("=== Fetching 2026 Billionaire Data ===")

# Using Forbes API endpoint
url = "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json?limit=20"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    records = []
    for person in data.get("personList", {}).get("personsLists", []):
        records.append({
            "Name": person.get("personName", ""),
            "Rank": person.get("position", ""),
            "Net_Worth_USD_Billions": round(person.get("finalWorth", 0) / 1000, 2),
            "Country": person.get("countryOfCitizenship", ""),
            "Industry": person.get("industries", [""])[0] if person.get("industries") else "",
            "Category": person.get("category", ""),
            "Age": person.get("age", 0),
            "Self_Made": "Yes" if person.get("selfMade") else "No",
            "Wealth_Category": (
                "Mega Billionaire (100B+)" if person.get("finalWorth", 0)/1000 >= 100
                else "Ultra Billionaire (50-100B)" if person.get("finalWorth", 0)/1000 >= 50
                else "Billionaire (10-50B)"
            ),
            "Wealth_Per_Second_USD": round(
                (person.get("finalWorth", 0) / 1000 * 1e9) / (365 * 24 * 60 * 60), 2
            )
        })
    
    df = pd.DataFrame(records)
    print(f"✅ Got {len(df)} billionaires!")
    print(df[["Name", "Net_Worth_USD_Billions", "Country"]].to_string())
    
    base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")
    df.to_csv(base + "billionaires_2026.csv", index=False)
    print("\n💾 Saved → billionaires_2026.csv")
else:
    print(f"❌ Failed — status: {response.status_code}")
    print("Forbes blocked the request — will use manual data instead")
