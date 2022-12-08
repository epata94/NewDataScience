#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'sales_2013.xlsx'
output_file = 'output_files/3output_pandas.xlsx'

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

print(data_frame.dtypes)

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()