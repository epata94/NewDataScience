#!/usr/bin/env python3
import sys
import pandas as pd

# input_file = sys.argv[1]
input_file = 'supplier_data.csv'
output_file = 'output_files/1output_long_format_pandas.csv'

data_frame = pd.read_csv(input_file)
column_name_list = list(data_frame.columns)
print(column_name_list)
print('=======================================')
print(data_frame)
# data_frame.to_csv(output_file, index=False)
data_frame = data_frame.stack()
# data_frame.index.names
print('=======================================')
print(data_frame)
data_frame.to_csv(output_file, index=True)
