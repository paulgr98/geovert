import argparse
import os

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="This is simple Python program that can convert Geosense's survey "
                                                 "CSV file into XML and XLSX files, that can later be imported into "
                                                 "other programs.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="input CSV file")
    group.add_argument("-d", "--directory", help="input directory with CSV files")
    parser.add_argument('positional_file', nargs='?', help="input file (default)")

    args = parser.parse_args()

    if args.directory:
        process_directory(args.directory)
    else:
        file_path = args.positional_file or args.file
        process_file(file_path)


def process_file(file_path):
    if file_path is None:
        print("File path is empty.")
    if not validate_file_extension(file_path):
        print("Invalid file extension. Expected .csv file.")
    data_frame = get_data_frame(file_path)
    output_file_path = get_output_file_path(file_path)
    export_to_xlsx(data_frame, output_file_path)


def validate_file_extension(file_path):
    return file_path.endswith(".csv")


def get_data_frame(file_path):
    header_line_number = get_header_line_number(file_path)
    if header_line_number == -1:
        print("Cannot find headers in the CSV file.")
        return None
    try:
        df = read_csv_file(file_path, header_line_number)
        df = adjust_headers(df)
        df = drop_last_column(df)
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_csv_file(file_path, header_line_number):
    with open(file_path, 'r') as file:
        return pd.read_csv(file, header=header_line_number)


def adjust_headers(df):
    new_columns = df.columns[1:].tolist() + ['temp']
    df.columns = new_columns
    return df


def get_header_line_number(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if line.startswith("ID"):
                return i
    return -1


def drop_last_column(df):
    return df.iloc[:, :-1]


def get_output_file_path(file_path):
    file_name = extract_file_name(file_path)
    output_directory = create_output_directory(file_path)
    return construct_output_file_path(output_directory, file_name)


def extract_file_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def create_output_directory(file_path):
    output_dir_name = "out"
    output_directory = os.path.join(os.path.dirname(file_path), output_dir_name)
    os.makedirs(output_directory, exist_ok=True)
    return output_directory


def construct_output_file_path(output_directory, file_name):
    return os.path.join(output_directory, f"{file_name}.xlsx")


def export_to_xlsx(df, output_file_path):
    df.to_excel(output_file_path, index=False)


def process_directory(directory_path):
    get_all_csv_files(directory_path)
    for file_path in get_all_csv_files(directory_path):
        process_file(file_path)


def get_all_csv_files(directory_path):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".csv"):
                file_paths.append(os.path.join(root, file))
    return file_paths


if __name__ == "__main__":
    try:
        main()
        print("Program finished successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
