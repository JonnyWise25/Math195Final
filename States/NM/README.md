# Link to origional repo
https://github.com/mggg-states/NM-shapefiles

# New Mexico Election Shapefile
New Mexico precinct shapefiles with election results from 2016 and 2018

## Data Sources

The New Mexico precinct shapefile was obtained from the New Mexico [Resource Geographic Information System (RGIS)](http://rgis.unm.edu/rgis6/) , which is managed by the Earth Data Analysis Center (EDAC) at the University of New Mexico. It was processed by members of the Metric Geometry and Gerrymandering Group (MGGG).

The Congressional, State Senate and State House district map shape files, as well as the 2010 census block shape file are from the [US Census Bureau's TIGER/Line Program](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

Precint level elections returns were provided by the  [New Mexico Secretary of State's](https://www.sos.state.nm.us/voting-and-elections/election-results/past-election-results-2018/) website. Block level demographic data is from the Census API.

## Processing

Statewide election returns from 2016 and 2018 - from the New Mexico Secretary of State - were cleaned by MGGG staff in order to join it with the New Mexico precinct shapefile. Census block data was aggregated to the precinct level using MGGG's [proration software](https://github.com/mggg/maup).

### Metadata ###

* `NAME10`: Name of precinct
* `Prec_num`: Precinct number
*	`County`: Precinct county
*	`AG18D`: Number of votes for the 2018 Democratic Attorney General candidate
*	`AG18R`: Number of votes for the 2018 Republican Attorney General candidate
*	`AG18L`: Number of votes for the 2018 Libertarian Attorney General candidate
*	`SOS18D`: Number of votes for the 2018 Democratic Secretary of State candidate
*	`SOS18R`: Number of votes for the 2018 Republican Secretary of State candidate
*	`SOS18L`: Number of votes for the 2018 Libertarian Secretary of State candidate
*	`SEN18D`: Number of votes for the 2018 Democratic Senate candidate
*	`SEN18R`: Number of votes for the 2018 Republican Senate candidate
*	`SEN18L`: Number of votes for the 2018 Libertarian Senate candidate
*	`GOV18D`: Number of votes for the 2018 Democratic Governor candidate
*	`GOV18R`: Number of votes for the 2018 Republican Governor candidate
*	`PRES16D`: Number of votes for the 2016 Democratic Presidential candidate
*	`PRES16R`: Number of votes for the 2016 Republican Presidential candidate
*	`PRES16L`: Number of votes for the 2016 Libertarian Presidential candidate
*	`SOS16D`: Number of votes for the 2016 Democratic Secretary of State candidate
*	`SOS16R`: Number of votes for the 2016 Republican Secretary of State candidate
*	`CDDIST`: 2011 enacted US congressional district ID
*	`HDIST`: 2011 enacted State House district ID
*	`SDIST`: 2011 enacted State Senate district ID
*	`Area`: Area of precinct in square meters
*	`Perimeter`: Perimeter of precinct in meters
*	`TOTPOP`: Total population
*	`NH_WHITE`: White, non-hispanic, population
*	`NH_BLACK`: Black, non-hispanic, population
*	`NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
*	`NH_ASIAN`: Asian, non-hispanic, population
*	`NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
*	`NH_OTHER`: Other race, non-hispanic, population
*	`HISP`: Hispanic population
*	`H_WHITE`: White, hispanic, population
*	`H_BLACK`: Black, hispanic, population
*	`H_AMIN`: American Indian and Alaska Native, hispanic, population
*	`H_ASIAN`: Asian, hispanic, population
*	`H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
*	`H_OTHER`: Other race, hispanic, population
*	`VAP`: Total voting age population
*	`HVAP`: Hispanic voting age population
*	`WVAP`: White, non-hispanic, voting age population
*	`BVAP`: Black, non-hispanic, voting age population
*	`AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
*	`ASIANVAP`: Asian, non-hispanic, voting age population
*	`NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
*	`OTHERVAP`: Other race, non-hispanic, voting age population
*	`2MOREVAP`: Two or more races, non-hispanic, voting age population

## Projection
This shapefile uses a WGS84/UTM zone 13N projection (EPSG: 32613).

## Rating
We give these shapefiles an A rating. All data was obtained from the state government and was processed by MGGG staff.
