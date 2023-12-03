import csv


def CSV_dict_parser(csv_path: str, encoding: str = "utf-8-sig", newline: str = ''):
    """decode StableDiffusion style.csv (CSV Dict type)"""
    with open(csv_path, mode="r", newline=newline, encoding=encoding) as CSV_file:
        return [csv_row for csv_row in csv.DictReader(CSV_file, skipinitialspace=True)]


if __name__ == '__main__':
    CSV_dict_parser("../static/styles.csv")
