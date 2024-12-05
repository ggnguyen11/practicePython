# this program populates an excel spreadsheet with given inputs, w/ openpyxl
# library for Excel (.xlsx) or built-in package csv for CSV files

import openpyxl
# documentation @ https://openpyxl.readthedocs.io/en/stable/

# creates new excel file w/ workbook object
workbook = openpyxl.Workbook()
sheet_one = workbook.active

# writes data to sheet
def modify_sheet(sheet):
    print("\nWhat data would you like to populate your sheet with?\n")
    file = input('Enter file to append from (.txt | .csv | etc.):\n')
# pointer variable for starting cell
    count = 2
    with open(file, 'r') as f:
        fline = f.readline()
        while fline:
# tests for separator in line of data
            if ' , ' in fline:
# split returns list using provided separator
                fline = fline.split(' , ')
            else:
                pass
# populates first column row-by-row w/ elements from given list
            col = input('\nEnter the column letter to populate (A-Z):\n')
            for i in fline:
                sheet[f'{col}{count}'] = i
                count += 1
#            sheet.append(fline)
            fline = f.readline()
    return sheet

# function to name workbook object
def name_sheet():
    while True:
        workbook_name = input('\nEnter spreadsheet name:\n')
        confirmation = input(f'\nIs this correct?' + \
            f' (Enter Y/N)\n{workbook_name}.xlsx\n')
        if confirmation[0].lower() == 'y':
            print(f'\nFile saved as {workbook_name}.xlsx.')
            break
    return workbook_name

# call to modify function
sheet_one = modify_sheet(sheet_one)

# assigns function return value to global variable
workbook_name = name_sheet()

# saves workbook as .xlsx file
workbook.save(f'{workbook_name}.xlsx')