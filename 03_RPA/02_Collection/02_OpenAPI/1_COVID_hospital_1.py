import requests

access_key="bgOnt78reFNsTUJuAwlI30JDObTxX6hbJCxyApJCtuf3xjJZJ/mOs8Vhg3GZAsLc1fXTkQ9sjq0mTEupWDdyyA=="

# http status code
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
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

print(raw_xml)