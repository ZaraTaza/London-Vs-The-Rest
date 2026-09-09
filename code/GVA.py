# 1. Install Libraries
pip install pandas openpyxl
import pandas as pd

# 2. Data Validation/Cleaning
df = pd.read_excel (
    "regionalgrossvalueaddedbalancedperheadandincomecomponents.xlsx",
    sheet_name="Table 2",
    skiprows=1
    )

print(df.columns.tolist())
print(df.head())

# Checking for Regional Names
df_itl1 = df[df["ITL"] == "ITL1"]
print(df_itl1.shape)
print(df_itl1["Region name"].tolist())

# Checking for Data Types
df_itl1.dtypes

df_itl1.isna().sum()

df_itl1["2012"]

for value in df_itl1["2012"]:
    print(value, type(value))

# Limiting Years from 1998 to 2023
year_columns = [str(year) for year in range(1998, 2024)]
df_itl1[year_columns] = df_itl1[year_columns].apply(pd.to_numeric, errors="coerce")
df_itl1.dtypes
df_itl1.isna().sum()

df_itl1.dtypes

# Checking for Regions of 2008 and 2023
df_itl1[["Region name", "2008", "2023"]]

# 3. Caculating GVA per head in each Region
df_indexed = df_itl1[year_columns].div(df_itl1["2008"], axis=0) * 100
df_indexed

df_indexed["2008"]

df_indexed["Region name"] = df_itl1["Region name"]
df_indexed.head()

# Sanity check
df["ITL"] == "ITL1"

df_itl1 = df[df["ITL"] == "ITL1"]
type(df_itl1)
print(df_itl1.shape)

# London's raw 2016 GVA per head value on its own cleaning
df_itl1[df_itl1["Region name"] == "London"]["2016"]

year_columns = [str(year) for year in range(1998, 2024)]
df_itl1[year_columns] = df_itl1[year_columns].apply(pd.to_numeric, errors="coerce")
df_itl1[df_itl1["Region name"] == "London"]["2016"]
df["ITL"] == "ITL1"

# 4. Calculate CAGR across Regions
start = 39929
end = 48701
years = 8
cagr = (end / start) ** (1 / years) - 1 
print(cagr)

cagr_percent = cagr * 100 
print(cagr_percent)

df_itl1[df_itl1["Region name"] == "North East"]["2008"]

df_itl1[df_itl1["Region name"] == "North East"]["2008"]

start = 17290
end = 19600
years = 8
cagr = (end / start) ** (1 / years) - 1
print(cagr)

cagr_present = cagr * 100
print(cagr_present)

print(years)

df_itl1[df_itl1["Region name"] == "North East"]["2019"]

start = 19600
end = 21262
years = 3
cagr = (end / start) ** (1 / years) - 1
print(cagr)

cagr_present = cagr * 100
print(cagr_present)

df_itl1[df_itl1["Region name"] == "London"]["2019"]

start = 48701
end = 53124
years = 3 
cagr = (end / start) ** (1 / years) - 1 
print(cagr)

cagr_present = cagr * 100 
print(cagr_present)

df_itl1[df_itl1["Region name"] == "London"]["2023"]

start = 53124
end = 64519
years = 4
cagr = (end / start) ** (1 / years) - 1 
print(cagr)

cagr_present = cagr * 100 
print(cagr_present)

df_itl1[df_itl1["Region name"] == "North East"]["2023"]

start = 21262
end = 25408
years = 4
cagr = (end / start) ** (1 / years) - 1 
print(cagr)

cagr_present = cagr * 100 
print(cagr_present)

regions = ["London", "North East", "Scotland"]
for region in regions:
    print(region)

regions = ["London", "North East", "Scotland"]
for region in regions: 
    start_value = df_itl1[df_itl1["Region name"] == region]["2008"]
    print(region, start_value)

regions = df_itl1["Region name"].tolist()
print(regions)

for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2008"]
    end = df_itl1[df_itl1["Region name"] == region]["2016"]
    years = 8
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2016"]
    end = df_itl1[df_itl1["Region name"] == region]["2019"]
    years = 3
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)

for region in regions:
    start = df_itl1[df_itl1["Region name"] == region]["2019"]
    end = df_itl1[df_itl1["Region name"] == region]["2023"]
    years = 4
    cagr = (end / start) ** (1 / years) - 1
    cagr_percent = cagr * 100
    print(region, cagr_percent)


# 5. Visualisations 
import matplotlib.pyplot as plt 
df_indexed.set_index("Region name")[year_columns].T

df_plot = df_indexed.set_index("Region name")[year_columns].T
df_plot.plot(figsize=(12, 7))
plt.title("Regional GVA per head, indexed to 2008 = 100")
plt.xlable("Year")
plt.ylable("Index (2008 = 100)")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()

years_columns_gva_trimmed = [str(year) for year in range(2008, 2024)]
df_gva_plot_trimmed = df_indexed.set_index("Region name")[years_columns_gva_trimmed].T
df_gva_plot_trimmed.plot(figsize=(12, 7)) 
plt.title("Regional GVA per head, indexed 2008 = 100") 
plt.xlabel("Years") 
plt.ylabel("Indexed GVA") 
plt.legend(loc="upper left", bbox_to_anchor=(1, 1)) 
plt.show()
