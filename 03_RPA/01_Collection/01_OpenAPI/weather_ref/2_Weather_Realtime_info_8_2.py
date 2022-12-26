# * 목적: 열 데이터 추가 자동화

import urllib.request
import datetime
import json
import time
from datetime import datetime

import pandas as pd

access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ%2FmOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA%3D%3D"

def get_request_url(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스)

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=30"
    parameters += "&dataType=JSON"
    url = url + parameters

    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None


def json_to_df_info(raw_json):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수

    all_data=[]
    column_list = ['baseDate', 'baseTime', 'category', 'nx', 'ny', 'obsrValue']
    for record in raw_json['response']['body']['items']['item']:
        # 이하 프로그램을 학생을이 작성하게 해볼것2
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data

def get_update_time_info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_time = time.strftime("%H%M", time.localtime(time.time()))

    day_hour = time.strftime("%H")
    day_min = time.strftime("%M")

    day_min_int = int(day_min)
    if 30 <= day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M")
        print("\n<<실시간 정보 업데이트를 실시합니다!!>>\n".center(30))

    elif 0 <= day_min_int < 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 시간은 60분 단위 이므로 30분 미만은 30분을 빼고 60을 더한다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신정보 업데이트를 실시합니다!!>>\n".center(30))
    return day_time

def preprocess_df (df):
    # raw format
    # baseDate, baseTime, category, nx, ny, obsrValue
    # 20221227, 0500, PTY, 58, 125, 0
    # ........

    # Target format
    # date_time     nx ny   pty reh rn1 t1h uuu vec vvv wsd
    # 202212270500  58 125   0  ...............

    # 학생들이 병합할 수 있는 시간 5분

    # df['DateTime'] = df['baseDate']+df['baseTime']
    df.insert(0,'DateTime',df['baseDate']+df['baseTime'])
    # df.drop(['baseDate','baseTime'], axis=1, inplace=True)
    nx = df.loc[0,'nx']
    ny = df.loc[0,'ny']
    date_time = df.loc[0, 'baseDate'] + ' ' + df.loc[0, 'baseTime']
    preprocess_df = pd.pivot_table(df,index='DateTime',columns=['category'], values='obsrValue')
    preprocess_df.insert(0,'date_time',[date_time])
    preprocess_df.insert(1,'nx',[nx])
    preprocess_df.insert(2,'ny',[ny])
    return preprocess_df

    # 다하고 전처리를 수집 파트, 전처리 파트, 데이터 베이스 파트 어디에서 하는 것이 좋은지 생각해 보자.

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# 업데이트는 30~60 사이에 이루어짐
yyyymmdd = time.strftime("%Y%m%d")
day_time = get_update_time_info()

# 구로동 좌표
x_coodinate = "58"
y_coodinate = "125"

raw_str_json = get_request_url(url)
if raw_str_json:
    raw_json = json.loads(raw_str_json)

column_list, all_data = json_to_df_info(raw_json)

df = pd.DataFrame(all_data, columns=column_list)

df_preprocessed = preprocess_df (df)

file_name = '초단기실황조회_%s%s.csv' % (yyyymmdd, day_time)

df_preprocessed.to_csv(file_name,index=False)

print(f'{file_name} SAVED\n')
