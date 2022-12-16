# Link to origional repo
https://github.com/mggg-states/VT-shapefiles

# Vermont Election Shapefile
This shapefile was obtained from the Vermont Open Geodata Portal and processed by members of the Metric Geometry and Gerrymandering Group (MGGG).

## Sources
The Vermont town shapefile was downloaded from the [Vermont Open Geodata Portal](http://geodata.vermont.gov/datasets/vt-data-town-boundaries). Election data were downloaded from the Secretary of State’s [website](https://www.sec.state.vt.us/elections/election-results.aspx). Demographic information from the 2010 Decennial Census was downloaded at the sub-county level from [American FactFinder](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml).

## Processing
Demographic and election data were joined to the shapefile using QGIS. Vermont does not release election results for towns with a total population under 50, thus 9 towns have been excluded from this module.

## Metadata
* `STATEFP10`: State FIPS code
* `COUNTYFP10`: County FIPS code
* `COUSUBFP10`: Sub-county FIPS code
* `GEOID10`: Town ID
* `NAME10`: Town name
* `NAMELSAD10`: Town legal and statistical name
* `ALAND10`: Area land in square meters
* `AWATER10`: Area water in square meters
* `INTPTLAT10`: Latitude of internal point
* `INTPTLON10`: Longitude of internal point
* `TOTPOP`: Total population from 2010 Decennial Census
* `WHITE`: White population from 2010 Decennial Census
* `BLACK`: Black population from 2010 Decennial Census
* `AMIN`: American Indian and Alaska Native population from 2010 Decennial Census
* `ASIAN`: Asian population from 2010 Decennial Census
* `NHPI`: Native Hawaiian and Pacific Islander population from 2010 Decennial Census
* `OTHER`: Population of other race from 2010 Decennial Census
* `2MORE`: Population of two or more races from 2010 Decennial Census
* `VAP`:  Population over the age of 18 from 2010 Decennial Census
* `HISP`: Hispanic population from the 2010 Decennial Census
* `SENDIST`: State Senate district ID
* `DISTNAME`: State Senate district name
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `PRES16L`: Number of votes for 2016 Libertarian presidential candidate
* `PRES16G`: Number of votes for 2016 Green Party presidential candidate
* `TOTV16`: Total votes cast in 2016
* `SEN16D`: Number of votes for 2016 Democratic senate candidate
* `SEN16R`: Number of votes for 2016 Republican senate candidate
* `USH14D`: Number of votes for 2014 Democratic US house candidate
* `USH14R`: Number of votes for 2014 Republican US house candidate
* `TOTV14`: Total votes cast in 2014
* `PRES12D`: Number of votes for 2012 Democratic presidential candidate
* `PRES12R`: Number of votes for 2012 Republican presidential candidate
* `PRES12L`: Number of votes for 2012 Libertarian presidential candidate
* `TOTV12`: Total votes cast in 2012
* `SEN12B`: Number of votes for Bernie Sanders in 2012 senate race
* `SEN12R`: Number of votes for 2012 Republican senate candidate
* `USH12D`: Number of votes for 2012 Democratic US house candidate
* `USH12R`: Number of votes for 2012 Republican US house candidate

## Rating
We give this shapefile an A rating. All data was obtained from the state government and was processed by MGGG staff.
