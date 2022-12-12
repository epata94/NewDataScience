# 목적: 여러 개의 통합 문서 합치기
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = '.'
output_file = 'output_files/13output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')

data = []
first_worksheet = True
# 전체 Excel 파일을 처리하기 위한 For문
for input_file in glob.glob(os.path.join(input_folder, '*.xls')):
	print(os.path.basename(input_file))
	with open_workbook(input_file) as workbook:
		# 전체 Worksheet를 처리하기 위한 for문
		for worksheet in workbook.sheets():
			if first_worksheet:
				header_row = worksheet.row_values(0)
				data.append(header_row)
				first_worksheet = False
			# 전체 행을 처리하기 위한 for문
			for row_index in range(1,worksheet.nrows):
				row_list = []
				# 전체 열을 처리하기 위한 for문
				for column_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value,workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
				data.append(row_list)

for list_index, output_list in enumerate(data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)