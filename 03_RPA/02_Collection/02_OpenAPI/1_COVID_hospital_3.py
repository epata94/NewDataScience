import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=="

def get_request_url():
    url = "http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList"
    params = {'serviceKey': access_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
        # return response.content
    else:
        print(f"비정상 response: status_code => {response.status_code} ")
        return None


raw_xml = get_request_url()
parse_xml = fromstring(raw_xml)
ElementTree(parse_xml).write('코로나19관련_병원정보_응답.xml', encoding='utf-8')

