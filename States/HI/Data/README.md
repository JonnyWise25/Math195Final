# Link to origional repo

# Hawaii Election Shapefile
This shapefile comes from Hawaii Statewide GIS Program and was processed by Metric Geometry and Gerrymandering Group (MGGG) staff.

## Sources
This precinct shapefile comes from the [Hawaii Statewide GIS Program](http://planning.hawaii.gov/gis/download-gis-data/) in the State Office of Planning. Election results come from the [State of Hawaii Office of Elections](https://elections.hawaii.gov/election-results/). 2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for Hawaii was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

## Preprocessing
Precincts 41-02 and 41-05 were merged as were precincts 42-01 and 42-04 in order to join 2016 and 2018 results onto the same precinct boundaries. Demographic data were aggregated from the block level using [MGGG’s proration software](https://github.com/mggg/maup).

## Metadata
* `NAME`: Precinct code
* `DPTYPE`: Precinct type (PP: polling place, ZEROPOP: zero population precinct, VBMO: vote-by-mail only)
* `COUNTY`: County name
* `ZEROPOP`: Zero population precinct (yes/null)
* `BALLOTTYPE`: Congressional district-state house district-state senate district-county council district
* `CD`: Congressional district ID
* `HDIST`: State House district ID
* `SEND`: State Senate district ID
* `SEN18D`: Number of votes for 2018 Democratic senate candidate
* `SEN18R`: Number of votes for 2018 Republican senate candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `USH18D`: Number of votes for 2018 Democratic US house candidates
* `USH18R`: Number of votes for 2018 Republican US house candidates
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `SEN16D`: Number of votes for 2016 Democratic senate candidate
* `SEN16R`: Number of votes for 2016 Republican senate candidate
* `USH16D`: Number of votes for 2016 Democratic US house candidates
* `USH16R`: Number of votes for 2016 Republican US house candidates
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

## Projection
This shapefile uses Hawaii Albers Equal Area Conic projection.

## Rating
We give these shapefiles an A rating. All data was obtained from the state government and was processed by MGGG staff.
