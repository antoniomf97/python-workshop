"""
Python Libraries - Excel

https://openpyxl.readthedocs.io/en/stable/
"""

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="text_excel.xlsx")


# https://realpython.com/openpyxl-excel-spreadsheets-python/