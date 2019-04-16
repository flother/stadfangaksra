# Staðfangaskrá: Iceland's street addresses

[![Download latest CSV](https://img.shields.io/badge/CSV-Download-brightgreen.svg)](https://raw.githubusercontent.com/flother/stadfangaskra/master/stadfangaskra.csv)

This is a copy of the official database of Icelandic street addresses, [Staðfangaskrá](https://opingogn.is/dataset/stadfangaskra), stored in a more usable format. Specifically:

- The data's available over HTTP, not FTP
- The data's available to download as a CSV file, not a CSV file within a ZIP file
- The fields in the CSV file are comma-separated, not pipe-separated
- The numeric coordinates are stored using "." for decimal points, not ","

The data is otherwise left untouched.

Each day, at [01:00 UTC](https://time.is/0100_UTC), the [source file](ftp://ftp.skra.is/skra/STADFANG.dsv.zip) is checked for updates. If it's been updated, the new data is saved to this repository. You can then see the [changes to the database over time](https://github.com/flother/stadfangaskra/commits/master/stadfangaskra.csv) by using this repo's Git commit history.

You can [download the latest CSV file](https://raw.githubusercontent.com/flother/stadfangaskra/master/stadfangaskra.csv) directly from GitHub.

The source data is provided by [Þjóðskrá Íslands](https://www.skra.is/), the national agency resposible for Iceland's property register. It's licensed under the [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/).
