from Utils.csv_work import extract_data_from_csv
from datetime import datetime



def find_latest_row(data):
    latest_time = datetime.min
    latest_row = None

    for record in data:
        if not record or not record[-1]:  # skip empty rows or missing timestamps
            continue
        try:
            row_time = datetime.fromisoformat(record[-1])
            if row_time > latest_time:
                latest_time = row_time
                latest_row = record
        except ValueError:
            # skip malformed timestamp strings
            continue
    return latest_row


def find_current_photogrammetry_row(row_id):
    database = extract_data_from_csv("./App_data/Test_plan/planned_photogrammetry.csv")
    for row in database:
        if row[0] == row_id:
            return row