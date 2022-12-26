# 목적: 전체 수집 데이터를 데이터 프레임으로 전환
import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring
import pandas as pd

access_key = 'bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=='
TOTAL_NUM = 102
MAX_TRANSACTION = 30

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

def get_request_url(page_no):
    url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
    params = {'serviceKey': access_key , 'numOfRows' : MAX_TRANSACTION, 'pageNo' : page_no}
    response = requests.get(url, params=params)
    return response.text

request_total_num = ( TOTAL_NUM // MAX_TRANSACTION) + 1
rename_dict = {'adtFrDd': '운영가능일자', 'sgguNm': '시군구명', 'sidoNm': '시도명', 'spclAdmTyCd': '구분코드', 'telno': '전화번호',
                   'yadmNm': '기관명'}
REDEFINE_COLUMNS = ['기관명','구분코드','시도명','시군구명','전화번호','운영가능일자']
all_data = pd.DataFrame(columns=REDEFINE_COLUMNS)
for page_no in range (1, request_total_num +1):
    raw_xml = get_request_url(page_no)
    root = fromstring(raw_xml)

    data_root = root.find('body').find('items')
    column_list, page_data = xml_to_df(data_root, 'item')

    df = pd.DataFrame(page_data, columns=column_list)
    df.rename(columns=rename_dict, inplace=True)
    df = df[['기관명', '구분코드', '시도명', '시군구명', '전화번호', '운영가능일자']]
    all_data = pd.concat([all_data, df], ignore_index=True)

print(all_data.shape)

all_data.to_csv('코로나19관련_병원정보_통합.csv', index=False, encoding='cp949')