# 목적: 기본 파이썬 csv 모듈을 활용하여 csv 파일 읽고 쓰기 (단순 복사)
import csv

input_file = 'supplier_data_org.csv'
output_file = 'output_files/2output_index_false.csv'

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		filewriter = csv.writer(csv_out_file, delimiter=',')
		for row_list in filereader:
			filewriter.writerow(row_list)