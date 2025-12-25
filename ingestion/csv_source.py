import csv

def fetch_csv_data(path="data.csv"):
    with open(path) as f:
        return list(csv.DictReader(f))

def fetch_csv2_data(path="data2.csv"):
    with open(path) as f:
        return list(csv.DictReader(f))
