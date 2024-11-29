# this program populates an excel spreadsheet with given inputs, w/ openpyxl
# library for Excel (.xlsx) or built-in package csv for CSV files

import openpyxl

# creates new excel file
workbook = openpyxl.Workbook()
sheet = workbook.active

# writes data to sheet
#sheet.append(data)

# function to name workbook object
def name_sheet():
    while True:
        workbook_name = input("\nEnter spreadsheet name:\n")
        confirmation = input(f'\nIs this correct?' + \
            f' (Enter Y/N)\n{workbook_name}.xlsx\n')
        if confirmation.lower() == 'y' or confirmation[0] == 'y':
            break
    return workbook_name

# assigns function return value to global variable
workbook_name = name_sheet()

# saves workbook with .xlsx file extension
workbook.save(f'{workbook_name}.xlsx')