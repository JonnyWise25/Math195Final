# Link to origional repo
https://github.com/mggg-states/MN-shapefiles

# Minnesota Election Shapefile
These shapefiles along with election results were created by the Office of the Minnesota Secretary of State with additional processing by MGGG staff. They replace a
previous version of this data which can still be accessed in the [Archived](https://github.com/mggg-states/MN-shapefiles/tree/master/Archived) folder of this
repository. This updated version includes absentee/mail-in ballots as well as correction of topology errors and precinct boundary errors by the Secretary of State's office.

## Sources
These precinct shapefiles with election results were created by the Minnesota Secretary of State's Election Division and downloaded from the [Minnesota Geospatial
Commons](https://gisdata.mn.gov/dataset/bdry-electionresults-2012-2020). 2010 Decennial Census demographic data were downloaded from the
[Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for Minnesota was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

## Processing
These shapefiles came with election data already joined and precincts assigned to districts. Demographic data were aggregated from the block level to precinct
using [MGGG’s proration software](https://github.com/mggg/maup). The MN12_18 file is the 2018 precinct boundaries with election data from 2012-2016 interpolated
onto the 2018 boundaries using the `maup` package with voting age population as the weight.

## Metadata
**2012 Precincts:**
* `VTD`: Voting tabulation district ID
* `PCTNAME`: Precinct name
* `PCTCODE`: Precinct code
* `MCDNAME`: Minor civil division name
* `MCDCODE`: Minor civil division code
* `CTU_TYPE`: Jurisdiction's governence (city, township, unorganized territory)
* `COUNTYNAME`: County name
* `COUNTYFIPS`: County FIPS code
* `CONGDIST`: Congressional district
* `MNSENDIST`: State Senate district
* `MNLEGDIST`: State House district
* `CTYCOMDIST`: County Commissioner district
* `JUDDIST`: Judicial District
* `TOTVOT12`: Total number of voters casting ballots in 2012
* `PRES12R`: Number of votes for 2012 Republican presidential candidate
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate
* `PRES12L`: Number of votes for 2012 Libertarian presidential candidate
* `SEN12I`: Number of votes for 2012 Independent senate candidate
* `SEN12R`: Number of votes for 2012 Republican senate candidate
* `SEND12D`: Number of votes for 2012 Democratic senate candidate
* `USH12R`: Number of votes for 2012 Republican US House candidates
* `USH12D`: Number of votes for 2012 Democratic US House candidates
* `SSEN12I`: Number of votes for 2012 Independent state senate candidates
* `SSEN12R`: Number of votes for 2012 Republican state senate candidates
* `SSEN12D`: Number of votes for 2012 Democratic state senate candidates
* `SH12I`: Number of votes for 2012 Independent state house candidates
* `SH12R`: Number of votes for 2012 Republican state house candidates
* `SH12D`: Number of votes for 2012 Democratic state house candidates
* `CA1YES12`: Number of votes in favor of Constitutional Amendment 1 (recognition of marriage solely between one man and one woman)
* `CA1NO12`: Number of votes against Constitutional Amendment 1 (recognition of marriage solely between one man and one woman)
* `CA2YES12`: Number of votes in favor of Constitutional Amendment 2 (photo ID required for voting)
* `CA2NO12`: Number of votes against Constitutional Amendment 2 (photo ID required for voting)
* `TOTPOP`: Total population
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `H_WHITE`: White, hispanic, population
* `H_BLACK`: Black, hispanic, population
* `H_AMIN`: American Indian and Alaska Native, hispanic, population
* `H_ASIAN`: Asian, hispanic, population
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
* `H_OTHER`: Other race, hispanic, population
* `H_2MORE`: Two or more races, hispanic, population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population

**2014 Precincts:**
* `VTDID`: Voting tabulation district ID
* `PCTNAME`: Precinct name
* `PCTCODE`: Precinct code
* `MCDNAME`: Minor civil division name
* `MCDCODE`: Minor civil division code
* `CTU_TYPE`: Jurisdiction's governence (city, township, unorganized territory)
* `COUNTYNAME`: County name
* `COUNTYFIPS`: County FIPS code
* `CONGDIST`: Congressional district
* `MNSENDIST`: State Senate district
* `MNLEGDIST`: State House district
* `CTYCOMDIST`: County Commissioner district
* `JUDDIST`: Judicial District
* `TOTVOT14`: Total number of voters casting ballots in 2014
* `SEN14I`: Number of votes for 2014 Independent senate candidate
* `SEN14R`:  Number of votes for 2014 Republican senate candidate
* `SEN14D`: Number of votes for 2014 Democratic senate candidate
* `SEN14L`: Number of votes for 2014 Libertarian senate candidate
* `USH14I`: Number of votes for 2014 Independent US house candidates
* `USH14R`: Number of votes for 2014 Republcian US house candidates
* `USH14D`: Number of votes for 2014 Democratic US house candidates
* `SH14I`: Number of votes for 2014 Independent state house candidates
* `SH14R`: Number of votes for 2014 Republican state house candidates
* `SH14D`: Number of votes for 2014 Democratic state house candidates
* `GOV14I`: Number of votes for 2014 Independent gubernatorial candidate
* `GOV14R`: Number of votes for 2014 Republican gubernatorial candidate
* `GOV14D`: Number of votes for 2014 Democratic gubernatorial candidate
* `SOS14I`: Number of votes for 2014 Independent secretary of state candidate
* `SOS14R`: Number of votes for 2014 Republican secretary of state candidate
* `SOS14D`: Number of votes for 2014 Democratic secretary of state candidate
* `AUD14I`: Number of votes for 2014 Independent auditor candidate
* `AUD14R`: Number of votes for 2014 Republican auditor candidate
* `AUD14D`: Number of votes for 2014 Democratic auditor candidate
* `AUD14L`: Number of votes for 2014 Libertarian auditor candidate
* `AUD14LC`: Number of votes for 2014 Grassroots Legalize Cannabis Party auditor candidate
* `AG14I`: Number of votes for 2014 Independent attorney general candidate
* `AG14R`: Number of votes for 2014 Republican attorney general candidate
* `AG14D`: Number of votes for 2014 Democratic attorney general candidate
* `AG14G`: Number of votes for 2014 Green Party attorney general candidate
* `AG14L`: Number of votes for 2014 Libertarian attorney general candidate
* `AG14LM`: Number of votes for 2014 Legal Marijauna Now Party attorney general candidate
* `TOTPOP`: Total population
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `H_WHITE`: White, hispanic, population
* `H_BLACK`: Black, hispanic, population
* `H_AMIN`: American Indian and Alaska Native, hispanic, population
* `H_ASIAN`: Asian, hispanic, population
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
* `H_OTHER`: Other race, hispanic, population
* `H_2MORE`: Two or more races, hispanic, population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population

**2016 Precincts:**
* `VTDID`: Voting tabulation district ID
* `PCTNAME`: Precinct name
* `PCTCODE`: Precinct code
* `MCDNAME`: Minor civil division name
* `MCDCODE`: Minor civil division code
* `CTU_TYPE`: Jurisdiction's governence (city, township, unorganized territory)
* `COUNTYNAME`: County name
* `COUNTYFIPS`: County FIPS code
* `CONGDIST`: Congressional district
* `MNSENDIST`: State Senate district
* `MNLEGDIST`: State House district
* `CTYCOMDIST`: County Commissioner district
* `JUDDIST`: Judicial District
* `TOTVOT16`: Total number of voters casting ballots in 2016
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16G`: Number of votes for 2016 Green Party presidential candidate
* `PRES16I`: Number of votes for 2016 Independent presidential candidate
* `PRES16L`: Number of votes for 2016 Libertarian presidential candidate
* `USH16R`: Number of votes for 2016 Republican US house candidates
* `USH16D`: Number of votes for 2016 Democratic US house candidates
* `SSEN16R`: Number of votes for 2016 Republican state senate candidates
* `SSEN16D`: Number of votes for 2016 Democratic state senate candidates
* `SH16R`: Number of votes for 2016 Republican state house candidates
* `SH16D`: Number of votes for 2016 Democratic state house candidates
* `TOTPOP`: Total population
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `H_WHITE`: White, hispanic, population
* `H_BLACK`: Black, hispanic, population
* `H_AMIN`: American Indian and Alaska Native, hispanic, population
* `H_ASIAN`: Asian, hispanic, population
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
* `H_OTHER`: Other race, hispanic, population
* `H_2MORE`: Two or more races, hispanic, population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population


**2018 Precincts:**
* `VTDID`: Voting tabulation district ID
* `PCTNAME`: Precinct name
* `PCTCODE`: Precinct code
* `MCDNAME`: Minor civil division name
* `MCDCODE`: Minor civil division code
* `CTU_TYPE`: Jurisdiction's governence (city, township, unorganized territory)
* `COUNTYNAME`: County name
* `COUNTYFIPS`: County FIPS code
* `CONGDIST`: Congressional district
* `MNSENDIST`: State Senate district
* `MNLEGDIST`: State House district
* `CTYCOMDIST`: County Commissioner district
* `JUDDIST`: Judicial District
* `TOTVOT18`: Total number of voters casting ballots in 2018
* `SEN18R`: Number of votes for 2018 Republican senate candidate
* `SEN18D`: Number of votes for 2018 Democratic senate candidate
* `SEN18LM`: Number of votes for 2018 Legal Marijuana Party senate candidate
* `SP_SEN18R`: Number of votes for 2018 Republican senate candidate (special election)
* `SP_SEN18D`: Number of votes for 2018 Democratic senate candidate (special election)
* `SP_SEN18LM`: Number of votes for 2018 Legal Marijuana Party senate candidate (special election)
* `USH18R`: Number of votes for 2018 Republican US house candidates
* `USH18D`: Number of votes for 2018 Democratic US house candidates
* `SSEN18R`: Number of votes for 2018 Republican state senate candidates
* `SSEN18D`: Number of votes for 2018 Democratic state senate candidates
* `SH18R`: Number of votes for 2018 Republican state house candidates
* `SH18D`: Number of votes for 2018 Democratic state house candidates
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18LC`: Number of votes for 2018 Grassroots Legalize Cannabis Party gubernatorial candidate
* `GOV18L`: Number of votes for 2018 Libertarian gubernatorial candidate
* `SOS18R`: Number of votes for 2018 Republican secretary of state candidate
* `SOS18D`: Number of votes for 2018 Democratic secretary of state candidate
* `SOS18I`: Number of votes for 2018 Independent secretary of state candidate
* `AUD18R`: Number of votes for 2018 Republican auditor candidate
* `AUD18D`: Number of votes for 2018 Democratic auditor candidate
* `AUD18LM`: Number of votes for 2018 Legal Marijuana Now Party auditor candidate
* `AUD18L`: Number of votes for 2018 Libertarian auditor candidate
* `AG18R`: Number of votes for 2018 Republican attorney general candidate
* `AG18D`: Number of votes for 2018 Democratic attorney general candidate
* `AG18LC`: Number of votes for 2018 Grassroots Legalize Cannabis Party attorney general candidate
* `TOTPOP`: Total population
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `H_WHITE`: White, hispanic, population
* `H_BLACK`: Black, hispanic, population
* `H_AMIN`: American Indian and Alaska Native, hispanic, population
* `H_ASIAN`: Asian, hispanic, population
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
* `H_OTHER`: Other race, hispanic, population
* `H_2MORE`: Two or more races, hispanic, population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population
* `TOTVOT16`: Total number of voters casting ballots in 2016
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16G`: Number of votes for 2016 Green Party presidential candidate
* `PRES16I`: Number of votes for 2016 Independent presidential candidate
* `PRES16L`: Number of votes for 2016 Libertarian presidential candidate
* `USH16R`: Number of votes for 2016 Republican US house candidates
* `USH16D`: Number of votes for 2016 Democratic US house candidates
* `SSEN16R`: Number of votes for 2016 Republican state senate candidates
* `SSEN16D`: Number of votes for 2016 Democratic state senate candidates
* `SH16R`: Number of votes for 2016 Republican state house candidates
* `SH16D`: Number of votes for 2016 Democratic state house candidates
* `TOTVOT14`: Total number of voters casting ballots in 2014
* `SEN14I`: Number of votes for 2014 Independent senate candidate
* `SEN14R`:  Number of votes for 2014 Republican senate candidate
* `SEN14D`: Number of votes for 2014 Democratic senate candidate
* `SEN14L`: Number of votes for 2014 Libertarian senate candidate
* `USH14I`: Number of votes for 2014 Independent US house candidates
* `USH14R`: Number of votes for 2014 Republcian US house candidates
* `USH14D`: Number of votes for 2014 Democratic US house candidates
* `SH14I`: Number of votes for 2014 Independent state house candidates
* `SH14R`: Number of votes for 2014 Republican state house candidates
* `SH14D`: Number of votes for 2014 Democratic state house candidates
* `GOV14I`: Number of votes for 2014 Independent gubernatorial candidate
* `GOV14R`: Number of votes for 2014 Republican gubernatorial candidate
* `GOV14D`: Number of votes for 2014 Democratic gubernatorial candidate
* `SOS14I`: Number of votes for 2014 Independent secretary of state candidate
* `SOS14R`: Number of votes for 2014 Republican secretary of state candidate
* `SOS14D`: Number of votes for 2014 Democratic secretary of state candidate
* `AUD14I`: Number of votes for 2014 Independent auditor candidate
* `AUD14R`: Number of votes for 2014 Republican auditor candidate
* `AUD14D`: Number of votes for 2014 Democratic auditor candidate
* `AUD14L`: Number of votes for 2014 Libertarian auditor candidate
* `AUD14LC`: Number of votes for 2014 Grassroots Legalize Canabis Party auditor candidate
* `AG14I`: Number of votes for 2014 Independent attorney general candidate
* `AG14R`: Number of votes for 2014 Republican attorney general candidate
* `AG14D`: Number of votes for 2014 Democratic attorney general candidate
* `AG14G`: Number of votes for 2014 Green Party attorney general candidate
* `AG14L`: Number of votes for 2014 Libertarian attorney general candidate
* `AG14LM`: Number of votes for 2014 Legal Marijauna Now Party attorney general candidate
* `TOTVOT12`: Total number of voters casting ballots in 2012
* `PRES12R`: Number of votes for 2012 Republican presidential candidate
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate
* `PRES12L`: Number of votes for 2012 Libertarian presidential candidate
* `SEN12I`: Number of votes for 2012 Independent senate candidate
* `SEN12R`: Number of votes for 2012 Republican senate candidate
* `SEND12D`: Number of votes for 2012 Democratic senate candidate
* `USH12R`: Number of votes for 2012 Republican US House candidates
* `USH12D`: Number of votes for 2012 Democratic US House candidates
* `SSEN12I`: Number of votes for 2012 Independent state senate candidates
* `SSEN12R`: Number of votes for 2012 Republican state senate candidates
* `SSEN12D`: Number of votes for 2012 Democratic state senate candidates
* `SH12I`: Number of votes for 2012 Independent state house candidates
* `SH12R`: Number of votes for 2012 Republican state house candidates
* `SH12D`: Number of votes for 2012 Democratic state house candidates
* `CA1YES12`: Number of votes in favor of Constitutional Amendment 1 (recognition of marriage solely between one man and one woman)
* `CA1NO12`: Number of votes against Constitutional Amendment 1 (recognition of marriage solely between one man and one woman)
* `CA2YES12`: Number of votes in favor of Constitutional Amendment 2 (photo ID required for voting)
* `CA2NO12`: Number of votes against Constitutional Amendment 2 (photo ID required for voting)

## Projection
These shapefiles use a NAD83/UTM zone 15N projection (EPSG: 26915).

## Rating
We give these shapefiles an A rating. All data was obtained from the state government and was processed by MGGG staff.
