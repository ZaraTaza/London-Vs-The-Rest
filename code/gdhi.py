# 1. Import libraries
import pandas as pd

# 2. Data Validation/Cleaning
# Loading data 
df_gdhi = pd.read_excel(
    "regionalgrossdisposablehouseholdincomeallitlregions2023.xlsx",
    sheet_name="Table 3",
    skiprows=1
)

print(df_gdhi.columns.tolist())
print(df_gdhi.head())

# Loading regions
df_gdhi_itl1 = df_gdhi[df_gdhi["ITL"] == "ITL1"]
print(df_gdhi_itl1.shape)
print(df_gdhi_itl1["Region name"].tolist())

# Checking data types
year_columns = [str(year) for year in range(1997, 2024)]
df_gdhi_itl1[year_columns] = df_gdhi_itl1[year_columns].apply(pd.to_numeric, errors="coerce")
df_gdhi_itl1.dtypes
df_gdhi_itl1.isna().sum()

years_columns_gdhi = [str(year) for year in range(1997, 2024)]
df_gdhi_itl1[years_columns_gdhi] = df_gdhi_itl1[years_columns_gdhi].apply(pd.to_numeric, errors="coerce")
df_gdhi_itl1.dtypes

# 3. Calculate CAGR 
# London CAGR 
start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == "London"]["2008"]
end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == "London"]["2016"]
years = 8 
cagr = (end / start) ** (1 / years) - 1 
cagr_percent = cagr * 100
print(cagr_percent)

# North East CAGR 
start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == "North East"]["2008"]
end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == "North East"]["2016"]
years = 8 
cagr = (end / start) ** (1 / years) - 1
cagr_percent = cagr * 100
print(cagr_percent)

# All regions CAGR from 2008 - 2016
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2008"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2016"]
    years = 8 
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# All regions CAGR from 2016 - 2019
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2016"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2019"]
    years = 3
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# All regions CAGR from 2019 - 2023
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2019"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2023"]
    years = 4
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)
