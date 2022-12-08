# xlwt 모듈 설치
# 목적: 단일 워크시트 처리

import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/2output_basic.xls'

# Workbook() 새로 쓰고자 하는 워크북생성
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# output_worksheet = output_workbook.add_sheet('january_2015')

with open_workbook(input_file) as workbook:
	# sheet_by_name([시트이름]) 워크북안에 있는 특정 워크시트를 반환
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows):
		for column_index in range(worksheet.ncols):
			#write([행번호],[열번호],[쓰고자하는 데이터값])
			# cell_value([행번호],[열번호]) : 행번호, 열번호에 매치가 되는 셀의 값을 반환
			output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)