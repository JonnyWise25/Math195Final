# Link to origional repo
https://github.com/mggg-states/OK-shapefiles

# Oklahoma Election Shapefile
This shapefile comes from the University of Oklahoma's Center for Spatial Analysis and processed by members of the Metric Geometry and Gerrymandering Group (MGGG).

## Sources
This precinct shapefile was obtained from the [Oklahoma Data Warehouse](https://data.csa.ou.edu) hosted by the Center for Spatial Analysis at the University of Oklahoma. Election results come from the [Oklahoma State Election Board](https://www.ok.gov/elections/Election_Info/Election_Results/2018-Election_Results.html).  2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile as well as congressional and state legislative districts for Oklahoma were downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

## Processing
Oklahoma reports absentee and early votes at the precinct level for every county except for Oklahoma County and Tulsa County, where non-election day votes are reported for the whole county. For those two counties, absentee and early votes were disaggregated to the precinct level by population. Demographic data were aggregated from the block level and precincts were assigned to congressional and state legislative districts using [MGGG’s proration software](https://github.com/mggg/maup). Precincts for Pushmataha County were digitized to conform to a map provided by the county.

## Metadata
* `PRECINCT`: Precinct code
* `COUNTY`: County code
* `CNTYNAME`: County Name
* `CNTYFIPS`: County FIPS code
* `PRECODE`: County code and precinct code
* `AG18D`: Number of votes for 2018 Democratic attorney general candidate
* `AG18R`: Number of votes for 2018 Republican attorney general candidate
* `AUD18L`: Number of votes for 2018 Libertarian state auditor candidate
* `AUD18R`: Number of votes for 2018 Republican state auditor candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `LG18D`: Number of votes for 2018 Democratic lieutenant governor candidate
* `LG18R`: Number of votes for 2018 Republican lieutenant governor candidate
* `TRE18I`: Number of votes for 2018 Independant treasurer candidate
* `TRE18R`: Number of votes for 2018 Republican treasurer candidate
* `USH18D`: Number of votes for 2018 Democratic US house candidates
* `USH18R`: Number of votes for 2018 Republican US house candidates
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
* `CD`: Congressional district ID
* `SEND`: State Senate district ID
* `HDIST`: State House district ID

## Projection
This shapefile uses a NAD83/UTM zone 13N projection (EPSG: 2957).
