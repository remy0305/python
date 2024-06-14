from win32com.client import Dispatch
import os

start=int(input("start="))
goal=int(input("final="))
app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Add()
sheet = xlsx.Worksheets(1)

for i in range(1,10):
    for j in range(1,10):
        sheet.Cells(i, j).Value = ()

for i in range(1, start+1):
    for j in range(1,goal+1):
        str1 = [0] * 5  # 將 str1 初始化為列表
        str1[0] = i
        str1[1] = "*"
        str1[2] = j
        str1[3] = "="
        str1[4] = i * j
        # 將 str1 作為字符串賦值給單元格
        sheet.Cells(i, j).Value = ''.join(map(str, str1))

xlsx.SaveAs("./9.xlsx")
xlsx.Close(False)
app.Quit()
