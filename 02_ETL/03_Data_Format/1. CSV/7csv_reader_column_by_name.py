# 목적: 열의 헤더명을 사용하여 특정 열을 선택하기
# 열의 헤더명으로 검색하는 것은 새로운 열이 추가 및 삭제되었을 경우에
# 기존의 프로그램의 수정을 최소화 하기위해서 필요하다.
import csv
import sys

input_file = 'supplier_data_org.csv'
output_file = 'output_files/7output_basic.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# Step1] 헤더행을 읽는다.
		header = next(filereader)
		# Step2]
		# 필터링할 열의 인덱스를 찾기 위해서 헤더 열의 값을
		# for문을 돌면서 검색용 열의 인덱스 번호를 찾는다.
		for index_value in range(len(header)):
			if header[index_value] in my_columns:
				my_columns_index.append(index_value)
		filewriter.writerow(my_columns)
		# Step3] 인덱스 번호를 기반으로 원하는 열의 모든 데이터를 추출한다.
		for row_list in filereader:
			row_list_output = [ ]
			for index_value in my_columns_index:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)