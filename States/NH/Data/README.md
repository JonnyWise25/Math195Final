# Link to origional repo
https://github.com/mggg-states/NH-shapefiles

# NH-shapefiles
This shapefile was obtained from NH Granit: New Hampshire’s Statewide GIS Clearinghouse. 2012-2018 data were processed by students in Diana Davis' Districting Data REU: Sara Asgari, Quinn Basewitz, Ethan Bergmann, Jack Brogsol, Martina Kampel, Becca Keating, and Dylan Torrance. 2020 data were processed by collaborator Bill Brown from Hanover, NH. Some additional processing was done by MGGG staff.

## Sources
The New Hampshire precinct shapefile was obtained from [NH Granit: New Hampshire’s Statewide GIS Clearinghouse](www.granit.unh.edu/data/downloadfreedata/downloaddata.html), a GIS service of the State of New Hampshire. Election data come from the [New Hampshire Secretary of State](https://sos.nh.gov/elections/elections/election-results/). 2010 Decennial Census demographic data were downloaded from the [Census API](https://api.census.gov/data/2010/dec/sf1). The 2010 census block shapefile for New Hampshire was downloaded from the US Census Bureau’s [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).


## Processing
Some very limited merging of precincts in the tabular election data and precinct shapefile were necessary to join election results to precinct boundaries. Demographic data were aggregated from the block level using MGGG’s proration software. Congressional and state legislative district IDs were also assigned to precincts using this package.


## Metadata
* `STATE`: State
* `STATEFP`: State FIPS code
* `COUNTY`: County name
* `COUNTYFP`: County FIPS code
* `Precinct`: Precinct name
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate
* `PRES12R`: Number of votes for 2012 Republican presidential candidate
* `GOV12D`: Number of votes for 2012 Democratic gubernatorial candidate
* `GOV12R`: Number of votes for 2012 Republican gubernatorial candidate
*	`USH12D`: Number of votes for 2012 Democratic US House candidate
*	`USH12R`: Number of votes for 2012 Republican US House candidate
* `EC12D`: Number of votes for 2012 Democratic executive council candidate
* `EC12R`: Number of votes for 2012 Republican executive council candidate
* `GOV14D`: Number of votes for 2014 Democratic gubernatorial candidate
* `GOV14R`: Number of votes for 2014 Republican gubernatorial candidate
* `SSEN14D`: Number of votes for 2014 Democratic state senate candidate
*	`SSEN14R`: Number of votes for 2014 Republican state senate candidate
* `EC14D`: Number of votes for 2014 Democratic executive council candidate
* `EC14R`: Number of votes for 2014 Republican executive council candidate
*	`PRES16D`: Number of votes for 2016 Democratic presidential candidate
*	`PRES16R`: Number of votes for 2016 Republican presidential candidate
* `GOV16D`: Number of votes for 2016 Democratic gubernatorial candidate
* `GOV16R`: Number of votes for 2016 Republican gubernatorial candidate
*	`SEN16D`: Number of votes for 2016 Democratic senate candidate
*	`SEN16R`: Number of votes for 2016 Republican senate candidate
*	`USH16D`: Number of votes for 2016 Democratic US House candidate
*	`USH16R`: Number of votes for 2016 Republican US House candidate
* `SSEN16D`: Number of votes for 2016 Democratic state senate candidate
*	`SSEN16R`: Number of votes for 2016 Republican state senate candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `EC20D`: Number of votes for 2020 Democratic executive council candidate
* `EC20R`: Number of votes for 2020 Republican executive council candidate
* `GOV20D`: Number of votes for 2020 Democratic gubernatorial candidate
* `GOV20R`: Number of votes for 2020 Republican gubernatorial candidate
* `PRES20D`: Number of votes for 2020 Democratic presidential candidate
*	`PRES20R`: Number of votes for 2020 Republican presidential candidate
*	`SEN20D`: Number of votes for 2020 Democratic senate candidate
*	`SEN20R`: Number of votes for 2020 Republican senate candidate
*	`USH20D`: Number of votes for 2020 Democratic US House candidate
*	`USH20R`: Number of votes for 2020 Republican US House candidate
* `SSEN20D`: Number of votes for 2020 Democratic state senate candidate
*	`SSEN20R`: Number of votes for 2020 Republican state senate candidate
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
This shapefile uses a UTM projection centered on New Hampshire (ESPG: 3437).

## Rating
We give this shapefile an A rating. All data were obtained from the state government and processing was conducted by a group trained by and working closely with MGGG.
