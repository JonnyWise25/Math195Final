# Link to origional repo
https://github.com/mggg-states/CT-shapefiles

# Connecticut Election Shapefiles
This shapefile was compiled and processed by members of the Metric Geometry and Gerrymandering Group (MGGG).  

## Sources
Raw data for Connecticut's voting district boundaries was sourced from election and other town officials and processed by members of MGGG. Precinct-level election results were obtained from the Connecticut Secretary of State's [Election Center](https://ctemspublic.pcctg.net/#/home). Block level demographic data for the 2010 Decennial Census were retrieved using the [Census API](https://api.census.gov/data/2010/dec/sf1).

## Preprocessing
Of Connecticut's 169 towns, 65 have a townwide precinct, 36 towns' voting districts matched the 2010 Census VTDs, and the remaining 68 were digitized from maps provided by the towns or edited using the state voterfile. Demographic data were aggregated from the census block level and voting districts were assigned to districts using [MGGG's proration software](https://github.com/mggg/maup).

## Metadata
* `STATEFP10`: State FIPS code
* `COUNTYFP10`: County FIPS code
* `NAME10`: Precinct name
* `NAMELSAD10`: Precinct name
* `PRECINCT`: Town and polling place name
* `AG18D`: Number of votes for 2018 Democratic attorney general candidate
* `AG18R`: Number of votes for 2018 Republican attorney general candidate
* `COMP18D`: Number of votes for 2018 Democratic comptroller candidate
* `COMP18R`: Number of votes for 2018 Republican comptroller candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `SOS18D`: Number of votes for 2018 Democratic secretary of state candidate
* `SOS18R`: Number of votes for 2018 Republican secretary of state candidate
* `TRE18D`: Number of votes for 2018 Democratic treasurer candidate
* `TRE18R`: Number of votes for 2018 Republican treasurer candidate
* `SEN18D`: Number of votes for 2018 Democratic senate candidate
* `SEN18R`: Number of votes for 2018 Republican senate candidate
* `USH18D`: Number of votes for 2018 Democratic US House candidate
* `USH18R`: Number of votes for 2018 Republican US House candidate
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
* `CD`: US Congressional district
* `HDIST`: Connecticut House district
* `SEND`: Connecticut Senate district

## Projection
This shapefile uses a NAD83/Connecticut projection (EPSG:26956).
