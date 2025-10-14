import csv
import os


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

def delete_csv_row_by_id(file_path: str, target_id: int):
    """Deletes a row from a CSV file where the first column matches target_id."""
    temp_path = file_path + ".tmp"

    with open(file_path, mode="r", newline="", encoding="utf-8") as infile, \
         open(temp_path, mode="w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Skip empty rows
            if not row:
                continue

            # If this row matches the ID, skip writing it (deletes it)
            try:
                if int(row[0]) == target_id:
                    continue
            except ValueError:
                # If first column is not an integer (e.g., header), keep it
                pass

            # Write all other rows
            writer.writerow(row)

    # Replace original file with the updated one
    os.replace(temp_path, file_path)