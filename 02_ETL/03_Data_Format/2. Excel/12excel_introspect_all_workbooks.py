# 목적: 분산 환경의 엑셀 파일 처리
import glob
import os
import sys
from xlrd import open_workbook

input_directory = '.'

workbook_counter = 0
# 현재 디렉토리를 기준으로 해서 모든 xls 파일에 대하여 처리
for input_file in glob.glob(os.path.join(input_directory, '*.xls')):
	workbook = open_workbook(input_file)
	# input_file ex) '.\\sales_2013.xls'
	# os.path.basename: 전체 경로에서 파일이름만 반환
	print('Workbook: {}'.format(os.path.basename(input_file)))
	print('Number of worksheets: {}'.format(workbook.nsheets))
	for worksheet in workbook.sheets():
		print('Worksheet name:', worksheet.name, '\t\tRows:',\
				worksheet.nrows, '\t\tColumns:', worksheet.ncols)
	workbook_counter += 1
print('Number of Excel workbooks: {}'.format(workbook_counter))