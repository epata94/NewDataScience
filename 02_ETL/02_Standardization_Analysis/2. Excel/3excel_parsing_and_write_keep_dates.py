# 목적: 날짜 형식 할당
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')


with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows):
		row_list_output = []
		for col_index in range(worksheet.ncols):
			# cell_type의 반환값이 3인 경우는 날짜 타입
			if worksheet.cell_type(row_index, col_index) == 3:
				date_cell = xldate_as_tuple(worksheet.cell_value\
					(row_index, col_index),workbook.datemode)
				# date_cell = date(*date_cell[0:3]).strftime\
				date_cell = date(*date_cell[0:3]).strftime \
					('%m/%d/%Y')
				# 연습으로 원본과 똑같은 형태의 날짜도 저장할 것
				row_list_output.append(date_cell)
				output_worksheet.write(row_index, col_index, date_cell)
			else:
				non_date_cell = worksheet.cell_value\
					(row_index,col_index)
				row_list_output.append(non_date_cell)
				output_worksheet.write(row_index, col_index,\
					non_date_cell)
output_workbook.save(output_file)