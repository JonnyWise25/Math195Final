# Link to origional repo
https://github.com/mggg-states/UT-shapefiles

# Utah Election Shapefile
This shapefile was obtained from the Utah Automated Geographic Reference Center (AGRC) and processed by members of the Metric Geometry and Gerrymandering Group (MGGG) with assistance from the reform group [Better Boundaries](https://betterboundaries.org) and members of the Brigham Young University Mathematics Department.

## Sources
The Utah precinct shapefiles come from the [Utah AGRC](https://gis.utah.gov/data/political/voter-precincts) and the voting tabulation districts from the [US Census Bureau’s TIGER/Line program](https://www.census.gov/cgi-bin/geo/shapefiles/index.php). Shapefiles for Utah’s congressional, house, and senate districts were also obtained from the [Utah AGRC](https://gis.utah.gov/data/political/2012-2021-house-senate-congressional-districts/). Election data come from the [MIT Election Data Science Lab](https://github.com/MEDSL/official-precinct-returns).  Demographic data were downloaded at the census block level from [IPUMS NHGIS](https://www.nhgis.org).

## Processing
The topology of the precinct shapefile was repaired using the st_make_valid() function from the R package [lwgeom](https://github.com/r-spatial/lwgeom). Sub-precincts in the shapefile were merged to match the precinct IDs in the election results. Demographic data were aggregated from the block level using [MGGG’s proration software](https://github.com/mggg/maup). Congressional, house, and senate district IDs were assigned to precincts also using this package.

## Metadata
* `CountyID`: County ID
* `VistaID`: Precinct name and sub-precinct number
* `PrcncID`: Precinct name
* `SbPrcnc`: Sub-precinct number
* `AliasNm`: Municipality name (where applicable)
* `DsslvID`: Precinct unique identifier
* `cnty_nm`: County name
* `cnty_fp`: County FIPs code
* `jrsdctn`: Jurisdiction name
* `PRES16D`: Number of votes for 2016 Democratic presidential candidate
* `PRES16R`: Number of votes for 2016 Republican presidential candidate
* `PRES16I`: Number of votes for 2016 Independent presidential candidate (Evan McMullin)
* `SEN16D`: Number of votes for 2016 Democratic senate candidate
* `SEN16R`: Number of votes for 2016 Republican senate candidate
* `GOV16D`: Number of votes for 2016 Democratic gubernatorial candidate
* `GOV16R`:  Number of votes for 2016 Republican gubernatorial candidate
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
* `CD`: US congressional district ID
* `SENDIST`: State Senate district ID
* `HDIST`: State House district ID

## Projection
This shapefile uses a NAD83/UTM zone 12 North projection (EPSG:26912).

## Rating
We give this shapefile an B rating. Precinct level election data did not neatly correspond to the precinct shapefile and some merging of precincts had to be performed in order to join the two files.
