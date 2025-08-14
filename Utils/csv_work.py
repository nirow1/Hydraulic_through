import csv

def change_csv_status(path: str, row: int, column: int):
    with open(path, mode="r+", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

        for i, row_data in enumerate(data):
            if row_data and i == row:
                row_data[column] = "1"

        # Move back to the beginning of the file and overwrite with modified data
        f.seek(0)
        writer = csv.writer(f)
        writer.writerows(data)
        f.truncate()

def extract_data_from_csv(path):
    with open(path, mode="r", newline="") as f:
        reader = csv.reader(f)
        return list(reader)