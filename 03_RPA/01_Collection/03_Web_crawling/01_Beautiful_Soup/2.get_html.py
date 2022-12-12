import requests  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup  # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(response.content, 'html.parser')

# <table class="table_develop3">을 찾음
table = soup.find('table', {'class': 'table_develop3'})
data = []  # 데이터를 저장할 리스트 생성

def data_correction(org_text): # 데이터 보정작업
    if org_text == '\xa0':
        return 'N/A' # Not Applicable
    return org_text

# 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
for tr in table.find_all('tr'):
	# 모든 <td> 태그를 찾아서 리스트로 만듦
    tds = list(tr.find_all('td'))
    # (각 날씨 값을 리스트로 만듦)
    for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
		# <td> 안에 <a> 태그가 있으면(지점인지 확인)
        if td.find('a'):
			# <a> 태그 안에서 지점을 가져옴
            point = data_correction(td.find('a').text)
			# <td> 태그 리스트의 인덱스 1에서 날씨(하늘) 가져옴
            cloud = data_correction(tds[1].text)
            # cloud = tds[1].text
			# <td> 태그 리스트의 인덱스 2에서 시정(가시거리)를 가져옴
            visibility = data_correction(tds[2].text)
            temperature = data_correction(tds[5].text)
            wd_temp = data_correction(tds[7].text)
			# data 리스트에 지점, 날씨, 시정, 기온, 체감온도를 추가
            data.append([point, cloud,visibility, temperature,wd_temp])
#습도, 풍향, 풍속을 추가하시오
print(data)