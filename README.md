# Staðfangaskrá: Iceland's street addresses

[![Download latest CSV](https://img.shields.io/badge/CSV-Download-brightgreen.svg)](https://raw.githubusercontent.com/flother/stadfangaskra/master/stadfangaskra.csv)

This is a copy of the official database of Icelandic street addresses, [Staðfangaskrá](https://opingogn.is/dataset/stadfangaskra), stored in a more usable format. Specifically:

- The data's available over HTTP, not FTP
- The data's available to download as a CSV file, not a CSV file within a ZIP file
- The fields in the CSV file are comma-separated, not pipe-separated
- The date fields are stored in `YYYY-MM-DD` format, not `DD.MM.YYYY`
- The numeric coordinates are stored using "." for decimal points, not ","

On top of these improvements, the `DAGS_UTGAFA` (date published) column is removed; its value — the current date — is identical for each row and can of course be recovered using the commit date. The data is otherwise left untouched.

The source data is updated once a week, on Sundays at 21:00, and so at [22:00 UTC](https://time.is/2200_UTC) every Sunday the [source file](ftp://ftp.skra.is/skra/STADFANG.dsv.zip) is checked for updates. The new data is then saved to this repository. You can then see the [changes to the database over time](https://github.com/flother/stadfangaskra/commits/master/stadfangaskra.csv) by using this repo's Git commit history.

You can [download the latest CSV file](https://raw.githubusercontent.com/flother/stadfangaskra/master/stadfangaskra.csv) directly from GitHub. You can convert the data from CSV to GeoJSON using [GDAL/OGR](https://www.gdal.org/):

```sh
$ ogr2ogr \
   -f GeoJSON \
   -oo X_POSSIBLE_NAMES=LONG_WGS84 \
   -oo Y_POSSIBLE_NAMES=LAT_WGS84 \
   -oo KEEP_GEOM_COLUMNS=NO \
   -lco RFC7946=YES \
   -lco WRITE_NAME=NO \
   stadfangaskra.geojson \
   /vsicurl_streaming/https://raw.githubusercontent.com/flother/stadfangaskra/master/stadfangaskra.csv
```

The source data is provided by [Þjóðskrá Íslands](https://www.skra.is/), the national agency responsible for Iceland's property register. It's licensed under the [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/).
