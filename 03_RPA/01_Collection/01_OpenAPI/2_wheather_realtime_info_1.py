# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

import requests
# Encoding Key
# access_key = 'bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ%2FmOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA%3D%3D'
# Decoding key
access_key ='bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=='
def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': access_key , 'numOfRows' : 10, 'pageNo' : 1,
        'dataType': 'JSON','base_date':'20221227','base_time':'1049','nx':58,'ny':125
    }
    response = requests.get(url, params=params)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text 를 응답받기로함
    return response.text

raw_json = get_request_url()
print(raw_json)