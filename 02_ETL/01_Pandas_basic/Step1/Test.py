import pandas as pd
import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

my_encoding = find_encoding('../data/korea_movie_list.csv')

df_2 = pd.read_csv('../data/korea_movie_list.csv', encoding=my_encoding)

pass