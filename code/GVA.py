# 1. Install Libraries
import pandas as pd

# 2. Load and Validate Data
df = pd.read_excel (
    "regionalgrossvalueaddedbalancedperheadandincomecomponents.xlsx",
    sheet_name="Table 2",
    skiprows=1
    )

# Checking for Regional Names
df_itl1 = df[df["ITL"] == "ITL1"]
print(df_itl1.shape)
print(df_itl1["Region name"].tolist())

# Checking for Data Types and Missing Values
df_itl1.dtypes
df_itl1.isna().sum()

# Limiting Years from 1998 to 2023 and Convert yearly GVA values to numeric
year_columns = [str(year) for year in range(1998, 2024)]
df_itl1[year_columns] = df_itl1[year_columns].apply(pd.to_numeric, errors="coerce")

# Checking for Regions of 2008 and 2023
print(df_itl1[["Region name", "2008", "2023"]])

# 3. Calculating GVA per head in each region
df_indexed = df_itl1[year_columns].div(df_itl1["2008"], axis=0) * 100

df_indexed["Region name"] = df_itl1["Region name"]
print(df_indexed.head())

# 4. Calculate CAGR across Regions
regions = df_itl1["Region name"].tolist()

"""
To calculate CAGR:
start = starting value
end = ending value
years = number of years between (e.g. 2021-2023 - 2 years in between)

CAGR as a percentage = return ((end / start) ** (1 / years) - 1) * 100
"""

# 2008 - 2016
for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2008"]
    end = df_itl1[df_itl1["Region name"] == region]["2016"]
    years = 8
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# 2016 - 2019 
for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2016"]
    end = df_itl1[df_itl1["Region name"] == region]["2019"]
    years = 3
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# 2019 - 2023
for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2019"]
    end = df_itl1[df_itl1["Region name"] == region]["2023"]
    years = 4
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

# 5. Visualisations 
# Plot whole dataset from 1998 to 2023
import matplotlib.pyplot as plt 

df_plot = df_indexed.set_index("Region name")[year_columns].T
df_plot.plot(figsize=(12, 7))
plt.title("Regional GVA per head, indexed to 2008 = 100")
plt.xlabel("Year")
plt.ylabel("Index (2008 = 100)")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()

# Trimming the dataset years to 2008 to 2023
years_columns_gva_trimmed = [str(year) for year in range(2008, 2024)]
df_gva_plot_trimmed = df_indexed.set_index("Region name")[years_columns_gva_trimmed].T
df_gva_plot_trimmed.plot(figsize=(12, 7)) 
plt.title("Regional GVA per head, indexed 2008 = 100") 
plt.xlabel("Years") 
plt.ylabel("Indexed GVA") 
plt.legend(loc="upper left", bbox_to_anchor=(1, 1)) 
plt.show()
