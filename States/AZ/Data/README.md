# Link to origional repo
https://github.com/mggg-states/AZ-shapefiles

# Arizona Election Shapefiles
This shapefile was obtained from Garret Archer, Data Analyst with the Arizona Secretary of State, and processed by members of the Metric Geometry and Gerrymandering Group (MGGG).

## Sources
The precinct shapefile is made available on [Kaggle](https://www.kaggle.com/azsecretaryofstate/arizona-statewide-precinct-shapefile?select=az_vtd_2018_new_pima.shp) by Garret Archer, formerly Senior Elections Analyst with the Arizona Secratary of State and currently a Data Analyst with ABC15 Arizona. Tabular election data are from the [MIT Election Data Science Lab](https://electionlab.mit.edu). Block level demographic data for the 2010 Decennial Census were retrieved using the [Census API](https://api.census.gov/data/2010/dec/sf1).

## Processing
Some very limited merging of precincts in the original shapefile was necessary to join election results. La Paz County precincts were edited to match data provided on the county's [election website](http://www.co.la-paz.az.us/DocumentCenter/View/76/Precinct-Map-PDF). Demographic data were aggregated from the block level using MGGG’s [proration software](https://github.com/mggg/maup). Congressional and state legislative district IDs were assigned to precincts also using this package.

## Metadata
* `COUNTY`: County name
* `CNTYABV`: County abbreviations
* `CODE`: Precinct code
* `PRECINCT`: Precinct
* `PCTNAME`: Precinct name
* `AG18D`: Number of votes for 2018 Democratic attorney general candidate
* `AG18R`: Number of votes for 2018 Republican attorney general candidate
* `GOV18D`: Number of votes for 2018 Democratic gubernatorial candidate
* `GOV18R`: Number of votes for 2018 Republican gubernatorial candidate
* `SOS18D`: Number of votes for 2018 Democratic secretary of state candidate
* `SOS18R`: Number of votes for 2018 Republican secretary of state candidate
* `SSEN18D`: Number of votes for 2018 Democratic state senate candidates
* `SSEN18R`: Number of votes for 2018 Republican state senate candidates
* `TRE18D`: Number of votes for 2018 Democratic treasurer candidate
* `TRE18R`: Number of votes for 2018 Republican treasurer candidate
* `USH18D`: Number of votes for 2018 Democratic US house candidates
* `USH18R`: Number of votes for 2018 Republican US house candidates
* `USH18G`: Number of votes for 2018 Green Party US house candidate
* `SEN18D`: Number of votes for 2018 Democratic senate candidate
* `SEN18R`: Number of votes for 2018 Republican senate candidate
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
This shapefile uses a NAD83/Arizona Central (ft) projection (EPSG:2223).

## Rating
We give these shapefiles an A rating. All data was obtained from the state government and was processed by MGGG staff.
