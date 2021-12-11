from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "nadosheet" #워크 시트 이름 변경
wb.save("sample.xlsx")
wb.close()