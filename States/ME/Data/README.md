# Link to origional repo
https://github.com/mggg-states/ME-shapefiles

# Maine Election Shapefiles
This shapefile was obtained from the Maine Geolibrary website and processed by students in Diana Davis' Districting Data REU. This effort was led by Jorge Lopez-Nava and Katie Knox and included Nathaniel Cox, Angus Lam, Jennifer Paige, Nathan Pitock, Powell Sheagren, and Victoria Song. Some additional processing was done by MGGG staff.

## Sources
The Maine precinct shapefile was obtained from the [Maine Geolibrary](https://www.maine.gov/geolib/catalog.html), a GIS service of the State of Maine. Election data come from the [Maine Bureau of Corporations, Elections, & Commissions](https://www.maine.gov/sos/cec/elec/results/index.html). 2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for Maine was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).


## Processing
Some very limited merging of precincts in the tabular election data and precinct shapefile were necessary to join election results to precinct boundaries. Data from absentee votes reported at the state level were disaggregated by voting age population. Because of data reporting and processing, a few precincts cross county boundaries. Demographic data were aggregated from the block level using MGGG’s proration software. Congressional and state legislative district IDs were also assigned to precincts using this package.


## Metadata
* `STATE`: State
* `STATEFP`: State FIPS code
* `COUNTY`: County name
* `COUNTYFP`: County FIPS code
* `Precinct`: Precinct name
* `CODE`: Precinct code
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate, without absentee votes
* `PRES12R`: Number of votes for 2012 Republican presidential candidate, without absentee votes
* `SEN14D`: Number of votes for 2014 Democratic senate candidate, without absentee votes
*	`SEN14R`: Number of votes for 2014 Republican senate candidate, without absentee votes
*	`PRES16D`: Number of votes for 2016 Democratic presidential candidate, without absentee votes
*	`PRES16R`: Number of votes for 2016 Republican presidential candidate, without absentee votes
*	`USH16D`: Number of votes for 2016 Democratic US House candidate, without absentee votes
*	`USH16R`: Number of votes for 2016 Republican US House candidate, without absentee votes
*	`SEN18D`: Number of votes for 2018 Democratic senate candidate, without absentee votes
*	`SEN18R`: Number of votes for 2018 Republican senate candidate, without absentee votes
*	`SEN18I`: Number of votes for 2018 Independent senate candidate, without absentee votes
*	`USH18D`: Number of votes for 2018 Democratic US House candidate, without absentee votes
*	`USH18R`: Number of votes for 2018 Republican US House candidate, without absentee votes
* `PRES12D+`: Number of votes for 2012 Democratic presidential candidate, with absentee votes
* `PRES12R+`: Number of votes for 2012 Republican presidential candidate, with absentee votes
* `SEN14D+`: Number of votes for 2014 Democratic senate candidate, with absentee votes
*	`SEN14R+`: Number of votes for 2014 Republican senate candidate, with absentee votes
*	`PRES16D+`: Number of votes for 2016 Democratic presidential candidate, with absentee votes
*	`PRES16R+`: Number of votes for 2016 Republican presidential candidate, with absentee votes
*	`USH16D+`: Number of votes for 2016 Democratic US House candidate, with absentee votes
*	`USH16R+`: Number of votes for 2016 Republican US House candidate, with absentee votes
*	`SEN18D+`: Number of votes for 2018 Democratic senate candidate, with absentee votes
*	`SEN18R+`: Number of votes for 2018 Republican senate candidate, with absentee votes
*	`SEN18I+`: Number of votes for 2018 Independent senate candidate, with absentee votes
*	`USH18D+`: Number of votes for 2018 Democratic US House candidate, with absentee votes
*	`USH18R+`: Number of votes for 2018 Republican US House candidate, with absentee votes
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
* `HDIST`: State House district
* `SEND`: State Senate district

## Projection
This shapefile uses a UTM Zone 19 projection (ESPG:6348).

## Rating
We give this shapefile an A rating. All data were obtained from the state government and processing was conducted by a group trained by and working closely with MGGG.
