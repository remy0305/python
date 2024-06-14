from openpyxl import load_workbook
import win32com.client as win32
import os
# Create an Excel application object
excel = win32.Dispatch('Excel.Application')
excel.Visible = False

# Open the Excel workbook
workbook = excel.Workbooks.Open(os.getcwd() + '/' + '51215105-2.xlsx')
sheet = workbook.Sheets(1)

# Set print gridlines
sheet.PageSetup.PrintGridlines = True
# Export the worksheet as PDF
pdf_path = os.getcwd() + '/' + '51215105-4.pdf'
workbook.ExportAsFixedFormat(0, pdf_path)

# Close the workbook and quit Excel
workbook.Close(False)
excel.Quit()