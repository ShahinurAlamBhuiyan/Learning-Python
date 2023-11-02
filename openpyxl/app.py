# go to pypi.org
# search for openpyxl
# copy the command and paste in the terminal.


# check the packages -->
# External Libraries -> site-pakages -> openpyxl


import openpyxl as xl
from openpyxl.chart import BarChart, Reference  # calling chart


def process_workbook(filename):
    wb = xl.load_workbook(filename)  # access of xl file
    sheet = wb['Sheet1']  # sheet name
    cell = sheet['a1']  # individual column . || cell = sheet.cell(1, 1)
    # print(cell.value)  # transaction_id

    # print(sheet.max_row)  # 4. getting how many row in the sheet

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row, 3)
        corrected_price = cell.value * 0.9
        corrected_price_cell = sheet.cell(row, 4)  # add cell
        corrected_price_cell.value = corrected_price  # adding cell value

    values = Reference(sheet, min_row=2, max_row=sheet.max_row, min_col=4, max_col=4)

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'e2')
    wb.save(filename)


process_workbook('transactions.xlsx')
