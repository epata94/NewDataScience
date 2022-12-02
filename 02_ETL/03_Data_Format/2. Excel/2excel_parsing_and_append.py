# xlwt 모듈 설치
# 목적: 단일 워크시트 처리

import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'sales_2013_test.xlsx'
output_file = input_file

# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
data_list=[]
sample_row = ['Customer ID', 'Customer Name', 'Invoice Number', 'Sale Amount', 'Purchase Date']
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')

	# for column_index in range(worksheet.ncols):
   	# worksheet.write(worksheet.nrows, column_index,sample_row[column_index])
	worksheet.write(7, 1,'aa')


