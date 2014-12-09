census-block-toolchain
======================

Scripts and methods that I used to convert the Population & Housing Unit Counts by Census Block shapefiles from the 2010 US Census to GeoJSON per County (as the file for the entire state was a bit unwieldy).

1. Get the source data from https://www.census.gov/geo/maps-data/data/tiger-data.html under Population & Housing Unit Counts -- Blocks
2. Unzip the census file. For Wisconsin that's tabblock2010_55_pophu.zip.
3. Convert from shapefile to geojson: ogr2ogr -nln "Wisconsin Census Blocks" -f GeoJSON -t_srs crs:84 -s_srs crs:84 wi.geojson tabblock2010_55_pophu.shp
4. Make scratch directory: mkdir blocksout
5. Generate geojson by county: ./split-geojson-cblocks-by-count.py -o blocksout wi.geojson
