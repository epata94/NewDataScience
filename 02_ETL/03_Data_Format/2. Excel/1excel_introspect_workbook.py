# xlrd 모듈 설치
# 목적: 엑셀 기본 정보 확인
import sys
from xlrd import open_workbook

input_file = sys.argv[1] #sales_2013.xlsx

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
	print("Worksheet name:", worksheet.name, "\tRows:", \
			worksheet.nrows, "\tColumns:", worksheet.ncols)
