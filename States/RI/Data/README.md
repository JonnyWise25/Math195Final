# Link to origional repo
https://github.com/mggg-states/RI-shapefiles

# Rhode Island Election Shapefile
This shapefile was obtained from the Rhode Island GIS Data Distribution System and processed by members of the Metric Geometry and Gerrymandering Group (MGGG).

## Sources
The precinct, congressional, state house, and state senate district shapefiles come from the Rhode Island Department of State through the [Rhode Island GIS Data Distribution System](http://www.rigis.org). 2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for Rhode Island was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html). Election data were downloaded from the [Rhode Island Board of Elections](http://www.elections.ri.gov/elections/preresults/).

## Processing
Election data from the RI Board of Elections were cleaned by MGGG staff to join it to the precinct shapefile. Demographic data were aggregated from the block level to precincts using [MGGG’s proration software](https://github.com/mggg/maup). Congressional, house, and senate district IDs were assigned to precincts also using this package.

## Metadata
* `NAME`: Precinct Name
* `Shape__Are`: Precinct area in square degree
* `Shape__Len`: Precinct perimeter in degree
* `JOINID`: Precinct ID
* `PRENAME`: Precinct name
* `REGVOT16`: Number of registered voters for 2016 general election
* `TOTVOT16`: Number of ballots cast in 2016 general election
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `REGVOT18`: Number of registered voters for 2018 general election
* `TOTVOT18`: Number of ballots cast in 2018 general election
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `SEN18D`: Number of votes for 2018 Democratic senate candidate
* `SEN18R`: Number of votes for 2018 Republican senate candidate
* `TOTPOP`: Total population
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population
* `HDIST`: State house district ID
* `SENDIST`: State senate district ID
* `CD`: Congressional district ID

## Rating
We give this shapefile an A rating. All data was obtained through the state government and was processed by MGGG staff.
