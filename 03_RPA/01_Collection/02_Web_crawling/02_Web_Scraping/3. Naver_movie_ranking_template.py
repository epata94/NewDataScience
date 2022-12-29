import urllib.request
from bs4 import BeautifulSoup


html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
print(soup.prettify()) # 원본 HTML의 indentation에 맞게 변경


tags =  soup.findAll('div', attrs={'class':'tit3'})
up_down =  soup.find('img', attrs={'src':'http://imgmovie.naver.net/2007/img/common/icon_na_1.gif'})

# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.

# 또는 아래와 같이 영화 정보 행을 리스트로 만들어서 복잡 리스트로 작성하여 화면에출력한다.
# [[1,'1987','N/A'],[2,'신과함께-죄와 벌','+1'],[3,'쥬만지: 새로운세계','-1']]