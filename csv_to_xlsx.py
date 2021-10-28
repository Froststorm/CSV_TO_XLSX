import csv
from os import sep
import openpyxl
import sys

# from time import sleep
from alive_progress import alive_bar


def csv_to_excel(csv_file, excel_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    with open(csv_file, encoding="utf-8") as file_obj:
        reader = csv.reader(file_obj, delimiter=";")
        rows = list(reader)
        pbar = len(rows)
        # print(pbar)
        with alive_bar(pbar) as bar:
            for row in rows:
                # row = "".join(row).split(";")
                # print(row)
                sheet.append(row)
                bar()
                # sleep(.1)
            workbook.save(excel_file)


if __name__ == "__main__":
    csv_ = sys.argv[1]
    xlsx_ = sys.argv[2]
    csv_to_excel(csv_, xlsx_)
