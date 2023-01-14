"""
Python Libraries - Excel

https://openpyxl.readthedocs.io/en/stable/
https://realpython.com/openpyxl-excel-spreadsheets-python/
"""

# from openpyxl import Workbook, load_workbook

# workbook = Workbook()
# sheet = workbook.active

# sheet["A1"] = "First"
# sheet["B1"] = "Second"
# sheet["C10"] = "Third"

# workbook.save(filename="./files/test_excel.xlsx")


# workbook = load_workbook(filename="./files/test_excel.xlsx")
# print(workbook.sheetnames)

# sheet = workbook.active
# print(sheet["C10"].value)

# print(sheet["A1:C10"])
# print()

# new_sheet = workbook.create_sheet("New Sheet")
# current = workbook["New Sheet"]

# current["A1"] = "New Stuff"
# current["B5"] = 10
# current["B6"] = 11

# values = [1, 2, 3, 4, 5, 6, 7, 8]
# for i, c in enumerate(current["C1":"C8"]):
#     c[0].value = values[i]
    

# workbook.save(filename="./files/test_excel.xlsx")