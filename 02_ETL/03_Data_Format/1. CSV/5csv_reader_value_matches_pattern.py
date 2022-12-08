# 목적: 패턴/정규 표현식을 활용한 필터링
import csv
import re
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/5output_basic.csv'

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
# pattern = re.compile(r'(^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			invoice_number = row_list[1]
			if pattern.search(invoice_number):
				filewriter.writerow(row_list)