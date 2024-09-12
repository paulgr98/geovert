# GeoVert

This is a simple Python program that converts Geosense's survey CSV files into XML and XLSX files, which can later be imported into other programs.

## Prerequisites

- Python 3.x
- `pandas` library
- `openpyxl` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/geosense-survey-converter.git
    cd geosense-survey-converter
    ```

2. Install the required libraries:
    ```sh
    pip install pandas openpyxl
    ```

## Usage

You can use this program to convert a single CSV file or all CSV files in a directory.

### Convert a Single CSV File

```sh
python main.py -f path/to/yourfile.csv
```

### Convert a Single CSV File

Run the `main.py` script with the `-f` option followed by the path to your CSV file.

```sh
python main.py -f path/to/yourfile.csv
```

### Convert All CSV Files in a Directory

Run the `main.py` script with the `-d` option followed by the path to your directory containing CSV files.

```sh
python main.py -d path/to/yourdirectory
```

## Example

To convert a single CSV file, use the `-f` option followed by the path to the file.

```sh
python main.py -f data/survey.csv
```

To convert all CSV files in a directory, use the `-d` option followed by the path to the directory.

```sh
python main.py -d data
```

## License

This project is licensed under the MIT License.
