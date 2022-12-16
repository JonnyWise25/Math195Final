# Link to origional repo
https://github.com/mggg-states/NE-shapefiles

# Nebraska Election Shapefiles
This shapefile was obtained from state and county sources and processed by students in Diana Davis' Districting Data REU. This effort was led by Poonam Sahoo and included Jiahua Chen, Kevin Choi, Keegan McKenna, Celia Parts, Justin Snyder and Alicia Yang. Additional processing was done by MGGG staff.

## Sources
Raw data for Nebraska's precinct boundaries were sourced from [NebraskaMAP](https://www.nebraskamap.gov/datasets/voting-districts) page, a GIS service of the State of Nebraska, and supplemented by more recent data from county officials. Election data were provided by the [Nebraska Secretary of State, Elections Division](https://sos.nebraska.gov/elections/elections-division). 2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for Nebraska was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

## Processing
Some merging of precincts in the tabular election data and precinct shapefile were necessary to join election results to precinct boundaries. Data from absentee votes reported at the county level were disaggregated to precincts by voting age population. Demographic data were aggregated from blocks to precincts using MGGG’s proration software. Congressional and state legislative district IDs were also assigned to precincts using this package.

## Metadata
* `STATE`: State
* `STATEFP`: State FIPS code
* `COUNTY`: County name
* `COUNTYFP`: County FIPS code
* `Precinct`: Precinct name
* `CODE`: Precinct code
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate, without absentee votes
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate, without absentee votes
*	`USH18D`: Number of votes for 2018 Democratic US House candidate, without absentee votes
*	`USH18R`: Number of votes for 2018 Republican US House candidate, without absentee votes
*	`SOS18D`: Number of votes for 2018 Democratic secretary of state candidate, without absentee votes
*	`SOS18R`: Number of votes for 2018 Republican secreatary of state candidate, without absentee votes
* `GOV18D+`: Number of votes for 2018 Democratic gubernatorial candidate, with absentee votes
* `GOV18R+`: Number of votes for 2018 Republican gubernatorial candidate, with absentee votes
*	`USH18D+`: Number of votes for 2018 Democratic US House candidate, with absentee votes
*	`USH18R+`: Number of votes for 2018 Republican US House candidate, with absentee votes
*	`SOS18D+`: Number of votes for 2018 Democratic secretary of state candidate, with absentee votes
*	`SOS18R+`: Number of votes for 2018 Republican secreatary of state candidate, with absentee votes
* `TOTPOP`: Total population from 2010 Decennial Census
* `NH_WHITE`: White, non-hispanic, population from 2010 Decennial Census
* `NH_BLACK`: Black, non-hispanic, population from 2010 Decennial Census
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population from 2010 Decennial Census
* `NH_ASIAN`: Asian, non-hispanic, population from 2010 Decennial Census
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population from 2010 Decennial Census
* `NH_OTHER`: Other race, non-hispanic, population from 2010 Decennial Census
* `NH_2MORE`: Two or more races, non-hispanic, population from 2010 Decennial Census
* `HISP`: Hispanic population from 2010 Decennial Census
* `H_WHITE`: White, hispanic, population from 2010 Decennial Census
* `H_BLACK`: Black, hispanic, population from 2010 Decennial Census
* `H_AMIN`: American Indian and Alaska Native, hispanic, population from 2010 Decennial Census
* `H_ASIAN`: Asian, hispanic, population from 2010 Decennial Census
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population from 2010 Decennial Census
* `H_OTHER`: Other race, hispanic, population from 2010 Decennial Census
* `H_2MORE`: Two or more races, hispanic, population from 2010 Decennial Census
* `VAP`: Total voting age population from 2010 Decennial Census
* `HVAP`: Hispanic voting age population from 2010 Decennial Census
* `WVAP`: White, non-hispanic, voting age population from 2010 Decennial Census
* `BVAP`: Black, non-hispanic, voting age population from 2010 Decennial Census
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population from 2010 Decennial Census
* `ASIANVAP`: Asian, non-hispanic, voting age population from 2010 Decennial Census
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population from 2010 Decennial Census
* `OTHERVAP`: Other race, non-hispanic, voting age population from 2010 Decennial Census
* `2MOREVAP`: Two or more races, non-hispanic, voting age population from 2010 Decennial Census
* `CD`: Congressional district
* `SEND`: State Senate district

Notes: State house districts are not included because Nebraska has a unicameral legislature. Also, the Nebraska governor and lieutenant governor are elected together, so the gubernatorial results also represent lieutenant governor results.

## Projection
This shapefile uses a Lambert Conformal Conic/State Plane projection centered on Nebraska (ESPG:6516).

## Rating
We give this shapefile a B rating. A precinct shapefile was available from the state but did not match well with several counties, so state- and county-provided precinct shapefiles were combined. This necessitated doing minor manual edits to precinct boundaries. There are discrepancies of up to .15% between state-reported vote totals and our summed totals in the results that include absentee votes. This does not impact the outcome of any election.
