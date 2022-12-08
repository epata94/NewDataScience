#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'sales_2013.xlsx'
output_file = 'output_files/9output_pandas.xlsx'

# sheet_name 속성을 지정하지 않고 read_excel함수를 수행하면
# 첫번쨰 워크시트만 반환함
# 모든 워크시트를 읽으려면 반드시 sheet_name=None 옵션 설정을 해야함
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
	row_output.append(data.loc[data['Sale Amount'] > 2000.0, :])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
