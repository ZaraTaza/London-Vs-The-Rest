# London-Vs-The-Rest
**Has regional economic inequality in the UK worsened or improved since the 2008 financial crash?**

**Overview**

An economics analysis on UK regions from 2008 to 2023, using Python to examine Gross Value Added (GVA*) per head. This project aims to answer if regional economic inequality has worsened or improved since the 2008 financial crash and whether richer regions, such as London, have been pulling away from the rest of the UK. To examine this, this report also incorporates Gross Disposable Household Income (GDHI**) per head, allowing output (where value is produced) to be compared against income (what residents actually earn).

*GVA is an economic measure of the value of goods and services produced in an area, industry or sector.

**GDHI is the total amount of money that people have left over to spend or save after paying taxes and receiving any direct benefits. 

**Methodology**

Data was sourced from Office for National Statistics which can be found below:

[Regional gross value added (balanced) per head and income components](https://www.ons.gov.uk/economy/grossvalueaddedgva/datasets/nominalregionalgrossvalueaddedbalancedperheadandincomecomponents)

[Regional gross disposable household income: all International Territorial Level (ITL) regions](https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/datasets/regionalgrossdisposablehouseholdincomegdhi)

The data was cleaned and analysed in Python to examine and compare economic trends amongst UK regions from 2008 to 2023. With the common rhetoric that London is pulling away from the rest of the UK, this project explores whether other UK regions were able to recover from the 2008 financial crash, and examines how far the economic gap between London and the rest has widened or narrowed since. 

It should be noted that figures are presented in nominal (current price) terms, as published by the ONS, and are not adjusted for inflation. As a result, some of the growth recorded in later periods particularly 2019–2023, which includes a period of high UK inflation, reflects rising prices as well as genuine economic change.

Regional GVA (output) and GDHI (income) per head were each indexed to 2008 = 100 to allow fair comparison of growth across regions with different starting levels. Compound Annual Growth Rate (CAGR) was calculated across three sub-periods (2008 – 2016, 2016 – 2019 and 2019 – 2023) to identify when divergence occurred. CAGR was used rather than simple percentage change because the three periods are of different lengths (8, 3 and 4 years). CAGR expresses growth as an equivalent constant annual rate, allowing periods of different lengths to be fairly compared. The first sub-period (2008 - 2016) was used to showcase the years with direct impact of the 2008 financial crash; the second sub-period (2016 - 2019) highlighted events such as Brexit and constant changes in government; and the third sub-period (2019 - 2023) is the most recent time frame, captured the pandemic years and the recovery years that followed. Dividing these time frames as such allows us to isolate periods for comparison.

Visualisations were created using Python and are presented throughout this report.

The following code can be found here:

[GVA](https://github.com/ZaraTaza/London-Vs-The-Rest/blob/main/code/GVA.py)

[GDHI](https://github.com/ZaraTaza/London-Vs-The-Rest/blob/main/code/GDHI.py)

**Key Findings**

**1) Regional inequality widened in cash terms**

London's GVA per head grew from £39,929 (2008) to £64,519 (2023) which is a gain of £24,590 per person, more than double the gain other regions saw (e.g. North East: +£8,118). Due to London starting from a much higher base, even similar or middling percentage growth elsewhere still translates into a widening cash gap. London's growth rate was not the fastest in the dataset but its head start meant it did not need to be. It is also worth noting that "the rest of the UK" is not a single economic bloc. Regions have grown at varying rates, with some closing the economic gap with London while others, such as the North East, have fallen further behind. 

However, the story is far more nuanced than merely London advancing ahead from the rest. Indexed to 2008=100, London's overall growth (+61.6% by 2023) was close to several other regions, including Northern Ireland (+62.9%) and North West (+61.0%). Breaking down the data into sub-periods (CAGR) showed a clear U-shape rather than a simple divergence.  

**2) Northern Ireland saw the fastest growth of any region in the most recent period**

Northern Ireland's 2019–2023 GVA CAGR was the highest single figure in the entire dataset at 6.09%. Although its earlier growth (2008–2016) lagged well behind London's, showing this is a recent phenomenon and not a 15-year trend. 

Northern Ireland's growth could be credited to factors such as its trading position as it has dual market access from both the EU and UK post-Brexit but this report does not go into detail on the reasons for economic growth or decline.

**3) On income (GDHI), London's lead is steadier**

Switching from output (GVA) to income (GDHI) does not shrink London's overall position. London's cumulative GDHI index remained the highest of all 12 regions by 2023. In 2019 to 2023, London (4.53%) was only ranked the 3rd-highest of all 12 regions which is quite different from its middling GVA rank in the same period.

Contrary to the common narrative of London "pulling away" from the rest of the UK, London's GDHI growth was consistently strong across all three sub-periods rather than one dominant burst. By contrast, other regions showed more volatile patterns. Northern Ireland, for example, lagged behind on GDHI but had the fastest GVA growth of any region in 2019–2023. This is not a uniform pattern across all regions. Wales is a clear exception, showing a wider gap with London under GDHI than under GVA.

Both charts show a dip in 2020 due to the pandemic, followed by a steep recovery from 2021 onwards, making 2019 – 2023 the strongest CAGR period across the dataset.

**Visualisations**

![Regional GVA per Head](https://github.com/ZaraTaza/London-Vs-The-Rest/blob/main/visuals/GVA.png)
![Regional GDHI per Head](https://github.com/ZaraTaza/London-Vs-The-Rest/blob/main/visuals/GDHI.png)

**Conclusion**

Whether inequality "worsened" or "improved" since 2008 depends entirely on which lens (GVA or GDHI) is used. In GVA  terms, the gap has clearly grown. In relative growth terms, London's advantage was real but concentrated in 2008 to 2016 and has since narrowed or reversed against several regions. This narrowing is more pronounced when using income (GDHI) rather than output (GVA), where London's lead over the rest of the UK looks noticeably smaller once measured by actual household income rather than economic output.
