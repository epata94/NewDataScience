# 실시간 고속도로 정체상황
# http://data.ex.co.kr/openapi/basicinfo/openApiInfoM?apiId=0406&serviceType=OPENAPI&keyWord=%EC%8B%A4%EC%8B%9C%EA%B0%84&searchDayFrom=2014.12.01&searchDayTo=2022.12.16&CATEGORY=&GROUP_TR=

import urllib.request
import datetime
import json
import time

url ="http://data.ex.co.kr/openapi/odtraffic/trafficAmountByCongest?key=test&type=json"

def get_request_url(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
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
response_data = get_request_url(url)
if (response_data == None):
    print('No response')
else:
    raw_data = json.loads(response_data)

print(type(raw_data))