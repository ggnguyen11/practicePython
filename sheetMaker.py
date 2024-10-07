# this program populates an excel spreadsheet with given inputs, w/ openpyxl
# library for Excel (.xlsx) or built-in package csv for CSV files

import openpyxl

# creates new excel file
workbook = openpyxl.Workbook()
sheet = workbook.active

# writes data to sheet
#sheet.append(data)

# saves workbook
workbook.save('test_sheetMaker.xlsx')

