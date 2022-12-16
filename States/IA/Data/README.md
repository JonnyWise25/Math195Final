# Link to origional repo
https://github.com/mggg-states/IA-shapefiles

# Iowa Election Shapefile
This shapefile was obtained from the US Census Bureau and processed by members of the Metric Geometry and Gerrymandering Group (MGGG). It is at the county level, as Iowa has strict laws regarding county preservation in congressional redistricting.

## Sources
The county shapefile comes from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/cgi-bin/geo/shapefiles/index.php). 2010 Decennial Census demographic data were downloaded from [American FactFinder](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml). County level election data for presidential elections since 2000 were obtained from the [MIT Elections Data and Science Lab](https://electionlab.mit.edu). The Congressional district shapefile was obtained from the [Iowa Legislature](https://www.legis.iowa.gov/legislators/districtMaps).

## Processing
Election data from the MIT Elections Data and Science Lab was cleaned by MGGG staff in order to join it to the county shapefile. Demographic data   were joined to the county shapefile in QGIS.

## Metadata
* `STATEFP10`: State FIPS code
* `COUNTYFP`: County FIPS
* `GEOID10`: State and county FIPS
* `NAME10`: County name
* `NAMELSAD`: County legal and statistical name
* `ALAND10`: Area land in square meters
* `AWATER10`: Area water in square meters
* `INTPTLAT10`: Latitude of internal point
* `INTPTLON10`: Longitude of internal point
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
* `TOTVOT00`: Number of votes cast in 2000 presidential race
* `PRES00D`: Number of votes for 2000 Democratic presidential candidate
* `PRES00R`: Number of votes for 2000 Republican presidential candidate
* `PRES00G`: Number of votes for 2000 Green Party presidential candidate
* `PRES00OTH`: Number of votes for 2000 other presidential candidates
* `TOTVOT04`: Number of votes cast in 2004 presidential race
* `PRES04D`: Number of votes for 2004 Democratic presidential candidate
* `PRES04R`: Number of votes for 2004 Republican presidential candidate
* `PRES04OTH`: Number of votes for 2004 other presidential candidates
* `TOTVOT08`: Number of votes cast in 2008 presidential race
* `PRES08D`: Number of votes for 2008 Democratic presidential candidate
* `PRES08R`: Number of votes for 2008 Republican presidential candidate
* `PRES08OTH`: Number of votes for 2008 other presidential candidates
* `TOTVOT12`: Number of votes cast in 2012 presidential race
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate
* `PRES12R`: Number of votes for 2012 Republican presidential candidate
* `PRES12OTH`: Number of votes for 2012 other presidential candidates
* `TOTVOT16`: Number of votes cast in 2016 presidential race
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `PRES16OTH`: Number of votes for 2016 other presidential candidates
* `CD`: Congressional district ID


## Rating
We give this shapefile an A rating. All data was obtained through the state government and was processed by MGGG staff.
