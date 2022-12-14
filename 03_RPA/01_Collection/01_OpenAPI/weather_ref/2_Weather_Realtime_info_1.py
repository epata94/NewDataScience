# 목적: 셈플 프로그램 검증
# 실패시 Workaround
# 키를 Encoding, Decoding을 교체하며 시도한다.
# dataType 인자명을 _type으로 변경해본다.
import time
import requests
# Encoding
# access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ%2FmOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA%3D%3D"
# Decoding
access_key = "bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=="

def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'base_date': base_date , 'base_time' : day_time, 'nx' : x_coodinate,'ny': y_coodinate, 'dataType': 'JSON' }
    # params = {'base_date': base_date , 'base_time' : day_time, 'nx' : x_coodinate,'ny': y_coodinate, '_type': 'JSON' }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print(f'비정상 응답: status_code => {response.status_code}')
        return None

base_date = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")

# 구로동 좌표
x_coodinate = "58"
y_coodinate = "125"


get_request_url()