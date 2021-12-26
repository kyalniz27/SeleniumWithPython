import openpyxl

path = "C://Users//seker//eclipse-workspace//SeleniumPractice//excel//data.xlsx"
workbook = openpyxl.load_workbook(path)
# 1. Get the sheet from Excel file
#sheet = workbook.active
# 2. Second way of getting the sheet from Excel
sheet = workbook['Sheet2']

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row = r, column = c).value = "Welcome"

workbook.save(path)
