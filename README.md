This is a copy of the official Icelandic street address registry, [Staðfangaskrá](https://opingogn.is/dataset/stadfangaskra), but stored in a more usable format. Specifically:

- It's available over HTTP, not FTP
- It's available to download as a CSV file, not a CSV file within a ZIP file
- The fields in the CSV file are comma-separated, not pipe-separated
- The numeric coordinates are stored using "." for decimal points, not ","

The file is updated daily at [01:00 UTC](https://time.is/0100_UTC). Changes are tracked over time using the repo's Git commit history. You can see a list of the recent changes to the CSV file at https://github.com/flother/stadfangaskra/commits/master/stadfangaskra.csv.

The source data is provided by [Þjóðskrá Íslands](https://www.skra.is/) and is licensed under the [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/).
