# 목적: 헤더 추가하기
import csv
import sys

input_file = 'supplier_data_no_header_row.csv'
output_file = 'output_files/12output_basic.csv'

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header_list = ['Supplier Name', 'Invoice Number', \
					   'Part Number', 'Cost', 'Purchase Date']
		filewriter.writerow(header_list)
		for row in filereader:
			filewriter.writerow (row)