import urllib.request
import json
from datetime import datetime, timedelta

import pandas as pd
import cx_Oracle

access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ%2FmOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA%3D%3D"

def get_request_url(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스)

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + hhmm
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

    now = datetime.now()

    if now.minute >= 40 and now.minute < 60:
        print(f"현재 시간대 정보로 업데이트 합니다.: {now}")
        return now
    else:
        update_cycle_min = timedelta(minutes=40)
        lastest_time = now - update_cycle_min
        print(f"이전 시간대 정보로 업데이트 합니다.: {lastest_time}")
        return lastest_time



def preprocessed_df_to_oracle(df):
    sql_insert = '''
            insert into weather(DATE_TIME, NX, NY, 시간1_강수량, 강수형태, 기온, 습도, 풍향,풍속,동서바람성분,남북바람성분) 
            values(:DATE_TIME, :NX, :NY, :시간1_강수량, :강수형태, :기온, :습도, :풍향,:풍속,:동서바람성분,:남북바람성분)
            '''
    DATE_TIME = df.iloc[0]['DATE_TIME']
    NX = int(df.iloc[0]['NX'])  # int 값에 대해서는 int 형으로 변환해줘야 한다.
    NY = int(df.iloc[0]['NY'])
    시간1_강수량 = df.iloc[0]['시간1_강수량']
    강수형태 = df.iloc[0]['강수형태']
    기온 = df.iloc[0]['기온']
    습도 = df.iloc[0]['습도']
    풍향 = df.iloc[0]['풍향']
    풍속 = df.iloc[0]['풍속']
    동서바람성분 = df.iloc[0]['동서바람성분']
    남북바람성분 = df.iloc[0]['남북바람성분']

    cur.execute(sql_insert,
                (   DATE_TIME, NX, NY, 시간1_강수량, 강수형태, 기온,
                    습도, 풍향, 풍속, 동서바람성분, 남북바람성분 )
                )

    con.commit()

def preprocess_df (df):
    df.insert(0,'DateTime',df['baseDate']+df['baseTime'])
    nx = df.loc[0,'nx']
    ny = df.loc[0,'ny']
    date_time = df.loc[0, 'baseDate'] + ' ' + df.loc[0, 'baseTime']
    p_df = pd.pivot_table(df,index='DateTime',columns=['category'], values='obsrValue')
    p_df.insert(0,'date_time',[date_time])
    p_df.insert(1,'nx',[nx])
    p_df.insert(2,'ny',[ny])

    p_df.rename(columns={'date_time': 'DATE_TIME', 'nx': 'NX', 'ny': 'NY', 'PTY': '강수형태', 'REH': '습도',
                       'RN1': '시간1_강수량','T1H':'기온','UUU':'동서바람성분','VEC':'풍향','VVV':'남북바람성분','WSD':'풍속'}, inplace=True)
    redefined_columns = ['DATE_TIME','NX','NY','시간1_강수량','강수형태','기온','습도', '풍향','풍속','동서바람성분','남북바람성분']
    p_df = p_df[redefined_columns]
    return p_df

con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
cur = con.cursor()

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# 업데이트는 40~60 사이에 이루어짐
request_time = get_update_time_info()
yyyymmdd = request_time.strftime("%Y%m%d")
hhmm = request_time.strftime("%H%M")

# 구로동 좌표
x_coodinate = "58"
y_coodinate = "125"

raw_str_json = get_request_url(url)

if raw_str_json:
    raw_json = json.loads(raw_str_json)

column_list, all_data = json_to_df_info(raw_json)

df = pd.DataFrame(all_data, columns=column_list)

df_preprocessed = preprocess_df (df)

preprocessed_df_to_oracle(df_preprocessed)