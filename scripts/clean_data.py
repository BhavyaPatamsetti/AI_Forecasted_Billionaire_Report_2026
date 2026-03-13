import pandas as pd
import os

base = os.path.expanduser("~/Desktop/BillionaireDashboard/data/")
print("=== Phase 3: Data Cleaning & Transformation ===\n")

# ── 1. CLEAN BILLIONAIRES DATA ─────────────────────────────────────
print("🧹 Cleaning billionaires data...")

df = pd.read_csv(base + "billionaires_clean.csv")

# Remove any rows where name or net worth is missing
df = df.dropna(subset=["Name", "Net_Worth_USD_Billions"])

# Fill missing age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean()).round(0).astype(int)

# Clean up Self_Made column → Yes/No
df["Self_Made"] = df["Self_Made"].map({True: "Yes", False: "No"}).fillna("Unknown")

# Add Wealth_Category column based on net worth
def wealth_category(worth):
    if worth >= 100:
        return "Mega Billionaire (100B+)"
    elif worth >= 50:
        return "Ultra Billionaire (50-100B)"
    else:
        return "Billionaire (10-50B)"

df["Wealth_Category"] = df["Net_Worth_USD_Billions"].apply(wealth_category)

# Add Wealth_Per_Second column (how much they earn per second)
df["Wealth_Per_Second_USD"] = (
    (df["Net_Worth_USD_Billions"] * 1e9) / (365 * 24 * 60 * 60)
).round(2)

print(df[["Name", "Net_Worth_USD_Billions", "Wealth_Category", "Wealth_Per_Second_USD"]].to_string())
df.to_csv(base + "billionaires_final.csv", index=False)
print("💾 Saved → billionaires_final.csv\n")


# ── 2. CLEAN WORLD PROBLEMS DATA ──────────────────────────────────
print("🧹 Cleaning world problems data...")

wp = pd.read_csv(base + "world_problems.csv")

# Add Affordability columns — what % of top billionaire wealth solves it
top_wealth = df["Net_Worth_USD_Billions"].max()
wp["Top_Billionaire_Can_Afford_Pct"] = (
    (top_wealth / wp["Total_Cost_USD_Billions"]) * 100
).round(2)

# Add a label
def can_afford(pct):
    if pct >= 100:
        return "✅ Can Afford"
    elif pct >= 50:
        return "⚠️ Almost"
    else:
        return "❌ Cannot Afford"

wp["Affordability_Label"] = wp["Top_Billionaire_Can_Afford_Pct"].apply(can_afford)

# Add cost per person
wp["Cost_Per_Person_USD"] = (
    (wp["Total_Cost_USD_Billions"] * 1e9) / (wp["People_Affected_Millions"] * 1e6)
).round(2)

print(wp[["Problem_Name", "Total_Cost_USD_Billions", "Top_Billionaire_Can_Afford_Pct", "Affordability_Label"]].to_string())
wp.to_csv(base + "world_problems_final.csv", index=False)
print("💾 Saved → world_problems_final.csv\n")


# ── 3. CLEAN ECONOMIC INDICATORS ──────────────────────────────────
print("🧹 Cleaning economic indicators...")

eco = pd.read_csv(base + "economic_indicators.csv")

# Convert Date to proper datetime
eco["Date"] = pd.to_datetime(eco["Date"])

# Add Year and Month columns for Power BI time intelligence
eco["Year"] = eco["Date"].dt.year
eco["Month"] = eco["Date"].dt.month
eco["Month_Name"] = eco["Date"].dt.strftime("%B")

# Round values
eco["Value"] = eco["Value"].round(2)

print(eco.to_string())
eco.to_csv(base + "economic_indicators_final.csv", index=False)
print("💾 Saved → economic_indicators_final.csv\n")


# ── 4. CLEAN GDP DATA ─────────────────────────────────────────────
print("🧹 Cleaning GDP data...")

gdp = pd.read_csv(base + "gdp_data.csv")

# Add GDP category
def gdp_category(gdp_val):
    if gdp_val >= 10:
        return "Major Economy (10T+)"
    elif gdp_val >= 3:
        return "Large Economy (3-10T)"
    else:
        return "Medium Economy (<3T)"

gdp["GDP_Category"] = gdp["GDP_USD_Trillions"].apply(gdp_category)

print(gdp.to_string())
gdp.to_csv(base + "gdp_final.csv", index=False)
print("💾 Saved → gdp_final.csv\n")


# ── 5. CREATE DATE DIMENSION TABLE ────────────────────────────────
print("🧹 Creating Date dimension table...")

dates = pd.date_range(start="2018-01-01", end="2026-12-31", freq="MS")
date_df = pd.DataFrame({
    "Date": dates,
    "Year": dates.year,
    "Quarter": dates.quarter,
    "Month_Number": dates.month,
    "Month_Name": dates.strftime("%B"),
    "Quarter_Label": "Q" + dates.quarter.astype(str) + " " + dates.year.astype(str),
})

date_df.to_csv(base + "date_dimension.csv", index=False)
print(f"💾 Saved → date_dimension.csv ({len(date_df)} rows)\n")


# ── FINAL SUMMARY ─────────────────────────────────────────────────
print("=" * 50)
print("✅ Phase 3 Complete! Files ready for Power BI:")
print("   → billionaires_final.csv")
print("   → world_problems_final.csv")
print("   → economic_indicators_final.csv")
print("   → gdp_final.csv")
print("   → date_dimension.csv")
print("=" * 50)