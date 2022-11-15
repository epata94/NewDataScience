import urllib.request
import datetime
import json
import time

access_key=""
yyyymmdd=''

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
    end_point = "" # ForecastTimeData 서비스를 이용할 것

    parameters = "" # 메뉴얼을 보고 요청 메세지를 완성할 것

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)


def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    # jsonData를 parsing 하여 json_weather_result에 저장된 예제 셈플을 참고하여 데이터를 저장한다.

    with open('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd,day_time), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():
    pass
#	시간 정보를 보정하여 Make_Weather_Json()를 호출한다.
    

json_weather_result = []

#동구 신암동의 좌표를 세팅한다.
x_coodinate = ""
y_coodinate = ""

get_Realtime_Weather_Info()