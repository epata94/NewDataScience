# 목적: 분산데이터 병합
import csv
import glob
import os
import sys

input_path = '.'
output_file = 'output_files/9output_basic.csv'
 
first_file = True # 플래그 변수
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='') as csv_in_file:
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row)