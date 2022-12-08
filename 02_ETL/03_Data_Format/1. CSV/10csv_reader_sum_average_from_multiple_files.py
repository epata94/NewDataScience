# 목적: 분산데이터 값의 통계값 구하는 메카니즘 이해
import csv
import glob
import os
import string
import sys

input_path = '.'
output_file = 'output_files/10output_basic.csv'

output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		output_list = [ ]
		output_list.append(os.path.basename(input_file))
		header = next(filereader)
		total_sales = 0.0
		# 평균을 구하기 위해 전체 Sale Amount 행 갯수를 파악하기 위한 변수
		number_of_sales = 0.0
		for row in filereader:
			sale_amount = row[3]
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			number_of_sales += 1.0
		average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
		output_list.append(total_sales)
		output_list.append(average_sales)
		filewriter.writerow(output_list)
csv_out_file.close()
