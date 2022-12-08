# 목적: 파이썬 기본 문법으로 특정 행을 필터링하기
import csv
import datetime


input_file = 'supplier_data.csv'
output_file = 'output_files/3output_basic.csv'

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			# cost = str(row_list[3]).strip('$').replace(',', '')
			cost = str(row_list[3]).strip('$')
			# cost의 가격이 600보다 크고 620보다 작은 행 필더링하는 조건
			# if (float(cost) > 600.00) and (float(cost) < 620.00):
			# 	filewriter.writerow(row_list)

			# 같은 결과의 검색 => Supplier Name열의 값이 Z인 경우
			# if supplier == 'Supplier Z':
			# 	filewriter.writerow(row_list)

			# 복합검색
			#if supplier == 'Supplier Y' and float(cost) < 200.0:
			#	filewriter.writerow(row_list)

			# 날짜 검색
			date_raw =[ int(value) for value in row_list[4].split('/') ]
			current_date = datetime.date(2000+date_raw[2],date_raw[0],date_raw[1])
			start_date_condition = datetime.date(2023,1,30)
			end_date_condition = datetime.date(2023, 2, 3)

			# if (current_date >= start_date_condition) and (current_date <= end_date_condition):
			# 	filewriter.writerow(row_list)

			# end_date_condition = start_date_condition + datetime.timedelta(days=4)
			# if (current_date >= start_date_condition) and (current_date <= end_date_condition):
			# 	filewriter.writerow(row_list)

			# 월요일 데이터 검색
			# date.weekday() 월요일 0 화요일 1 ...
			# if current_date.weekday()==0:
			# 	filewriter.writerow(row_list)

			# 1월 데이터 추출
			# if current_date.month == 1:
			#  	filewriter.writerow(row_list)

			# 2023년 데이터 추출
			# if current_date.year == 2023:
			#  	filewriter.writerow(row_list)

