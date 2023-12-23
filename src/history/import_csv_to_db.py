import argparse
import os
import sqlite3

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def process_csv_files(csv_files: list[str], is_cleaning: bool = False) -> None:
    """
    Processes a list of CSV files by loading them
    into an SQLite database.
    """
    conn = sqlite3.connect(os.path.join(BASE_DIR, "database.db"))

    for csv_file in csv_files:
        # Get the name of the table from the filename
        table_name = os.path.splitext(csv_file)[0].replace("/", "_")

        # Drop the existing table (if it exists)
        conn.execute(f'DROP TABLE IF EXISTS "{table_name}"')

        if not is_cleaning:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(csv_file)

            # Write the data from your DataFrame into the database
            df.to_sql(table_name, conn, index=False)

    conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Process some CSV files.")
    parser.add_argument("--clean", "-c", action="store_true",
                        help="Drop the tables corresponding to the CSV files")
    parser.add_argument("csv_files", metavar="N", type=str, nargs="+",
                        help="CSV files to be processed")

    args = parser.parse_args()

    process_csv_files(args.csv_files, is_cleaning=args.clean)


if __name__ == "__main__":
    main()
