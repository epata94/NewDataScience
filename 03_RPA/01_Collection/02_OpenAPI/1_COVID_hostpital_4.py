# 목적: XML 데이터를 데이터 프레임으로 변환 테스트

from xml.etree.ElementTree import parse
import pandas as pd

def xml_to_df(data_root,data_root_name):
    all_data=[]
    column_list =[]
    is_column_list = False
    for row in data_root.iter(data_root_name):
        row_data = []
        is_first = True
        for column in row.iter():
            if is_first:
                is_first = False
                continue
            row_data.append(column.text)
            if not is_column_list:
                column_list.append(column.tag)

        is_column_list = True
        all_data.append(row_data)

    return column_list, all_data

tree = parse("코로나19관련_병원정보_응답.xml")
data_root = tree.getroot().find('body').find('items')

column_list, all_data = xml_to_df(data_root,'item')

df = pd.DataFrame(all_data, columns=column_list)
print(df)

df.to_csv('코로나19관련_병원정보_응답.csv', index=False)