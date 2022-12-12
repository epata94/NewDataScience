# 목적: 특정 집합의 값을 포함하는 행의 필터링
import csv
import sys

input_file = sys.argv[1] # supplier_data_org.csv
output_file = sys.argv[2] # output_files/4output_basic.csv

# 한개의 열에서 필터링하는 조건이 2가지 이상일 때
important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			a_date = row_list[4]
			if a_date in important_dates:
				filewriter.writerow(row_list)