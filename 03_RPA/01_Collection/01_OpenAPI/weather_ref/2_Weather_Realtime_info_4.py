# * 목적: JSON 데이터 JSON형태로 저장

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



url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
# 업데이트는 30~60 사이에 이루어짐
yyyymmdd='20221227'
day_time = '0350'

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
