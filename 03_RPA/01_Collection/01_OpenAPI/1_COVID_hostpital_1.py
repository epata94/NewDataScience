# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

# 샘플 프로그램
# import requests
#
# url = 'http://apis.data.go.kr/B551177/StatusOfArrivals/getArrivalsCongestion'
# params ={'serviceKey' : '서비스키', 'numOfRows' : '10', 'pageNo' : '1', 'terno' : 'T1', 'airport' : 'HAN', 'type' : 'xml' }
#
# response = requests.get(url, params=params)
# print(response.content)
import requests
access_key = 'bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=='
def get_request_url():
    url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
    params = {'serviceKey': access_key , 'numOfRows' : 10, 'pageNo' : 1}
    response = requests.get(url, params=params)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text 를 응답받기로함
    return response.text

raw_xml = get_request_url()
print(raw_xml)