import csv
import io
import sys
import urllib.request
import zipfile


def make_coord(v):
    return float(v.replace(",", "."))


def output_addresses_csv():
    output = None
    response = urllib.request.urlopen("ftp://ftp.skra.is/skra/STADFANG.dsv.zip")
    zf = zipfile.ZipFile(io.BytesIO(response.read()))
    with zf.open("STADFANG.dsv") as fh:
        rows = csv.DictReader(io.TextIOWrapper(fh), delimiter="|")
        for row in rows:
            if output is None:
                output = csv.DictWriter(
                    sys.stdout,
                    fieldnames=[k for k in row.keys() if k != "DAGS_UTGAFA"],
                )
                output.writeheader()
            row["X_ISN93"] = make_coord(row["X_ISN93"])
            row["Y_ISN93"] = make_coord(row["Y_ISN93"])
            row["LAT_WGS84"] = make_coord(row["LAT_WGS84"])
            row["LONG_WGS84"] = make_coord(row["LONG_WGS84"])
            del row["DAGS_UTGAFA"]
            output.writerow(row)
