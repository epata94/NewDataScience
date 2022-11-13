'''
1. tag 속성과 내용 가져오기
2. 정규표현식으로 속성값 가져오기

 tag element : tag + attr + content
 ex) <a href ='www.naver.com'>네이버</a>
'''

from bs4 import BeautifulSoup # html 파싱

# 1. 로컬 파일 가져오기
file = open("chapter09/data/html02.html", mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')

# 3. tag 속성 찾기
links = html.find_all('a') # list 반환
print('links size=', len(links))

for link in links :
    #print(link) # element
    #print(link.attrs) # dict
    try :
        print(link.attrs['href']) # 5개
        print(link.attrs['target']) # 1개 - error(1,2,4,5)
    except Exception as e :
        print('예외발생 : ', e)

for link in links :
    if 'target' in link.attrs :
        print(link.attrs['href'])
        print(link.attrs['target'])
    else :
        print(link.attrs['href'])


# 정규표현식으로 속성값 가져오기
# href = "http://~
import re

patt=re.compile('http://') # pattern object 생성
links = html.find_all(href = patt)
print(links) # list
# [<a href="http://www.naver.com">네이버</a>, <a href="http://www.naver.com" target="_blank">네이버 새창으로</a>, <a href="http://www.duam.net">다음</a>]

for link in links :
    print(link.string) # 내용
    print(link.attrs['href']) # 속성값

'''
네이버
http://www.naver.com
네이버 새창으로
http://www.naver.com
다음
http://www.duam.net
'''


















