import urllib.request
import datetime
import json
import time
import pandas
import pandas as pd

# access_key="VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D"
access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ%2FmOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA%3D%3D"

def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    # end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    end_point = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=100"
    parameters += "&dataType=JSON"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    all_data = []
    column_list = ['baseDate', 'baseTime', 'category', 'nx', 'ny', 'obsrValue']
    if (jsonData['response']['header']['resultMsg'] == 'NORMAL_SERVICE'):
        for record in jsonData['response']['body']['items']['item']:
            row_data=[]
            for column in column_list:
                row_data.append(record.get(column))
            all_data.append(row_data)

    df = pd.DataFrame(all_data,columns=column_list)

    file_name = '초단기실황조회_%s%s.csv' % (yyyymmdd,day_time)

    df.to_csv(file_name, index=False)

    print(f'{file_name} SAVED\n')

def get_Realtime_Weather_Info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_time = time.strftime("%H%M", time.localtime(time.time()))

    day_hour = time.strftime("%H")
    day_min = time.strftime("%M")

    day_time = time.strftime("%H%M", time.localtime(time.time()))
    # Make_Weather_Json(day_time)
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 정확히 30분을 뺀다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")

# 구로동 좌표
x_coodinate = "58"
y_coodinate = "125"

get_Realtime_Weather_Info()