#!/usr/bin/env python3
import sys
import pandas as pd

input_file = 'supplier_data.csv'
# output_file = 'output_files/1output_index_false_pandas.csv'
output_file = 'output_files/2output_index_true_pandas.csv'

data_frame = pd.read_csv(input_file)
print(data_frame)
# data_frame.to_csv(output_file, index=False)
data_frame.to_csv(output_file, index=True)
