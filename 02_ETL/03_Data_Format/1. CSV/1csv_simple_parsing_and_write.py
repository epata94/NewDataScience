# 목적: CSV 파일 읽고 쓰기
input_file = 'supplier_data_org.csv'
output_file = 'output_files/1output_index_false.csv'

# with open(input_file, 'r', newline='') as filereader:
with open(input_file, 'r') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		# readline()는 현재 줄을 읽고 파일포인터의 위치를 다음 라인으로 이동한다.
		# 파일포인터: 현재 파일에서 읽기 또는 쓰기 작업을 하기 위한 텍스트 위치
		header = filereader.readline() # 헤더행

# 데이터 분석을 위한 기본 템플릿
		header = header.strip()
		# csv 파일 열단위 구분을 위해 ,로 분리
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