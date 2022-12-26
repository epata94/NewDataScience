# * 목적: 업데이트 주기에 맞추어 시간 파라메터 설정

import urllib.request
import datetime
import json
import time
from datetime import datetime

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


def get_parsed_json(raw_json):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수

    all_data=[]
    for record in raw_json['response']['body']['items']['item']:
        all_data.append({
                        'baseDate': record.get('baseDate'),
                        'baseTime': record.get('baseTime'),
                        'category': record.get('category'),
                        'nx': record.get('nx'),
                        'ny': record.get('ny'),
                        'obsrValue': record.get('obsrValue')
                                    })

    return all_data

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

parsed_json = get_parsed_json(raw_json)

file_name = '초단기실황조회_%s%s.json' % (yyyymmdd, day_time)
with open(file_name, 'w', encoding='utf8') as outfile:
    retJson = json.dumps(parsed_json, indent=4, sort_keys=True, ensure_ascii=False)

    outfile.write(retJson)

print(f'{file_name} SAVED\n')
