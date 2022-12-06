# 목적: CSV 파일 읽고 쓰기
input_file = 'supplier_data.csv'
output_file = 'output_files/1output_index_false.csv'

# with open(input_file, 'r', newline='') as filereader:
with open(input_file, 'r') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		header = filereader.readline() # 헤더행

# 데이터 분석을 위한 기본 템플릿
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filewriter.write(','.join(map(str,header_list))+'\n')

# 데이터 분석이 필요하지 않는 경우에는 아래와 같이 코드를 간소화 할수 있다.
# 		filewriter.write(header)

		for row in filereader:
 # 데이터 분석을 위한 기본 템플릿
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')
# 단순히 copy & paste가 목적이라면 아래와 같이 간소화 할 수 있다.
# 		filewriter.write(row)