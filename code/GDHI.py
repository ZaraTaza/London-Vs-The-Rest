# 1. Import libraries
import pandas as pd

# 2. Load and validate data
df_gdhi = pd.read_excel(
    "regionalgrossdisposablehouseholdincomeallitlregions2023.xlsx",
    sheet_name="Table 3",
    skiprows=1
)

# Load regions
df_gdhi_itl1 = df_gdhi[df_gdhi["ITL"] == "ITL1"]
print(df_gdhi_itl1.shape)
print(df_gdhi_itl1["Region name"].tolist())

# Define time period
year_columns = [str(year) for year in range(1997, 2024)]

# Convert yearly GDHI values to numer
df_gdhi_itl1[year_columns] = df_gdhi_itl1[year_columns].apply(pd.to_numeric, errors="coerce")

# Check data types and missing values
df_gdhi_itl1.dtypes
df_gdhi_itl1.isna().sum()

# 3. Calculate CAGR 
""
To calculate CAGR:
start = starting value
end = ending value
years = number of years between start and end

CAGR % = ((end / start)) ** (1 / years) - 1) * 100 
"""
regions_gdhi = df_gdhi_itl1["Region name"].tolist()

# CAGR from 2008 - 2016
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2008"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2016"]
    years = 8 
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# CAGR from 2016 - 2019
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2016"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2019"]
    years = 3
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# CAGR from 2019 - 2023
regions_ghdhi = df_gdhi_itl1["Region name"].tolist()
for region in regions_ghdhi:
    start = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2019"]
    end = df_gdhi_itl1[df_gdhi_itl1["Region name"] == region]["2023"]
    years = 4
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# 4. Calculate Indexed GDHI
# Define analysis period
years_columns_gdhi = [str(year) for year in range(1997, 2024)]

# Convert yearly GDHI values to numeric
df_gdhi_itl1[years_columns_gdhi] = (
    df_gdhi_itl1[years_columns_gdhi]
    .apply(pd.to_numeric, errors="coerce")
)

df_gdhi_indexed = df_gdhi_itl1[years_columns_gdhi].div(df_gdhi_itl1["2008"], axis=0) * 100

# Add region names
df_gdhi_indexed["Region name"] = df_gdhi_itl1["Region name"]
print(df_gdhi_indexed.head())

# 5. Visualisations 
# Plotted whole dataset from 1997 to 2023
import matplotlib.pyplot as plt
df_gdhi_plot = df_gdhi_indexed.set_index("Region name")[years_columns_gdhi].T
df_gdhi_plot.plot(figsize=(12, 7))
plt.title("Regional GDHI Growth per head, indexed 2008 = 100")
plt.xlabel("Years")
plt.ylabel("Indexed GDHI")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()

# Trimming the dataset years to 2008 to 2023
years_columns_gdhi_trimmed = [str(year) for year in range(2008, 2024)]
df_gdhi_plot_trimmed = df_gdhi_indexed.set_index("Region name")[years_columns_gdhi_trimmed].T
df_gdhi_plot_trimmed.plot(figsize=(12, 7))
plt.title("Regional GDHI per head, indexed 2008 = 100")
plt.xlabel("Years")
plt.ylabel("Indexed GDHI")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()
