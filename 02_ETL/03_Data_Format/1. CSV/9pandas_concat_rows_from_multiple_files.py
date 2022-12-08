#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = '.'
output_file = 'output_files/9output_pandas.csv'

# pandas에서 분산파일을 읽거나 쓰기 위한 라이브러리는 특별히 제공되지 않는다.
all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_frames = []
for file in all_files:
	data_frame = pd.read_csv(file, index_col=None)
	all_data_frames.append(data_frame)
# axix=0 는 행단위로 concat
# axix=1 은 열단위로 concat
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)