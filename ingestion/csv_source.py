import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fetch_csv_data(path="data/data.csv"):
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, newline="") as f:
        return list(csv.DictReader(f))


def fetch_csv2_data(path="data/data2.csv"):
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, newline="") as f:
        return list(csv.DictReader(f))
