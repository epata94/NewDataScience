'''
<BeautifulSoup library install>
 1. cmd 명령후 install
 C:\\Users>pip install beautifulsoup4
 
 2. install 후 package 설치 확인 
 C:\\Python36\\Lib\\site-packages\\beautifulsoup4-4.6.3.dist-info
 C:\\Python36\\Lib\\site-packages\\bs4
 
1. tag 이름으로 추출 
2. find()함수로 추출 
'''

import urllib.request # 원격 서버 파일 요청
from bs4 import BeautifulSoup # html 파싱

# 요청할 url
url = 'http://www.naver.com/index.html'

# 1. 원격 서버 파일 요청
res = urllib.request.urlopen(url) # web 문서 get 
data = res.read() # text 형태로 읽음

# 2. source 디코딩
src = data.decode("utf-8") # 디코딩
print('source')
print(src)


# 3. html 파싱
html = BeautifulSoup(src, 'html.parser') # html source 파싱
print('html 파싱')
print(html)

# 4. 태그 내용
a = html.find('a')
print('a tag : ', a)
print('a tag 내용 : ', a.string)

'''
a tag :  <a href="#news_cast" onclick="document.getElementById('news_cast2').tabIndex = -1;document.getElementById('news_cast2').focus();return false;"><span>연합뉴스 바로가기</span></a>
a tag 내용 :  연합뉴스 바로가기
'''



