# 목적: 열의 인덱스 값을 사용하여 특정 열을 선택하기
import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/6output_basic.csv'

# 열의 index를 의미한다.
my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# 열 필터링할 때는 헤더행을 읽을 필요가 없다.
		for row_list in filereader:
			row_list_output = [ ]
			# row_list_output = ['Supplier X','$500.00']
			for index_value in my_columns:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)