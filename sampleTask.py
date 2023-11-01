import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

data = [["Name", "Age"], ["Kalyan", 35]]

for row in data:
    worksheet.append(row)
workbook.save("example.xlsx")



