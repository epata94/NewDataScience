#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'supplier_data_unnecessary_header_footer.csv'
output_file = 'output_files/11output_pandas_backup.csv'

# header=None => 첫번째 행이 헤더로 되는 것을 방지하기 위한 인자
data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])

# drop후 첫번째 행을 헤더로 지정하기 위한 코드
data_frame.columns = data_frame.iloc[0]
# data_frame = data_frame.drop(3)
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)